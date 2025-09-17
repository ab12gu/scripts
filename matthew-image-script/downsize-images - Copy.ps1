Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# --- Helper function for GUI input ---
function Show-InputBox([string]$prompt, [string]$title, [string]$default) {
    $form = New-Object System.Windows.Forms.Form
    $form.Text = $title
    $form.Size = New-Object System.Drawing.Size(400,120)
    $form.StartPosition = "CenterScreen"

    $label = New-Object System.Windows.Forms.Label
    $label.Text = $prompt
    $label.AutoSize = $true
    $label.Location = New-Object System.Drawing.Point(10,10)
    $form.Controls.Add($label)

    $textbox = New-Object System.Windows.Forms.TextBox
    $textbox.Location = New-Object System.Drawing.Point(10,35)
    $textbox.Size = New-Object System.Drawing.Size(360,20)
    $textbox.Text = $default
    $form.Controls.Add($textbox)

    $okButton = New-Object System.Windows.Forms.Button
    $okButton.Text = "OK"
    $okButton.Location = New-Object System.Drawing.Point(150,65)
    $okButton.Add_Click({ $form.Tag = $textbox.Text; $form.Close() })
    $form.Controls.Add($okButton)

    $form.ShowDialog() | Out-Null
    return $form.Tag
}

try {
    # --- Select source folder ---
    $folderBrowser = New-Object System.Windows.Forms.FolderBrowserDialog
    $folderBrowser.Description = "Select the folder containing images"
    $folderBrowser.ShowNewFolderButton = $false
    if ($folderBrowser.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) { exit }
    $sourceFolder = $folderBrowser.SelectedPath

    # --- Enter new folder name ---
    $newFolderName = Show-InputBox "Enter the name of the new folder to save resized images:" "New Folder Name" "ResizedImages"
    if ([string]::IsNullOrWhiteSpace($newFolderName)) { exit }
    $destinationFolder = Join-Path $sourceFolder $newFolderName
    if (-not (Test-Path $destinationFolder)) { New-Item -Path $destinationFolder -ItemType Directory | Out-Null }

    # --- Enter new width and height ---
    $newWidth = Show-InputBox "Enter new image width (pixels):" "Width" "800"
    $newHeight = Show-InputBox "Enter new image height (pixels):" "Height" "600"

    if (-not ($newWidth -as [int]) -or -not ($newHeight -as [int])) {
        [System.Windows.Forms.MessageBox]::Show("Invalid width or height. Exiting.")
        exit
    }

    $newWidth = [int]$newWidth
    $newHeight = [int]$newHeight

    # --- Get all images in folder (case-insensitive) ---
    $images = Get-ChildItem -Path "$sourceFolder\*" -File | Where-Object { 
        $_.Extension -match '^\.(jpg|jpeg|png|bmp|gif)$' 
    }

    if ($images.Count -eq 0) {
        [System.Windows.Forms.MessageBox]::Show("No images found in the folder.", "Info")
        exit
    }

    # --- Resize each image ---
    foreach ($image in $images) {
        $img = [System.Drawing.Image]::FromFile($image.FullName)
        $resizedImg = New-Object System.Drawing.Bitmap $newWidth, $newHeight
        $graphics = [System.Drawing.Graphics]::FromImage($resizedImg)
        $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graphics.DrawImage($img, 0, 0, $newWidth, $newHeight)
        $destinationPath = Join-Path $destinationFolder $image.Name
        $resizedImg.Save($destinationPath)
        $graphics.Dispose()
        $resizedImg.Dispose()
        $img.Dispose()
    }

    [System.Windows.Forms.MessageBox]::Show("All images resized and saved to:`n$destinationFolder", "Done")

} catch {
    [System.Windows.Forms.MessageBox]::Show("Error: $($_.Exception.Message)", "Error")
}

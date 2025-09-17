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

    # --- Enter target size (largest side in pixels) ---
    $targetSizeStr = Show-InputBox "Enter the desired size for the largest side of the image (pixels):" "Resize Images" "800"
    if (-not ($targetSizeStr -as [int])) {
        [System.Windows.Forms.MessageBox]::Show("Invalid size. Exiting.")
        exit
    }
    $targetSize = [int]$targetSizeStr

    # --- Get all images in folder (case-insensitive) ---
    $images = Get-ChildItem -Path "$sourceFolder\*" -File | Where-Object { 
        $_.Extension -match '^\.(jpg|jpeg|png|bmp|gif)$' 
    }

    if ($images.Count -eq 0) {
        [System.Windows.Forms.MessageBox]::Show("No images found in the folder.", "Info")
        exit
    }

    # --- Resize each image proportionally ---
    foreach ($image in $images) {
        try {
            $img = [System.Drawing.Image]::FromFile($image.FullName)

            # Calculate proportional width and height
            $maxSide = [Math]::Max($img.Width, $img.Height)
            $scale = $targetSize / $maxSide
            $newWidth = [Math]::Round($img.Width * $scale)
            $newHeight = [Math]::Round($img.Height * $scale)

            $resizedImg = New-Object System.Drawing.Bitmap $newWidth, $newHeight
            $graphics = [System.Drawing.Graphics]::FromImage($resizedImg)
            $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
            $graphics.DrawImage($img, 0, 0, $newWidth, $newHeight)

            $destinationPath = Join-Path $destinationFolder $image.Name
            $resizedImg.Save($destinationPath)

            $graphics.Dispose()
            $resizedImg.Dispose()
            $img.Dispose()
        } catch {
            [System.Windows.Forms.MessageBox]::Show("Skipping file '$($image.Name)' – not a valid image.", "Warning")
        }
    }

    [System.Windows.Forms.MessageBox]::Show("All valid images resized and saved to:`n$destinationFolder", "Done")

} catch {
    [System.Windows.Forms.MessageBox]::Show("Error: $($_.Exception.Message)", "Error")
}

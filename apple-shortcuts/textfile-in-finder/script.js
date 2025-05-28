function run(input, parameters) {
	var finder = Application('Finder');
	finder.includeStandardAdditions = true;
	var currentPath = 
		decodeURI(finder.windows[0].target().url().slice(7));
	return currentPath;
}

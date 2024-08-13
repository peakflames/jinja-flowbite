Write-Host "Clean build and dist directories...."
Remove-Item -Recurse -Force .\build
Remove-Item -Recurse -Force .\dist

Write-Host "Activating venv...."
& .\venv\Scripts\activate

Write-Host "Building wheel package...."
& python setup.py bdist_wheel

Write-Host "Publishing to pypy...."
& py -m twine upload --repository pypi dist/* --verbose

Write-Host "Successfully published...." -ForegroundColor Green
#Created By @LuckytThandel
$File = Read-Host -Prompt "File Path "
$num = Read-Host -Prompt "Outcome Length "
$mode = Read-Host -Prompt "Mode [0,1,2] "
$Output_File = Read-Host -Prompt "Output File: "
$File_exist = Test-Path $File

if ($File_exist) {
	
	Write-Host "Working on It`n" -ForegroundColor Green
	$content = Get-Content -Path $File
    $cons = 0
	foreach($line in $content) {
        $py_version = python -V
	    if ($py_version -like "*3*") {
            try{
                python C:\Users\LuckyThandel\Documents\Sequence_creator\main.py "$line" $num -m $mode -o $Output_File
                Write-Host "`nLine $cons completed" -ForegroundColor Green
                $cons +=1
                }
            catch {
                  Write-Host "The word length seems wrong`n"
                    
                    } 
            }
        else {    
            $py_version = python3 -V
            if ($py_version -like "*3*") {
                python3 main.py $line [int]$num -m [int]$mode -o $Output_File

                    }
    
                }

	}
}
else {
    write-Host "File Doesn't Exist" -ForegroundColor Red

}
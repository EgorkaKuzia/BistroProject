function rimConvert{
  param([int] $number)

  $result = "
  $decimals = @(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1,)
  $r = @('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

  for($i = 0; $i -lt $decimals.Lenght; $i++){
    while ($number -ge $decimals[$i]{
      $result += $r[$i]
      $number -= $decimals[$i]
    }
  }
  return $result
}

$number = 2023

$rNum = rimConvert -number $number

Write-Host "$number : $rNum"

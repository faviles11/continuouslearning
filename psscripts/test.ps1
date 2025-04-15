param (

[string]$UserId,

[string]$PhoneNumber

)



$paramConnectMgGraph = @{

Scopes = 'User.ReadWrite.All', 'Group.ReadWrite.All', 'Directory.ReadWrite.All', 'UserAuthenticationMethod.ReadWrite.All'

TenantId = <'Tenant ID>’ 

ClientId = <'ClientId>’

#ClientSecretCredential = $ClientSecretCredential

NoWelcome = $true

}



try {

# Add a new phone method for MFA using the provided phone number

$UserId='b181a3e6-c379-4192-9541-7bb7e9d82c98'

$PhoneNumber='248-705-6071'

Write-Output "Connectiong to MgGraph"



Connect-MgGraph @paramConnectMgGraph



Write-Output "Check if user MFA Enabled"



$userMethods = Get-MgUserAuthenticationMethod -UserId $UserId



$mfaEnabled = $userMethods.AuthenticationMethod | Where-Object { $_.methodType -eq 'phone' -or $_.methodType -eq 'email' }



if($mfaEnabled.Count -gt 0){

    Write-Output "MFA is Enabled"

}

else{

    Write-Output "MFA is Not Enabled"

}



Write-Output "Enabling user MFA"

New-MgUserAuthenticationPhoneMethod -UserId $UserId -PhoneNumber $PhoneNumber -PhoneType mobile

Write-Output "MFA enabled for user with ID: $UserId"

} catch {

# Catch and display any errors that occur during the MFA enabling process

Write-Error "Failed to enable MFA for user with ID: $UserId. Error: $_"

}
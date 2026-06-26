# Netskope Docs — Client
_Generated: 2026-06-26 10:05 UTC_
_Pages: 94_

---
## Allowlist the Netskope Client
**URL:** https://docs.netskope.com/en/allowlist-the-netskope-client/
**Last Modified:** 2025-08-31T01:50:51+00:00
**Scraped:** 2026-06-26T08:58:31.596617+00:00

Allowlist the Netskope Client
Some endpoint security software or Anti-Virus/Anti-Malware engines may mark the Netskope Client as malicious (because it attempts to intercept all internet-bound traffic for the purposes of forwarding it to the Netskope Cloud), and can block it from running.
Therefore it is important to allowlist/ permit Netskope Client processes, services, and folders in any AV and/or other security agents running on the endpoint. To learn more, view
Allowlist Folders and Files
.
In this Topic
Allowlist the Netskope Client

---
## Configure Netskope Client Settings
**URL:** https://docs.netskope.com/en/configure-netskope-client-settings/
**Last Modified:** 2025-08-31T01:50:50+00:00
**Scraped:** 2026-06-26T08:59:04.138519+00:00

Configure Netskope Client Settings
The Netskope Client has a range of settings that are controlled centrally by administrators; for example: Tamperproofing settings, Software Update settings, and on-premises detection.
Settings profiles can be applied globally or targeted towards specific groups of users. Just like the Steering Profile Configuration, there is a default settings configuration that is used as a fallback or in the absence of any other profiles.
Go to
Settings > Security Cloud Platform > Devices
, and click
Client Configurations
.
The Devices page shows a list of all devices that have been deployed with the Netskope Client.
Create or Edit a Client Configuration Profile
Click on the Default tenant configuration to edit the default configuration profile, or
New Client Configuration
to create a new one.
Tip
If you plan to enable tamperproofing (like disabling the ability for users to turn off the Netskope Client), you may wish to create a second configuration profile that targets your your IT team (or the team that manages your Netskope deployment), and allow then to disable the Client for troubleshooting purposes.
We recommended that you leave most of the settings under the Traffic Steering tab as the default, unless you have a specific need or reason to change them.
For full details on each option available under the Client Configuration settings, go here:
Configuring the Netskope Client
Set Software Update Preferences
The Install & Troubleshoot tab allows you to control how and when the Netskope Client is automatically updated as releases are made available.
The Netskope Client should be set to automatically update to the latest Golden Release as best practice.
Tip
We strongly recommend that you set the Client to upgrade automatically to the Latest Golden Release.
Golden Releases run a few versions behind the latest release, but are more thoroughly tested and supported for longer.
Important
Changing the Log Level (under
Advanced
) to Debug will negatively impact performance and throughput of the Netskope Client. This setting should only be used at the direction of Netskope Support for troubleshooting purposes.
Set Tamperproof Preferences
The Tamperproof tab allows control over whether end-users can freely enable/disable/stop the Netskope Client.
Tamperproof settings can be used to prevent users from disabling the Netskope Client.
Tip
For general end-users, we recommend to prevent the disabling of the Netskope Client, disable the Allow disabling of Clients option.
You should also enable password protection for Client uninstallation and service stop, which can be helpful in environments where users still have local administrator rights on their machines.
Important
No software tamperproofing is 100% effective if the end-user has local administrator privileges on their machine (as this provides them with ultimate control over the device).
We recommend that you disable administrator privileges on corporate managed machines where possible.
In this Topic
Configure Netskope Client Settings

---
## Deploy the Netskope Client
**URL:** https://docs.netskope.com/en/deploy-the-netskope-client/
**Last Modified:** 2026-05-27T08:01:40+00:00
**Scraped:** 2026-06-26T08:59:31.603968+00:00

Deploy the Netskope Client
We recommend that you enable
Secure Enrollment
.
The Netskope Client is the primary method of steering traffic to the Netskope cloud for real-time inspection, and can be deployed using multiple methods:
Email Invite
Packaging the Application, like SCCM, Intune, JAMF (recommended).
Email Invite
The user receives an email from your Netskope tenant containing a unique link (with embedded enrollment token) to download the Client.
On installation, the Client is automatically enrolled and authenticated.
Use this method for PoCs, initial testing, one-off users, or for certain small M and A scenarios.
Pros
This method is quick and easy.
No MDM or Software Push is required.
Cons
The user needs to initiate installation of the Client themselves.
The user needs local admin privileges to be able to install the Client. By default, users added via this method are not part of any group.
To send an email invite
Go to
Settings > Security Cloud Platform > Users
.
Select the desired user.
Click the “…” next to their name, and select
Send Invitation
.
The email the user receives can be customized by going to
Settings > Tools > Templates
, and editing the
Email Invitation
template.
Packaging the Application
This is the best method for production deployment and full-scale rollout.
Requires SCIM integration with a cloud identity provider (like Microsoft Entra ID, Okta).
Relies on the UPN of the logged in user to authenticate. This must match the identity provider.
Pros
Installation is silent: Users do not know that an agent is pushed and no interaction from the user is required.
No requirement for a user to have local admin privileges.
Use of the client can be enforced through MDM, Group, or Company policy.
The client can be installed within multi-user environments (eg: Citrix) and is fully supported.
Cons
Company change control process typically needs to be followed before the Client can be pushed (and this can take time).
Some smaller companies may not have the software to push the Client or manage devices.
If the UPN of the logged in user does not match the directory, the Client can instead be rolled out to authenticate the user via SAML/SSO.
See here for more information
.
To package the client, follow the instructions in one of the links below:
Microsoft Endpoint Configuration Manager / SCCM
Microsoft Intune
Microsoft Group Policy Object (GPO)
Omnissa Workspace One
JAMF
Kandji
XenMobile
MobileIron
Core
/
Cloud
Note
You do not need to use the Directory Importer tool if you have synchronized your users using SCIM in
Integrate an Identity Provider (IdP)
of this guide, despite what the linked documentation (in the bulleted list above) might say.
Sample CLI
msiexec /I
C:NetskopeInstallerPkgnsclient-<ver>.msi
host=<addon URL> token=<orgID> tenant=<tenant-name> domain=<tenant-domain-name> installmode=IDP mode=peruserconfig enrollauthtoken=<auth token> enrollencryptiontoken=<encryption token> prelogonuser=<user>@prelogon.netskope.com
<ver>
is the version of the Netskope client package downloaded.
<orgID>
is your Organization ID. This is located at
Settings > Security Cloud Platform > MDM Distribution
. Under “Create VPN Configuration”, copy the Organization ID string.
<tenant-name>
is the name of your tenant from Step 1. This is the subdomains proceeding the goskope.com in the URL used to access the Admin Control. For example, if you access the Admin Console at https://lightwave.goskope.com, then your tenant name would be lightwave. If you access the Admin Console at https://lightwave.au.goskope.com, then your tenant name would be lightwave.au
For a full list of command line parameters, see Table 15
here
.
In this Topic
Deploy the Netskope Client

---
## Netskope Client Videos
**URL:** https://docs.netskope.com/en/netskope-client-videos/
**Last Modified:** 2025-08-31T01:50:58+00:00
**Scraped:** 2026-06-26T08:59:57.350638+00:00

Netskope Client Videos - Netskope Knowledge Portal
Netskope Client Videos
Deploying Netskope Client with Email Invitation
Deploying Netskope Client with AirWatch
Deploying Netskope Client with JAMF: UPN & Multi-User Modes
Deploying Netskope Client with JAMF: Email Mode
Deploying Netskope Client with JAMF: Non-AD Joined Mac OS Devices
In this Topic
Netskope Client Videos

---
## Allow Users to Disable Private App Segment Access on the Netskope Client
**URL:** https://docs.netskope.com/en/allow-users-to-disable-private-apps-access-on-the-netskope-client/
**Last Modified:** 2026-01-14T23:14:26+00:00
**Scraped:** 2026-06-26T09:01:26.914762+00:00

Allow Users to Disable Private App Segment Access on the Netskope Client - Netskope Knowledge Portal
Allow Users to Disable Private App Segment Access on the Netskope Client
You can allow users to disable the Client for Private App Segment Access using the Client Configuration settings.
Note
This feature is supported on Windows and is also available on macOS starting with version 119.0. If you want to enable this feature, contact your sales team.
Go to
Settings > Security Cloud Platform
and click
Client Configuration
.
On the Tamperproof tab, enter a name, select a user group, and enable
Allow disabling of Private App Segments Access
.
Click
Save
.
The option to Disable or Enable Private Access is available in the Netskope Client.
For Windows
For Mac
In this Topic
Allow Users to Disable Private App Segment Access on the Netskope Client

---
## Configure Client Prelogon Connectivity
**URL:** https://docs.netskope.com/en/configure-client-prelogon-connectivity/
**Last Modified:** 2026-03-03T01:42:47+00:00
**Scraped:** 2026-06-26T09:02:49.529809+00:00

Configure Client Prelogon Connectivity
This article explains how to enable prelogon for Windows endpoints to access resources prior to user authentication on the Windows endpoint. This functionality is commonly used to access domain controllers, allowing Windows endpoints to update and/or reset their passwords when expired. The following instructions assume NPA has been set up correctly and currently provides reachability to the AD DC.
Note
Prelogon is only supported on Windows devices.
There are two contexts in which an endpoint can establish a tunnel to NPA using the Netskope Client:
In the prelogon context, the user has not yet authenticated to the Windows endpoint. The prelogon user is used to authenticate the device itself to NPA to facilitate limited access to resources.
In the user tunnel context (sometimes referred to as
postlogon
), the user has authenticated to the Windows endpoint and
logged on
. The Netskope Client seamlessly assumes this authentication and evaluates all subsequent user-generated traffic against user policies.
Important
Be sure to evaluate existing access policies to prevent overexposure before prelogon is enabled. Do not use
any user
in a policy to prevent overexposure to prelogon.
Prerequisites
The requirements for using prelogon authentication are:
Complete the recommended AD DS configuration following these
instructions
.
Access to a Windows Endpoint with permissions to install the Client.
Some device posture criteria are not applicable if the user is a prelogon user. You should consider additional controls such as device cert validation and/or CRL validation for prelogon access.
Important
Using Device Classification as a Criteria in policies with prelogon users assign to it will always show prelogon users as
unmanaged
.
Note
Always On Always Connected (AOAC) is enabled by default when Prelogon is enabled.
Use Cases
Purposes for using prelogon authentication include:
Enable a first time user on Windows to join a domain as well as reset their password.
Enable a PC to immediately mount network drives after boot up.
Provide
Always On
Security, even when a user is not logged in.
Workflow
To use Prelogon authentication:
Create or use a steering configuration.
Configure the Netskope Client.
Create a local user.
Create Real-time protection policies.
Confirm the Steering Configuration for Prelogon Authentication
In order for the Netskope Client to steer traffic destined for Private Apps and servers, such as a domain controller, the correct steering method must be applied. If a configuration is already present and globally applicable, this setting can be modified by selecting the Edit button at the top right.  Note that any change to this configuration will impact user traffic, limited to the scope of users/groups configured for these changes.  We recommend to limit the scope of such changes in production environments.  Ensure that the Client is configured to steer private apps:
Go to
Settings > Security Cloud Platform > Steering Configuration
and open or create the configuration to be used for Prelogon Authentication.
Confirm the user/user group.
Specify the Netskope Client will
steer
private apps.
Select and enable
Private App Segments
.
Click
Save
.
Configure the Netskope Client for Prelogon Authentication
After completing the above steps, and have verified that the Client is able to authenticate successfully, the Client configuration should be tuned to meet the use case and user experience requirements of the environment in which it is being deployed.
The Client Configuration allows the Netskope cloud to push updated Client versions and behaviors to endpoints transparently.  Prelogon functionality requires R94 or later.
Go to
Settings > Security Cloud Platform >
Client Configurations
and click
New Client Configuration
. Create the Device configuration to be used for Prelogon Authentication.
Go to the Private App Segment tab to set Client behaviors regarding traffic handling. This is also where you can enable prelogon, and upload a PEM file with a CA certificate to authenticate against Clients if one is preferred.  If the Device Certificate is issued by an Intermediate CA, then just the Issuing CA certificate needs to be uploaded, not the entire chain.
Note
To use PKI, additional work is required outside of the Netskope Admin Console. Each device authenticating to a Client Configuration with PKI enabled must have a device certificate available.
Enable
Prelogon for Private App Segments
.
Enter a prelogon username. Note the email address, which always ends with
@prelogon.netskope.com
. This is used to select a local user for prelogon in a Real-time Protection policy.
Note
The user needs to be different for each Client config. For example:
Client Config1: user1@prelogon.netskope.com
Client Config2: user2@prelogon.netskope.com
The Prelogon user configured through the Client configuration will be created as a member of the group to which the Client configuration is assigned.
For MSIEXEC command information, go to the Prelogon Connectivity list in the
Netskope Client Deployment Commands
section.
If
Secure Enrollment
is enabled, to enable prelogon and deploy the enroll the auth token/enroll encryption token with one msiexec command, use:
msiexec /I NSClient.msi host=
<addon URL>
token=
<orgID>
tenant=
<tenant-name>
domain=
<tenant-domain-name>
installmode=IDP mode=peruserconfig enrollauthtoken=
<auth token>
enrollencryptiontoken=
<encryption token>
prelogonuser=
<user>
@prelogon.netskope.com
When both Prelogon and Secure Enrollment are enabled, you must deploy the token regardless of the mode in which the Client was installed.
Failing to do so will result in the Prelogon user being unable to be provisioned.
To use a device certification authority, click
Select File
to upload the certificates in PEM format.
To validate the device certificate against a Certificate Revocation List, enable
Validate URL
. The URL used to validate the device comes from the CA certificate.
Enable
Start Prelogon tunnel when user tunnel disconnects
. This enables the Client to always try to re-establish the prelogon tunnel when the user tunnel switches from
connected
to
disconnected
, even when the user disables the Client.
Note
If you enable this option, users will not be able to fully disable the Client while using prelogon.  To allow users to fully disable the client, do not check this box.
If you enable this option and Periodic Re-authentication for Private Apps is also enabled, when re-authentication expires, the Prelogon tunnel will not establish.
Click
Save
.
Create a Real-time Protection Policy for Prelogon Traffic
Add the local user that will be used for prelogon to a Real-time Protection policy, and ensure that user has access to the private app defined previously. This will ensure the prelogon user can join the domain prior to the user’s successful authentication against the Netskope cloud.
Go to
Policies > Real-time Policies
and select
Private App Segment Access
from the New Policy dropdown list.
For Source, select the user(s) with
@prelogon.netskope.com
in the email address, and use
Client
for the Access Method.
For Destination (Private App Segment is preselected). Select the
Private App Segment
for prelogon users from the dropdown list.
For Profile and Action, use
Allow
.
For Set Policy, enter a policy name.
Click
Save
.
Create a Real-time Protection Policy for User Tunnel Traffic
After prelogon is enabled, a device tunnel is established leveraging the local user configured in Netskope and deployed with the Client. When the user logs into the Windows machine, the user credentials are carried over and then applied so subsequent traffic traverses the
user tunnel
, under the assumed authentication of the user that has logged into the endpoint. This seamless transition allows users to receive additional access beyond their prelogon state, by enforcing a separate set of policies tied to the user’s domain authentication. An example of such a policy is illustrated below, with the additional access to
PrivateAppTest
being granted to two domain-joined users.
Go to
Policies > Real-time Policies
and select
Private App Segment Access
from the New Policy dropdown list.
For Source, select the users and use
Client
for the Access Method.
For Destination (Private App Segment is preselected). Select the
Private App Segment
for user tunnel traffic from the dropdown list.
For Profile and Action, use
Allow
.
For Set Policy, enter a policy name.
Click
Save
.
Prelogon Troubleshooting
This article describes the troubleshooting methodology for NPA Prelogon connectivity.
User Login
When a user cannot log in to Windows and device reboot does not help, an error similar to the image shown appears.
This error indicates that logon cannot be completed due to a lack of connectivity to Active Directory Domain Controllers. There are some common cases associated with the this error:
A newly-provisioned device (for example, a brand new endpoint being onboarded via Windows Autopilot).
A user’s password is expired and there are no other cached user profiles on the endpoint.
In both cases, there is a reliance on the NPA prelogon tunnel as a connectivity method to Active Directory. Due to observed behavior with a prelogon tunnel, a user can’t get access to the device and therefore cannot collect Netskope Client logs necessary for troubleshooting.
If another user’s cached profile is present or a local administrator account is configured, those credentials should be used to gain access to the device and collect Netskope Client logs. The following recommendations will guide the troubleshooting process in the event when it is not possible to logon to the device by any means.
Device Enrollment
Check device enrollment status. In the Netskope UI, go to
Settings > Security Cloud Platform > Devices
, click
Add Filter
and
Show Pre-Logon Users
, and select
Yes
. Other filter parameters can be used to narrow down the search, as well as the time period, at the top right corner.
Successfully enrolled devices within prelogon context will appear in the list with a
_Prelogon
suffix.
If an enrolled device is found in the list, the remainder of this section can be skipped.
If a device can’t be found in the list, it may indicate issues with the Netskope Client installation and/or enrollment. You will need to investigate the Netskope Client installation status and correctness of the configuration parameters. The following sections provide troubleshooting insights.
Research Netskope Client Installation Status
For Autopilot-driven deployments, Intune is able to report Netskope Client installation status. In the Intune UI, go to
Devices > Windows > Device Name > Managed Apps
, and in the Select User dropdown list, select
Device without user
.
In case of an unknown/failed installation status, we recommend that you manually reproduce the Netskope Client installation with the same command line arguments on a managed device. Managed device OS version and Netskope Client version should be mirroring the setup used within device management tools (like Autopilot, SCCM). You should be able to interface with the device directly without any device management tools. Information about successfully reproduced errors along with Netskope Client logs should be submitted to Netskope Support.
Research Correctness of Netskope Client Configuration Parameters
In order to successfully enroll within a prelogon context, the Netskope Client should be installed with certain command line parameters. You need to validate the correctness of those parameters and its syntax, as well as if they match with appropriate Netskope tenant configuration.
For Autopilot-driven deployments those arguments can be checked in the Intune UI. In the Intune UI. Go to
Apps > Windows
, select
Netskope Client
, and then click
Properties
. Validate the data and make sure there are no extra spaces, line skips, and other syntax issues. An example of the correct command line argument string is provided below.
host=addon-
<tenant>
.goskope.com token=
<org-id token>
prelogonuser=
<user>
@prelogon.netskope.com mode=peruserconfig /qn
More information about command-line arguments can be found here
/en/netskope-client-for-windows.html
.
Research Correctness of Netskope Tenant Configuration
We recommend that you examine the Prelogon configuration settings. In the Netskope UI, go to
Settings > Security Cloud Platform > Devices
and click on the appropriate Client Configuration.
Make sure that the prelogon username created in the Client Configuration matches with the one that is used within the command line parameters for the Netskope Client installation.
Attempt to Reproduce an Issue on a Managed Device
If all the above steps do not help you find a reason why the device can’t be enrolled, you will need to manually reproduce the Netskope Client installation with the same command line arguments on a managed device. You should be able to interface with the device directly without any management tools (like Autopilot, SCCM). After the installation, examine the status for Private Access by right-clicking
Client Configuration
.
If the status is reported as
Private Access: Connected (User Tunnel)
, make sure the option
Start pre-logon tunnel when user tunnel disconnects
in the Client Configuration dialog is checked.
Disable the Netskope Client, and after a short while, check the Netskope Client configuration again. It should show the prelogon tunnel as connected.
If the prelogon tunnel state shows
Disconnected
or
N/A
, this confirms there is a problem on the managed device as well. Right-click on the Netskope Client and collect the logs bundle to share with
Netskope Support
.
Netskope Tenant Configuration for Prelogon
In the Netskope UI, go to
Settings > Security Cloud Platform > App Definition >
Private App Segments
> Troubleshooter
.
Select the required application from the dropdown list (like Active Directory), appropriate user name for prelogon Client Configuration and enrolled device, and then click
Troubleshoot
.
The Troubleshooter tool will evaluate the Netskope tenant configuration against a list of possible issues. List of the common issues are:
For a given prelogon username, the Steering Configuration is not aligned with the Client Configuration.
The Real-time Protection policy does not have the appropriate entries to allow connectivity to Active Directory resources.
The Publisher can’t connect to Active Directory resources, or an incorrect Publisher is selected for a Private App.
There are issues with machine certificate validation.
To learn more about the Troubleshooter tool, go to
Private Access Troubleshooting
.
In this Topic
Configure Client Prelogon Connectivity

---
## Use Client Re-authentication
**URL:** https://docs.netskope.com/en/use-client-re-authentication/
**Last Modified:** 2026-05-26T21:48:51+00:00
**Scraped:** 2026-06-26T09:10:51.876377+00:00

Use Client Re-authentication
The Netskope Client can require a user to re-authenticate for access to private apps. IdP federation must be configured to use this feature. The Client and IdP prerequisites are:
All users must be authenticated via the IdP and imported into your Netskope tenant. The email address of the user must be available for all IdP authenticated users.
Configure your IdP in the
Settings
>
Security Cloud Platform
>
SAML (
under the Forward Proxy section
)
in your Netskope Tenant UI. See
SAML Forward Proxy
for details.
Ensure that the URL
nsauth-
<tenant-URL>
is publicly accessible. If not, please reach out to Netskope Support.
Re-authentication is configured and enabled on the Netskope Client.
To configure Client re-authentication:
Go to
Settings > Security Cloud Platform > Netskope Client > Client Configuration
and click
New Client Configuration
.
Enter a configuration name and select a user group (or OU) from the dropdown.
On the Private App Segment tab, enable the
Periodic re-authentication for Private App Segments
checkbox.
Select a time period from the Interval dropdown for how often you want re-authentication to occur.
To allow a user time to re-authenticate after the specified interval time has expired, enable the
Grace Period
checkbox and enter the amount of minutes. The grace period must be less than the interval.
Click
Save
.
The Netskope Client menu shows when re-authentication is enabled, and allows you to re-authenticate by clicking that option on the menu.
If the interval expires, the Netskope Client prompts the IdP sign-in window for re-authentication. If the grace period expires, the Netskope Client disconnects from Netskope Private Access.
Tip
To customize the authentication frequency, which requires a customization on the IdP, refer to
Optimizing Identity Provider Settings for NPA Periodic Re-authentication
.
Re-authenticate on Logon
Netskope Private Access supports the ability to force a user to re-authenticate into the Netskope Client if the user’s device has restarted, or if the user logs out of the PC and logs back into the device. Contact
Support
to enable this functionality in your tenant.
In this Topic
Use Client Re-authentication

---
## Addressing SSL Error while Accessing AWS Services via the AWS CLI with the Netskope Client Enabled
**URL:** https://docs.netskope.com/en/addressing-ssl-error-while-accessing-aws-services-via-the-aws-cli-with-the-netskope-client-enabled/
**Last Modified:** 2025-09-16T17:32:57+00:00
**Scraped:** 2026-06-26T09:11:53.204300+00:00

Addressing SSL Error while Accessing AWS Services via the AWS CLI with the Netskope Client Enabled
The AWS CLI is a tool that can be used to interact with AWS services via any terminal program.
However, with the Netskope Client enabled, accessing the AWS services via the CLI causes an error as:
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:581)
This article describes the steps necessary to remediate this error and access AWS services via the AWS CLI tool with the Netskope Client enabled.
Root Cause
A user will typically set up their AWS using the command as below:
aws configure
They are then asked to enter the details about their access credentials and the region information.
Post providing this information the expected output is the connection to be established to the AWS instance. However, this setup fails.
Users might also see an error if they have a pre-configured AWS CLI and the Netskope Client is installed later.
In these scenarios, the users will see the following error message on executing commands:
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:581)
Both these are caused due to a certificate error. With the Netskope Client enabled, the certificate that is presented to the AWS instance is the Netskope Client certificate. As this is not the expected certificate on AWS’s end, the authentication is not complete and the initialization fails.
AWS CLI trusts only server certs issued by CAs in its private cert store. It does not use the system certificate store which has the entry for the Netskope Client cert.
Solution
Netskope Client certs need to be made available in the AWS CLI cert store for the tool to work with Netskope.
Amazon has released a version 2 of the AWS CLI.
Use the specific solution depending on the AWS CLI version installed.
AWS CLI Version 1
Depending on the device that the AWS CLI tool is being installed, you can download the scripts from the
Support
portal.
Windows users require the
ns_certbundle_aws_cli_v1.bat
script, while Mac users require the
ns_certbundle_aws_cli_v1.sh
script. Go to this
KB article
on our Support site to get these script files.
After the scripts have been downloaded, please follow the following steps:
Copy the script to the users
aws config
folder.
On Windows:
C:\Users\<<user>>\.aws
(substitute <<user>> to you Windows user).
On Mac OS:
~/.aws
Execute the script to create
netskope-cert-bundle.pem
.
Assuming the rest of the configuration is already in place, run this command to set the cert bundle in the aws config. Change cert bundle paths on Win & Mac as necessary.
aws configure set default.ca_bundle <path_to-cert_bundle>
Instead, you can use an environment variable to set the cert bundle in the
aws config
:
export AWS_CA_BUNDLE="~/.aws/nskp_config/netskope-cert-bundle.pem"
There are multiple ways to specify the CA certificate bundle to verify SSL certificates. Refer to
Configuration and Credential File Settings
for more details about setting the cert bundle. It is specific to user preference. Windows users must run the .bat file and not the .sh file.
(For Windows)
C:\Users\<<user>>\.aws\netskope-cert-bundle.pem
(For Mac)
~/.aws/netskope-cert-bundle.pem
Once these certs are set, the AWS CLI should be able to access all the AWS Services.
AWS CLI Version 2
Depending on the device that the AWS CLI tool is being installed, you can download the scripts from the
Support
portal.
Windows users require the
ns_certbundle_aws_cli_v2.bat
script, while Mac users require the
ns_certbundle_aws_cli_v2.sh
script. Go to this
KB article
on our Support site to get these script files.
After the scripts have been downloaded, please follow the following steps:
For Windows:
Create a config folder to host the script and resulting cert bundle.
mkdir C:\Program Files\Amazon\AWSCLIV2\nskp_config
Copy the script to the config folder created above.
Execute the script to create
netskope-cert-bundle.pem
.
Assuming the rest of the configuration is already in place, run this command to set the cert bundle in
aws config
.
aws configure set default.ca_bundle “C:\Program Files\Amazon\AWSCLIV2\nskp_config\netskope-cert-bundle.pem”
Instead, you can use an environment variable to set the cert bundle in the
aws config
:
export AWS_CA_BUNDLE="~/.aws/nskp_config/netskope-cert-bundle.pem"
There are multiple ways to specify the CA certificate bundle to verify SSL certificates. Refer to
Configuration and Credential File Settings
for more details about setting the cert bundle. It is specific to user preference. Windows users must run the .bat file and not the .sh file.
For Mac OS:
The AWS CLI V2 allows the installation either globally for all users or for the current user. Depending on the option selected, the path where the installation occurs differs.
For global installation, the script assumes that the installation path is the default one which is:
/usr/local/aws-cli
Create a nskp_config folder in the .aws directory to hold the certificate bundle.
mkdir ~/.aws/nskp_config
Move the downloaded script ‘ns_certbundle_aws_cli_v2.sh’ to the config folder.
mv ~/Downloads/ns_certbundle_aws_cli_v2.sh ~/.aws/nskp_config
Run the script
If the AWS CLI v2 was installed globally for all users, simply run the script:
./ns_certbundle_aws_cli_v2.sh
If the AWS CLI v2 was installed for the current user, provide the path where the AWS CLI was installed. This will be the same path as mentioned in the AWS CLI installation (in the XML file).
./ns_certbundle_aws_cli_v2.sh -p <aws_cli_install_path>
Assuming the rest of the configuration is already in place, run this command to set the cert bundle in the aws config. Change cert bundle paths on.
aws configure set default.ca_bundle ~/.aws/nskp_config/netskope-cert-bundle.pem
Instead, you can use an environment variable to set the cert bundle in the
aws config
:
export AWS_CA_BUNDLE="~/.aws/nskp_config/netskope-cert-bundle.pem"
There are multiple ways to specify the CA certificate bundle to verify SSL certificates. Refer to
Configuration and Credential File Settings
for more details about setting the cert bundle. It is specific to user preference. Windows users must run the .bat file and not the .sh file.
In this Topic
Addressing SSL Error while Accessing AWS Services via the AWS CLI with the Netskope Client Enabled

---
## Deploy Client on macOS Using Intune
**URL:** https://docs.netskope.com/en/deploy-client-on-macos-using-intune/
**Last Modified:** 2026-05-27T11:39:23+00:00
**Scraped:** 2026-06-26T09:12:09.038731+00:00

Deploy Client on macOS Using Intune - Netskope Knowledge Portal
Deploy Client on macOS Using Intune
This article provides instructions to deploy Netskope Client on macOS devices(Big Sur and later) using the Microsoft Intune. The following steps are for deploying Netskope Client on macOS devices running macOS 11.x (Big Sur) or later.
Prerequisites
Devices running macOS 11.x (Big Sur) or later.
Enroll devices in Microsoft’s Endpoint Manager.
Download Netskope Root and Intermediate certificates and convert them to the .cer extension. To learn more, see
Certificates
.
To convert certificates from .pem to .cer, run the following command in a terminal:
openssl x509 -inform PEM -in rootcaCert.pem -outform DER -out rootcaCert.cer
Ensure that users are provisioned to the Netskope tenant using SCIM or Directory Importer. To learn more about user provisioning, see
Provisioning and Authentication
and
Configure Directory Importer
.
If you are using IdP mode for the Client deployment configure and verify SAML forward proxy authentication. To learn more about SAML Forward Proxy authentication, see
Provisioning and Authentication
.
Deployment Procedure
Perform the following steps to deploy client on macOS using Intune:
Sign in to
Microsoft Intune Admin Cente
r.
Go to
Devices
>
macOS devices
. Ensure that the devices to which you will install Netskope Client are listed.
Create two configuration profiles to deploy the Netskope certificates.
Go to
macOS policies
>
Configuration Profiles
>
Create Profile
and select
Profile Type
as
Templates
and
Template name
as
Trusted Certificate
.
Click
Create
.
The page will refresh with settings.
Enter a name for the root certificate profile and click
Next
.
Click the folder icon to select the Netskope root certificate (.cer file) and click
Next
to continue.
Assign the appropriate device group and click
Next
.
Review the configuration and click
Create
.
Repeat the steps used to upload Netskope root certificate and create another configuration profile to upload Netskope intermediate certificate.
Download the Netskope Intune configuration script from
Netskope Support portal
.
Extract the contents of
MAC-MDM-script.zip
file.
Open the script in a text editor and locate the
#Intune Deployment example
section. Modify the lines by removing the comment (#).
Choose a deployment mode according to your requirement and update the script options for parameters 4 to 8 as follows for each mode:
Deployment Modes
Configuration Parameters
IDP Single-User mode
Parameter 4: Enter IDP to specify the client deployment mode is IDP.
Parameter 5: Domain name. Example, if your tenant URL is https://corp.goskope.com, then enter goskope.com.
Parameter 6: Tenant name. Example, If your tenant URL is https://corp.goskope.com, enter corp.
Parameter 7: Email Address request option. Enter 0, if you do not want to request the user’s email address. Enter 1 to request the user’s email address.
Parameter 8: Enter the ​​enrollencryptiontoken. This is the
Enforce encryption of initial configuration of Netskope Client
token that you can get if you have enabled
Secure Enrollment
in
Settings
>
Security Cloud Platform
>
MDM Distribution
>
Secure Enrollment
.
set -- 0 0 0 idp < tenant domain name > < tenant name > 0/1 enrollencryptiontoken= < Encryption token >
For example, if you have the following tenant details:
Tenant: abcde.eu.goskope.com
Organization ID: xxxxxxxxxxxxxxxxxxx
Encryption Token: yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
set -- 0 0 0 idp eu.goskope.com abcde 0 enrollencryptiontoken=yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
IDP Multi-User mode
Parameter 4: Enter IDP to specify that the client deployment is in IDP mode.
Parameter 5: Domain name. Example, if your tenant URL is https://corp.goskope.com, then enter goskope.com.
Parameter 6: Tenant name. Example, If your tenant URL is https://corp.goskope.com, enter corp.
Parameter 7: Email Address request option. Enter 0, if you do not want to request user email address. Enter 1 to request the user’s email address.
Parameter 8: Enter peruserconfig to specify multi-user IDP deployment mode.
Parameter 9: Enter the ​​enrollencryptiontoken. This is the
Enforce encryption of initial configuration of Netskope Client
token that you can get if you have enabled
Secure Enrollment
in
Settings
>
Security Cloud Platform
>
MDM Distribution
>
Secure Enrollment
.
set -- 0 0 0 idp < tenant domain name > < tenant name > 0/1 peruserconfig enrollencryptiontoken= < Encryption token >
For example, if you have the following tenant details:
Tenant: abcde.eu.goskope.com
Organization ID: xxxxxxxxxxxxxxxxxxx
Encryption Token: yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
set -- 0 0 0 idp eu.goskope.com abcde 0 peruserconfig enrollencryptiontoken=yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
For macOS devices (single-user installations) that are not AD joined
Parameter 4 : Your tenant URL. Example, If your tenant URL is https://corp.goskope.com, enter addon-corp.goskope.com.
Parameter 5: For rel 90.2 and later - Your Organization ID.
Parameter 6: Preferences file (plist)  name. When entering the filename, enter the complete filename including the .plist extension.
Example: netskope.plist . Do not add HTTP to the URL in the .plist file.
Parameter 7 : Enter the keyword preference_email.
Parameter 8: Enter the  enrollauthtoken. This is the
Enforce authentication of Netskope Client Enrollment
token that you can get if you have enabled
Secure Enrollment
in
Settings
>
Security Cloud Platform
>
MDM Distribution
>
Secure Enrollment
.
Parameter 9: Enter the enrollencryptiontoken. This is the
Enforce encryption of initial configuration of Netskope client
token that you can get if you have enabled
Secure Enrollment
is enabled in
Settings
>
Security Cloud Platform
>
MDM Distribution
>
Secure Enrollment
.
set -- 0 0 0 addon- < tenant name >.< tenant domain >.goskope.com < Org ID > < plist file name > preference_email enrollauthtoken= < authentication token > enrollencryptiontoken=< encryption token >
For example, if you have the following tenant details:
Tenant: abcde.eu.goskope.com
Organization ID: xxxxxxxxxxxxxxxxxxx
Authentication Token: zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
Encryption Token: yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
set -- 0 0 0 addon-abcde.eu.goskope.com xxxxxxxxxxxxxxxxxxx PreferenceProfileName.plist preference_email enrollauthtoken=zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz enrollencryptiontoken=yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
To learn about creating plist in Intune, view
plist in Intune
.
Save the script.
To add system extensions, go to
macOS policies
>
Configuration Profiles
>
Create Profile
and select
Profile Type
as
Settings Catalog
.
Since the template “Extensions” is deprecated by Microsoft as displayed in the following screenshot, it does not let you save the profile.
Click
Create
.
It opens the
Create Profile
window.
In
Basics
, enter a name for the profile.
Click
Next
to continue.
In
Configuration Settings
, click
+Add Settings
.
In
Settings Picker
, select a category to see all the available settings.
Select
System Configuration
>
System Extensions
.
This opens another window to configure the System Extensions payload settings for enrolled devices.
Select checkbox for
Allowed System Extensions
.
All options under
Allowed System Extensions
is selected by default.
After you select settings for
Allowed System Extensions
, go to
Configuration Settings
on the left-pane and click
+Edit Instance
.
In the
Configure Instance
window, add the following:
Bundle Identifier
:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Team Identifier:
24W52P9M7W
Click
Save
.
Click
Next
to continue.
In
Scope tags
(optional), assign a tag to a profile in a specific group.
Click
Next
to continue.
In
Assignment
, select the users or groups that will receive your profile.
Click
Next
to continue.
In
Review+Create
, you can review the policy configurations.
Click
Create
.
Use the
Profiles
options in the end-user device to validate if the System Extension was deployed successfully.
To provide full disk access permission for macOS Sonoma or later, navigate to
Dashboard
>
Devices
>
macOS
>
Configuration Profiles
>
Create Profile
>
New Policy
.
Select
Settings Catalog
from the
Templates
dropdown menu.
Click
Create
.
It opens the
Create Profile
window.
In
Basics
, enter a name for the profile.
Click
Next
to continue.
In
Configuration Settings
, click
+Add Settings
.
In
Settings Picker
, select a category to see all the available settings.
Select
Privacy
>
Privacy Preferences Policy Control
.
This opens another window to configure the privacy preferences policy control payload.
Select checkbox for
System Policy All Files
under
Services
.
All options under System Policy All Files is selected by default.
After you select settings for Privacy Preferences Policy Control, go to
Configuration Settings
on the left-pane and click
+Edit Instance
.
In the
Configure Instance
window, add the following:
Toggle to enable
Allowed
to
True
.
Code Requirement:
anchor apple generic and identifier "com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
Identifier:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Identifier Type:
Bundle ID.
You can remove the
Authorization
field under
Privacy Preferences Policy Control
. Click
next to the
Authorization
field to delete.
Click
Save
.
Click
Next
to continue.
In
Scope tags
(optional), assign a tag to a profile in a specific group.
Click
Next
to continue.
In
Assignment
, select the users or groups that will receive your profile.
Click
Next
to continue.
In
Review+Create
, you can review the policy configurations.
Click
Create
.
For Endpoint DLP, you can add the following Identifier and Code Requirement:
– Identifier: com.netskope.epdlp.client
– Code Requirement:
anchor apple generic and identifier "com.netskope.epdlp.client" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
To learn more:
Enabling Endpoint DLP on the Netskope Client for macOS
.
Go to
macOS policies
>
Configuration Profiles
.
Download custom configuration profiles from
Netskope Support Portal
. Here, click
Files
>
View Al
l to find the configuration profile file (NetskopeClient.mobileconfig).
Select
Create Profile
and under the
Profile Types
option, select
Templates
>
Custom
. Click
Create
.
It is recommended to create the Configuration Profile before deploying Netskope Client on macOS. This enables to pre-authorize the Netskope App Proxy through MDM to steer traffic silently without any end-user approval.
Specify a profile name.
Keep the
Deployment Channe
l option to
Device Channel
.
Upload the custom configuration profile downloaded from Netskope Support Portal. Click
Next
to continue.
Select and assign appropriate users or groups. Click
Next
to continue.
Review configuration and click
Create
.
Use the
Profiles
option in the end-user device to validate if the installation was successful.
If you want to create PLIST in Intune for non-AD Domain-Joined devices, go to the section
Create PLIST in Intune
.
Validate Certificate Chain
You can validate the complete certificate chain in your Mac keychain.
IdP Enrollment Workflow
If you choose to enroll Netskope Client using IdP mode in Intune, perform the following steps:
After you complete the steps to deploy Netskope Client in Intune, you will receive a notification to allow the proxy configurations.
Click
Allow
.
In
Enroll Netskope Client
, enter the
Email Address
.
Click
Next
.
Enter the tenant name and select the tenant domain as shared with the user by their respective IT.
Now, you can sign in using your authentication credential to complete the enrollment process.
Create PLIST in Intune for Non-AD domain-Joined Devices
Creating a preference file in Intune include the following steps:
Create profile with the Preference file.
Upload the script file in Intune.
To learn more, view
Add a Property List
.
Create a Profile Using the Preference File
If you are deploying a Client using a PLIST-based installation, create the Profile type as Preference file  and define the email variable with the token {{mail}}.
Follow the steps to create a profile:
Sign in to
Microsoft Intune Admin Center
.
Navigate to
Devices
>
Configuration Profiles
>
Create Profile
.
Provide the following details in Create a Profile page:
Platform:
Select macOS
Profile Type:
Templates. Select the Template name as Preference File.
Click
Create
.
In
Basics
, enter the name and description
Click
Next
.
In
Configuration Settings
, provide the following details:
Preference domain name:
Enter the bundle ID: com.netskope.client.Netskope-Client.
Upload the property list file.
<key>email</key>
<string>{{mail}}</string>
Select
Next
.
In
Scope
,  assign a tag to filter the profile to specific IT groups.
Select
Next
.
In
Assignment
, select the users or groups that will receive your profile.
Select
Next
.
In
Review + Create
, review your configuration and click
Create
.
Upload Preinstallation Script File in Intune
Perform the following steps to upload the preinstallation script using macOS app (PKG) type:
Go to
Apps
> Click Create..
Click Create.
In
Select app type
, choose
macOS app (PKG)
from the
App type
drop-down menu.
Click
Select
.
In
Select file
, click
select app package file
.
This opens a separate screen App package file.
In
app package file
, click the folder icon to select the .pkg file from your local folder.
Click
OK
.
Under
App Information
, enter the
Publisher
name
.
Click
Next
.
Under
Program
, copy and paste the Netskope Intune configuration script (downloaded from the support portal) in
Pre-install script
.
In the preinstallation script, update the Email Preference mode in the script as given in the following example:
set -- 0 0 0 addon-
<tenant-URL>
<ORG ID>
template.plist preference_email
The
template.plist
parameter must match with the
plist file name in
Configuration Settings
in this
section
. For example, add
com.netskope.client.Netskope-Client.plist
configured in this
section
.
Click
Next
.
Under
Requirements
, Select the Minimum operating system.
Click
Next
.
Under
Detection
Rules
, review the
AppleBundleIDs
.
You can remove the bundle ID com.netskope.client.nsIPFilterNKE. Click the delete icon to remove the bundle ID.
Click
Next
.
Under
Assignment
, select the users or groups that will receive your profile.
Click
Next
to continue.
Under
Review+Create
, you can review the policy configurations.
Click
Create
.
In this Topic
Deploy Client on macOS Using Intune

---
## Deploy Client on iOS Using Jamf Pro
**URL:** https://docs.netskope.com/en/deploy-client-on-ios-using-jamf-pro/
**Last Modified:** 2025-12-08T06:47:54+00:00
**Scraped:** 2026-06-26T09:12:20.251805+00:00

Deploy Client on iOS Using Jamf Pro
Jamf Pro is an enterprise mobility management tool that is used for the endpoint management of Apple iOS and macOS devices. This article provides instructions to install the Netskope Client on iOS devices using Jamf Pro.
Prerequisites
Administrators must possess proficient working knowledge of Jamf Pro.
Administrators must review
Netskope Client Client Enrollment Methods
to understand the Client User Enrollment methods available for their environment.
Import users into the Netskope tenant – see
Provisioning Users for Netskope Client
.
Download
Netskope Root and Tenant Certificates
and ensure the certificates are available when needed.
See
Deploy Netskope Client via IdP
when using IDP as the method of user enrollment.
Jamf must have a pre-existing user (email) to device mapping.
Supported Platforms and Enrollment Methods
This article outlines the Netskope Client deployment instructions for the following user enrollment methods and supported platforms. User enrollment methods not documented here are not supported at this time.
Enrollment Methods
Single User
Multi-user
PLIST
Y
N
Configuration Profile Setup
The core configuration for Client installation is managed through Jamf Configuration Profiles. The following sections provide a detailed overview of how to configure these profiles effectively.
The following can be added to a New or Existing Configuration Profile. To create a New Configuration Profile:
In the Jamf console, go to
Devices
>
Configuration
Profiles
>
New
.
Under
Options
>
General
.
Enter the display name. For example, Netskope Client Configuration Profile.
Choose the following:
Category:
None
Level:
Computer Level
Distribution Method:
Install Automatically
Click
Save
.
Click
Scope
.
Click
Targets
, then select the specific user(s) or device(s) to assign the configuration profile.
Click
Save
.
On-Demand VPN Configuration Profile
The following steps explain how to configure a Configuration Profile for an On‑Demand VPN deployment.
In the Jamf console, go to
Devices
>
Configuration
Profiles
> select required Configuration Profile
Go to
Options
>
VPN
.
Click
Configure
.
To configure On-Demand VPN:
Enter the
Connection Name
. For example, Netskope VPN.
From the options displayed in the
VPN Type
dropdown, select
VPN
.
From the options displayed under
Connection Type
, select
Custom SSL
.
Enter
com.netskope.Netskope
in the
Identifier
field.
The second Netskope in
com.netskope.Netskope
is case-sensitive and ‘ N’ must be in uppercase.
Enter
gateway-<tenant-URL>
in the
Server
field.
Replace <tenant-name> in the tenant URL with your tenant name.
To enable zero-touch deployment, provide the following key-value pair in Custom Data:
OrgKey:
<Your organization ID in the tenant>
AddonHost:
addon-<tenant-URL>.
UserEmail:
$EMAIL
enrollauthtoken:
<Secure Enrollment authentication token>
enrollencryptiontoken:
<secure enrollment encryption token> (if enabled)
– To get the OrgKey, you can log into the Netskope tenant > Settings > Security Cloud Platform > Netskope Client > MDM Distribution. Here, go to Deployment Resources for iOS and copy the Organization ID from the Create VPN Configuration.
– Ensure to provide the same email address as added in your tenant.
– The $EMAIL variable for UserEmail is case sensitive and should be all uppercase
Click the checkbox to select the option
Enable VPN On Demand
.
Provide
On Demand Rules Configuration XML
.
<array>
<dict>
<key>Action</key>
<string>Connect</string>
<key>InterfaceTypeMatch</key>
<string>WiFi</string>
</dict>
<dict>
<key>Action</key>
<string>Connect</string>
<key>InterfaceTypeMatch</key>
<string>Cellular</string>
</dict>
</array>
Disabling VPN in iOS settings terminates the extension (this is iOS design), but it is reactivated by iOS automatically on network activity if OnDemandRules are configured.
Click the checkbox to select the option
Prohibit users from disabling on-demand VPN settings
.
Click
Save
.
Per-App VPN Configuration Profile
The following steps explain how to configure a Configuration Profile for a Per-App VPN deployment
In the Jamf console, go to
Devices
>
Configuration Profiles
> select required Configuration Profile.
Go to
Options
>
VPN
.
Click
Configure
.
To configure Per-App VPN:
Enter the
Connection Name
. For example, Netskope VPN.
From the options displayed in the
VPN Type
dropdown, select
Per-app VPN
.
Select the checkbox for
Automatically start Per-App VPN connection
.
Under
Safari Domains
, you can add those domains that are allowed to use this per-app VPN in the Safari app.
This configuration is not applicable to any other browser.
From the options displayed under
Per-App VPN Connection Type
, select
Custom SSL
.
Enter
com.netskope.Netskope
in the
Identifier
field.
The second Netskope in
com.netskope.Netskope
is case-sensitive and ‘ N’ must be in uppercase.
Enter
gateway-<tenant-URL>
in the Server field.
Replace <tenant-name> in the tenant URL with your tenant name.
To enable zero-touch deployment, provide the following key-value pair in Custom Data:
OrgKey:
<Your organization ID in the tenant>
AddonHost:
addon-<tenant-URL>
UserEmail:
$EMAIL
enrollauthtoken:
<Secure Enrollment authentication token>
enrollencryptiontoken:
<secure enrollment encryption token> (if enabled)
OnDemandConnectionsHoldTimeout
: <numeric value in seconds>
This numeric value in the VPN profile can hold the connection for a longer time until it establishes the tunnel successfully and handles traffic. Netskope recommends using values that are large enough to cover normal connection time.
To know your OrgKey, AddonHost, enrollauth, and enrollencryption tokens, view
Netskope Deployment Parameters
.
From the options displayed under
User Authentication
, select
Certificate
.
From the options displayed under
Provide Type
, select
Packet-tunnel
.
For more details on Per-App VPN, refer
Configuring Per-App in Jamf Pro
.
Click
Save
.
Push Netskope Root and Tenant Certificates via Jamf
Provide additional trust to end users by pushing certificates during client installation. Before you can push the root and tenant certificates, ensure that you do the following:
Download root and tenant certificates from Netskope MDM distribution page.
Login to Netskope tenant admin console with admin credentials.
Go to
Settings
>
Security Cloud Platform
>
MDM Distribution
. The certificate download options are displayed in the Certificate Setup section.
Convert the downloaded certificates to
.cer
format by renaming the .pem files to .cer.
Perform the following steps to add certificates to Jamf:
In the Jamf console, go to
Computers
>
Configuration
Profiles
> select required Configuration Profile
Go to
Options
>
Certificate
.
Click
Configure
or
Edit
.
Enter a name for the certificates.
Select
Upload
to upload the converted root and tenant certificates.
To add a certificate click the “+” icon.
In the
Scope
tab, select the target computers.
Click
Save
.
Mobile Device Apps Setup
Configure a Mobile Device Apps definition to assign the Netkope Client application to specific user(s) or device(s).
Go to
Devices
>
Content Management
>
Mobile Device Apps
.
Click
New
to create a new app.
Choose one of the following
App Type
options:
App store app or apps purchased in volume.
In-house app
This document goes with the option “App store app or apps purchased in volume”.
Click
Next
.
In the
Search
or
Upload
section, search for Netskope Client app and select the app store country origin.
Do not select Per-App VPN for the Netskope Client app.
Click
Next
.
In the
Add App
section, click
Add
to select Netskope Client app.
It navigates to the
New Mobile Device App
screen.
Under the
General
tab, enter the
Display Name
.
Select
iOS
as the category to add the app to.
Click the
Scope
tab in Mobile Device Apps.
Click
Targets
, then select the specific user(s) or device(s) to assign the configuration profile.
Click
Save
.
The Mobile Device App screen displays the newly added app.
If Per App VPN configuration was selected, other mobile Apps should be associated with respective Per App VPN Profile.
Go to
Devices
>
Content Management
>
Mobile Device Apps
.
Select the required App and click
Edit
.
Go to
Per-App Networking
and select the required VPN profile in Per App VPN dropdown.
Click
Save
.
In this Topic
Deploy Client on iOS Using Jamf Pro

---
## Deploy Netskope Client on MacOS Using Jamf School
**URL:** https://docs.netskope.com/en/deploy-client-on-macos-using-jamf-school/
**Last Modified:** 2025-12-08T17:53:40+00:00
**Scraped:** 2026-06-26T09:12:21.437163+00:00

Deploy Netskope Client on MacOS Using Jamf School - Netskope Knowledge Portal
Deploy Netskope Client on MacOS Using Jamf School
This section describes the steps to deploy the Netskope Client app in a macOS device using Jamf School.
Prerequisites
Administrators must possess proficient working knowledge of Jamf School.
Administrators must review
Netskope Client Enrollment Methods
to understand the Client User Enrollment methods available for their environment.
Users must be imported into the Netskope tenant – see
Provisioning Users for Netskope Client
Download
Netskope Root and Tenant Certificates
and ensure the certificates are available when needed.
Download the Netskope package for macOS from
Netskope Support
.
See
Deploy Netskope Client via IdP
when using IDP as the method of user enrollment.
Download the latest JAMF scripts (JAMFScripts.zip) from the
Netskope Support
portal. This downloads a file JAMFScript_v22_Nov2024 that contains two files:
jamfuninstall.sh
nsclientconfig.sh – Use this file while adding script.
For a PLIST user enrollment method:
Jamf must have a pre-existing user (email) to device mapping.
Download the
CustomEmailConfig.mobileconfig
file from the
Netskope Support
portal.
In Jamf School, enable the
Scripting
option under
Organization
>
Settings
>
Modules
to allow you to add the required scripts.
Supported Platforms and Enrollment Methods
This article outlines Netskope Client deployment instructions for the following user enrollment methods and support platforms. User enrollment methods not documented here are not supported at this time.
Enrollment Methods
Single User
Multi-user
IDP
Y
Y
PLIST
Y
N
Profile Setup
Jamf Profiles manage the core configuration for Client installation. The following sections provide a detailed overview of how to configure these profiles effectively.
Create Profile
Creating profiles is useful as it can help define and configure the system settings such as VPN, Restrictions, and so on for your device. Always create a profile before you start configuring the profile settings. For more information, view
Profiles
.
You can either create a new profile or add the following to an existing profile. To create a new configuration profile:
Log into
JAMF School
.
Go to
Profiles
.
Click
+Create Profile
.
In
Platform
, select the following:
Select the
Platform
as
macOS
Select the
Enrollment Type.
Click
Next
.
In
Details
, perform the following:
Enter the profile name.
Enter the description for the profile.
Click
Next
.
In
Time Filter
, select the checkbox to configure the time at which you want to apply the profile to the devices.
Click
Finish
.
After creating the profile, it navigates to the page where you can set up the profile details such as
Certificates
,
System Extensions
, and so on. Refer to the following sections to learn more about adding different attributes in your profile.
Pre-Approve Network Extension
The Netskope Client on macOS installs a network extension that requires administrator approval to function. The following configuration pre-approves the network extension and suppresses end-user notifications requesting approval.
To configure system extensions in Jamf School:
In the Jamf School console, go to Profiles.
Select and open the required
Profile
.
Click
Scope
.
Click + to add the desired group.
Click Save.
Click
System Extensions
.
Click Configure and perform the following:
Select the checkbox to enable
Allow users to approve system extensions.
Select
Type
as
Allowed System Extensions.
Enter
24W52P9M7W
in
Team Identifier.
Click
+Add
and enter
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
in
Allowed System Extensions
.
Click
Save
.
Pre-Approve Full Disk Access Permission For macOS 14 (Sonoma) and Later
The Netskope Client on macOS requires Full Disk Access permissions for various foundational functionalities. The following configuration pre-approves these permissions and suppresses end-user notifications requesting approval.
To configure full disk access permission in Jamf School:
In the Jamf School console, go to
Profiles
.
Select and open the required Profile.
Click
Scope
.
Click
+
to add the desired group.
Click
Save
.
Click
Security & Privacy
.
Click
Configure
and perform the following:
Click the
Privacy
tab.
Scroll to
System Policy All Files
.
Click
Add new
.
Click
Select Application
.
Enter the following:
Enter the Name.
Enter
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
in
Identifier
.
Select
Bundle ID
for
Identifier Type
.
Enter the following anchor apple generic and identifier in
Code Requirement
.
"com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
Click
Save
.
Pre-Approve VPN Popup for App Proxy
The Netskope Client on macOS installs a network extension that triggers updates to the device’s Network settings. The following configuration pre-approves these updates and suppresses end-user notifications requesting approval.
To configure:
In the Jamf School console, go to
Profiles
.
Select and open the required Profile.
Click
Scope
.
Click
+
to add the desired group.
Click
Save
.
Click
VPN
.
Click
Configure
and perform the following:
Enter any name in
Connection Name
.
Select
Custom SSL
in
Connection Type
.
Enter
com.netskope.client.Netskope-Client
in
Identifier
.
In
Designated Requirement
, enter the following:
anchor apple generic and identifier”com.netskope.client.Netskope-Client” and (certificateleaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificateleaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificateleaf[subject.OU] = “24W52P9M7W”)
Select
App-Proxy
in
Provider Type
.
Enter the Netskope Gateway URL for the tenant in Server:
gateway-<tenant_hostname>.goskope.com
Click
Save
.
Restrict App Proxy Removal
Netskope recommends adding optional deployment parameter Restrict App Proxy Removal to manage user permissions regarding System Extensions in macOS 15 (Sequoia) and above. These controls prevent the removal of the specified system extension by the user.
To restrict app proxy removal:
In the Jamf School console, go to
Profiles
.
Select and open the required Profile.
Click
Scope
.
Click
+
to add the desired group.
Click
Save
.
Click
Restrictions
.
Click
Configure
and perform the following:
Under
Preferences
, select
Restrict items in System Preferences
.
Select items (Network in this case)
Click
Save
.
Push Netskope Root and Tenant Certificates Through Jamf School
Provide additional trust to end users by pushing Netskope certificates during Client installation. Before pushing the root and tenant certificates, ensure that you do the following:
Download root and tenant certificates from Netskope MDM distribution page.
Login to Netskope tenant admin console with admin credentials.
Go to
Settings
>
Security Cloud Platform
>
MDM Distribution
. The certificate download options are displayed in the Certificate Setup section.
Convert the downloaded certificates to
.cer
format by renaming the
.pem
files to
.cer
.
Perform the following steps to add certificates to Jamf School:
In the Jamf School console, go to
Profiles
.
Select and open the required Profile.
Click
Scope
.
Click
+
to add the desired group.
Click
Save
.
Click
Certificates
.
In
Select your file
, click
Choose
File
and upload the root certificate.
Click
Upload Certificate
.
Repeat the same steps to upload the Netskope Intermediate certificate.
Click
Save
.
Create Custom Profile for PLIST
Use this section only if you are deploying using PLIST.
Go to
Profiles
.
Click
+Create Profile
.
Click
Upload Custom Profile
.
Upload the .mobileconfig file (check
prerequisites
to download the file) in Profile file.
The webUI now displays Email Configuration in Settings in this profile.
Click
Next
.
Enter
Profile Name
and
Description
.
Click
Next
.
Enable
Use time filter
and select the time and day according to the requirement.
Click
Finish
.
Click the created profile and map the respected device group.
Configure Script and Installation Parameters
In this section, add scripts in Jamf School that later helps in user enrollment based on the chosen enrollment method. Use the following enrollment methods of your choice and proceed with the deployment. For more information, view
Scripts
.
Copy and paste the shell script from the file
nsclientconfig.sh
downloaded from the Netskope Support Portal. For more information, view
Prerequisites
.
User Enrollment Method
Configuration Parameter
IDP Single-User mode
To add a new script using IDP Single-User mode:
Go to
Scripts
>
+Create New Script
.
Perform the following:
Enter the
Name
for the script.
Select
bash
in
Type
.
Select
Just once
in
when to run
.
Copy paste the above script in the content section and modify as follows on line #62:
Remove leading “#”
Replace Domain name=
. For example, goskope.com.
Tenant name=
. For example, if your tenant URL is example.goskope.com, then enter only example.
Email address request option. Replace
with 0, if you do not want to request user's email address. Enter 1 to request user's email address.
Add ​​enrollencryptiontoken if needed. For example, enrollencryptiontoken=51696332b0116a7f446077xxxxxxxxxx.
Get your Encryption token from Settings > Security Cloud Platform > MDM Distribution > Secure Enrollment.
Click
+
to add the desired device group.
Click
Save
.
IDP Multi-User mode
To add a new script using IDP Multi-User mode:
Go to
Scripts
>
+Create New Script
.
Perform the following:
Enter the
Name
for the script.
Select
bash
in
Type
.
Select
Just once
in
when to run
.
Copy paste the above script in the content section and modify as follows on line #62:
Remove leading “#”
Replace Domain name=
. For example, goskope.com.
Tenant name=
. For example, if your tenant URL is example.goskope.com, then enter only example.
Email address request option. Replace
with 0, if you do not want to request user's email address. Enter 1 to request user's email address.
Enter peruserconfig to specify multi-user IDP deployment mode.
Add ​​enrollencryptiontoken if needed. For example, enrollencryptiontoken=51696332b0116a7f446077xxxxxxxxxx.
Get your Encryption token from Settings > Security Cloud Platform > MDM Distribution > Secure Enrollment.
Click
+
to add the desired device group.
Click
Save
.
PLIST
To add a new script using PLIST:
Go to
Scripts
>
+Create New Script
.
Perform the following:
Enter the
Name
for the script.
Select
bash
in
Type
.
Select
Just once
in
when to run
.
Copy paste the above script in the content section and modify as follows on line #68:
Replace
with addon-
. For example, if administrators access Netskope admin console through acme.goskope.com then addon URL is addon-acme.goskope.com.
Replace
with the Organization ID available in the MDM Distribution webUI in your tenant.
Leave the following as this is a static value:
com.netskope.client.Netskope-Client.plist
.
Leave the following as this is a static value: preference_email
If Secure Enrollment is enabled, append the authentication and encryption enrollment parameters and tokens:
enrollencryptiontoken=<encryption token>
enrollauthtoken=<authentication token>
Get your Authentication token and Encryption token from Settings > Security Cloud Platform > MDM Distribution > Secure Enrollment.
Click
+
to add the desired device group.
Click
Save
.
Create an App
You can use the In-House macOS Package option to upload the macOS package to Jamf School.
To create an app:
Go to
Apps
>
Inventory
.
Click
+ Add App
.
Select
Add In-House macOS Package
.
In
Add In-House macOS package,
click to select the Netskope macOS .pkg file downloaded from Netskope Support.
Click
Close
.
The Apps section displays the uploaded application details.
Click the edit icon to add the respective device groups to this application.
Create Device Group
Use Device Groups to classify your devices according to their attributes. For more information, view
Device Groups
.
To create a device group:
Log in to
JAMF School
.
Go to
Devices
>
Device Groups
.
In the
Groups
page, click
+Add Group
.
In
Add device
group, perform the following:
Enter the name for the device group.
Enter the description for the device group.
Select
Static Group
or
Smart Group
.
This document proceeds with the Static Group option.
In
Options
, configure the desired requirements.
Click
Next
.
In
Profiles
, select the profile that you want to add to the smart group for automatic or on-demand installation. Click Automatic/On-Demand tabs to select.
Click
Next
.
In
Apps
, select the devices on which you want to install applications automatically or on-demand. Click Automatic/On-Demand tabs to select.
Click
Next
.
In
Documents
, select the documents from the list for automatic or on-demand installation.
Click
Next
.
In
Members
, select the devices that you want to add to this device group.
Click
Finish
.
The Groups page displays the created device group details.
Verifying Client Installation
Check the installation logs on the user’s machine in the /var/log/install.log folder. If the user configuration download script fails and the Netskope client installer is executed, the installer will exit and display the “Configuration file missing, aborting installation! error” message.
Check Netskope Client Installation Status
To verify the status of each device, go to
Computer
>
Policies
and click on the policy you created.
Click the
Logs
button at the bottom to view the log files for each device and then click the
Show
button.
Confirming the Netskope Client Extension Approval
To confirm that the Netskope Client extension has been approved and the client is running, run the following command in your macOS terminal window:
systemextensionsctl list
The output should look like this:
% systemextensionsctl list  
1 extension(s)
--- com.apple.system_extension.network_extension
enabled active teamID bundleID (version) name [state]
* * 24W52P9M7W com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy (85.2.0.269/1) 
NetskopeClientMacAppProxy [activated enabled]
Additionally, inspect the system preferences and Network UI to confirm that Netskope Client extension is active.
Uninstalling Netskope Client
See
Uninstalling the Netskope Client
for instructions on uninstalling the Netskope Client.
In this Topic
Deploy Netskope Client on MacOS Using Jamf School

---
## Netskope Client Deployment Options
**URL:** https://docs.netskope.com/en/netskope-client-deployment-options/
**Last Modified:** 2026-05-13T05:23:58+00:00
**Scraped:** 2026-06-26T09:12:30.790056+00:00

Netskope Client Deployment Options
This document describes the deployment workflow and various deployment options available for the administrators to deploy Netskope Client.
Supported Deployment Options
Refer to the following table to understand the different deployment options available for each platform:
Deployment Option
Windows
macOS
Linux
Android/ChromeOS
iOS
MDM
✓
✓
×
✓
✓
Email Invite
✓
✓
✓
✓
✓
Google Playstore
×
×
×
✓
×
AppStore
×
×
×
×
✓
Supported MDM For Each Platform
Refer to the following table to understand the different MDM options available for each platform:
Operating System
Deployment Options
Windows
Email Invite
,
Microsoft Endpoint Configuration Manager
,
Omnissa Workspace ONE
,
Microsoft Group Policy Object (GPO)
,
Microsoft Intune
macOS
Email Invite
,
Jamf Pro
,
Jamf School
,
Omnissa Workspace ONE
,
Microsoft Intune
,
Kandji
Linux
Email
iOS
Email Invite
,
Microsoft Intune
,
Omnissa Workspace ONE
,
XenMobile
,
MobileIron Core
,
Ivanti Neurons
,
Jamf Pro
,
Jamf School
,
IBM MaaS360
,
Kandji
Android
Email Invite
,
Microsoft Intune
,
Omnissa Workspace ONE
,
MobileIron Core
,
Ivanti Neurons
,
IBM MaaS360
,
Google Workspace
Chrome OS
Email Invite
,
Google Workspace
VDI
Azure Virtual Desktop
,
Amazon WorkSpaces
,
Citrix DaaS Integration with Azure Virtual Desktop
,
Citrix Virtual Apps and Desktop,
Omnissa Horizon
Deploying to Always On, Always Connected (AOAC) devices
.
Netskope Client disconnects tunnel when the AOAC device display is off and resumes connection when the AOAC device display switches on.
Supported OS: Windows 10, 11
By default, this feature is set to enable/true. Contact Netskope Support for more details.
– If enabled (set to
true
) then the Netskope Client will not disconnect the tunnel when the AOAC device display is switched off.
– If disabled (set to
false
) then Netskope Client will disconnect the tunnel when the AOAC device display is switched off and reconnect when the display is switched on.
Netskope Client Deployment Parameters
Netskope Client Enrollment
Enforce Enrollment for Netskope Client
Netskope Client for macOS
Netskope Client For Windows
Netskope Client For Linux
Netskope Client For Android and ChromeOS
Netskope Client for iOS
Troubleshooting Guide for iOS Netskope Client App
Netskope Client for Virtual Desktop Infrastructure (VDI)
Explicit Proxy Over Client (EPoC)
External Browser-based Authentication
Netskope Client Integration With Imprivata
Chrome Extension Support For User Notifications
Microsoft Endpoint Configuration Manager
Omnissa Workspace ONE
Microsoft Group Policy Object (GPO)
Microsoft Intune
Google Workspace
Jamf Pro
Jamf School
ManageEngine Endpoint Central
Kandji
IBM MaaS360
XenMobile
MobileIron Core
Ivanti Neurons(MobileIron Cloud)
Deploy Netskope Client In Restricted Regions
Citrix Virtual Apps and Desktop
Deploy Netskope Client On Citrix DaaS With Azure Virtual Desktop
Azure Virtual Desktop
Amazon WorkSpaces
Omnissa Horizon
In this Topic
Netskope Client Deployment Options

---
## Netskope Client Hardening
**URL:** https://docs.netskope.com/en/netskope-client-hardening/
**Last Modified:** 2026-02-06T13:39:09+00:00
**Scraped:** 2026-06-26T09:12:31.906769+00:00

Netskope Client Hardening - Netskope Knowledge Portal
Netskope Client Hardening
Netskope Client provides various hardening options to ensure its smooth operation. This document provides insights into the hardening features of the Netskope Client installed on Windows and macOS devices. To learn the supported versions, view
Supported OS and Platforms
.
By using the Client hardening options, you can prevent users with elevated permissions from altering Client files and services and ensure that the full functionality of security features Netskope offers is available to you.
The Netskope Client installs on end user devices as a non-intrusive application that facilitates a seamless user experience and steers configured end user traffic to Netskope Cloud. By design, the Netskope Client establishes a tunnel to Netskope Cloud by choosing the nearest POP (data center). This ensures the following:
Configured traffic from the Client is steered via an optimal path to connect to Netskope POP.
The complete benefits of Netskope security services are available to the customers.
Depending on an organization’s IT policy, end users may or may not have administrative rights on their respective system. An end user with administrative privileges has access and controls to alter the default configuration of the Client and its services installed on their devices. This can affect the normal functioning of the Netskope Client and may be detrimental to the organizations’ security policies.
Netskope Client Hardening Options
You can use the following hardening options to ensure the Netskope Client operates smoothly on end user devices running Windows and macOS:
Tamperproofing
Configuration Encryption
Protect Client configuration and resources
Tamperproofing Netskope Client
The Client configuration includes the following tamperproof options.
Disable or enable Client.
Password protection to prevent unauthorized uninstallation of the Client.
Block all traffic if the Client tunnel is not established.
To learn more, view
Tamperproof
.
Client Configuration Encryption
The Client configuration files generated in the admin configuration and downloaded by the client can be encrypted. To learn more, view
Client Configuration
.
Protect Client Configuration And Resources
When you enable this option, it prevents users with elevated permissions from altering any sub-part (files, folders, and process) of the Netskope Client installation. It prevents users from modifying, renaming, or deleting Netskope processes, folders, files, and registry keys. To learn more, view
Protect Client Configuration and resources
.
In this Topic
Netskope Client Hardening

---
## Netskope Client Overview
**URL:** https://docs.netskope.com/en/netskope-client-overview/
**Last Modified:** 2026-05-14T18:32:50+00:00
**Scraped:** 2026-06-26T09:12:33.018717+00:00

Netskope Client Overview
The Netskope Client is a lightweight application designed to direct traffic from end-user devices to the Netskope Cloud Next Generation Secure Web Gateway (SWG), Zero Trust Network Access (ZTNA), and Firewall as a Service (FWaaS) components. The Netskope Client also offers services such as
Endpoint Data Loss Prevention
(EDLP) and
Endpoint Software-Defined Wide Area Network
(SD-WAN) capabilities. Additionally, it provides real-time visibility of managed devices accessing cloud and web resources from any location, thereby supplying data to Netskope
Digital Experience Management
(DEM). The sections on Endpoint DLP, Endpoint SD-WAN, and DEM contain further details on these features.
The Netskope Client maintains secure access for endpoints, regardless of location. This is achieved by intercepting web and application traffic as defined by a
Steering Configuration
, and forwarding it through a secure tunnel to the Netskope Cloud. The Netskope Client’s configuration is updated at regular intervals to ensure optimal functionality.
Supported Platforms
Refer to
Netskope Client Supported OS and Platform
for more details on the supported versions of each operating system (OS).
Netskope Client Advantages
The following are the advantages of using Netskope Client in your environment:
Provide visibility to all users on and off premises.
Provide visibility to all managed and unmanaged applications.
Inspect browser and native application traffic.
Use a single agent to seamlessly and uniformly enforce policy decisions on endpoints across an organization.
How it Works
The Netskope Client requires outbound connectivity to Netskope’s datacenters for downloading required configuration files and establishing its secure tunnel.
To learn more, view
Netskope Client Network Configuration
.
Netskope Client Deployment
The Netskope Client installer is available for download in the
Netskope Support
portal.
Release Number
– Netskope Client uses 4-place version number system. The individual digits represent
release
.
major
.
minor
.
build_number
respectively. For example: 137.0.1.2638.
Client Golden Release
– Golden release versions are available every 3-releases and support backward compatibility up to two previous versions. To learn more about Golden release versions and and download Client installers, see this
Netskope Client Downloads
article.
Netskope supports multiple options to deploy Netskope Client on your device. Refer to
Netskope Client Deployment Options
to various deployment options available for the administrators to deploy Netskope Client.
Netskope Client Services
Netskope Client steers traffic to Netskope’s security solutions such as Netskope Private Access, Netskope Cloud Firewall, SWG, and so on.
Netskope Client for Netskope Private Access
The Netskope Client ensures secure access for end-users to private applications hosted in  data centers, private clouds, or public clouds. Utilizing a Zero Trust architecture, it enforces least-privileged access. This means users are strictly limited to the specific applications they are authorized to use, significantly enhancing security by preventing exposure to the wider network.
Netskope Client for Netskope Cloud Firewall
The Netskope Client steers outbound user traffic—including web and application connectivity across all ports and protocols—to the Netskope Cloud. This allows for application inspection and policy enforcement. For roaming users and distributed offices, Netskope Cloud Firewall ensures centralized management, visibility, and consistent policy application. To learn more, view
Netskope Client in Cloud Firewall
.
Steering Configuration
A Steering Configuration defines which traffic (based on ports, protocols, domains, and applications) the Netskope Client intercepts and directs to the Netskope Cloud. Netskope administrators manage and maintain these configurations. They are assigned to end-users based on their group or Organizational Unit (OU), enabling precise and granular steering across the organization.
Click
here
to read more about Steering Configuration.
In this Topic
Netskope Client Overview

---
## Provisioning Users for Netskope Client
**URL:** https://docs.netskope.com/en/provisioning-users-for-netskope-client/
**Last Modified:** 2025-08-31T01:48:05+00:00
**Scraped:** 2026-06-26T09:12:35.293613+00:00

Provisioning Users for Netskope Client
A fundamental step in deploying Netskope Client within your environment involves importing your users into the Netskope tenant. Netskope Cloud Platform leverages its own directory to apply security policies across all deployment modes and operating systems. For this reason, it is mandatory to populate users and groups as described in this article.
The following are the supported methods for importing users and groups into your Netskope tenant:
Manual Import
Using SCIM App
Using Directory Importer
To learn more, view
User Import Methods and User Attributes
.
– Email ID and UPN are mandatory fields during user import.
– An email is required for all users during user import as it represents the user’s identity across the Netskope Secure Cloud Platform.
– In addition, a user UPN is mandatory for SCIM and Directory Importer integrations and may be required for user enrollment of the Netskope Client. See
Netskope Client Enrollment Methods
for more details.
In this Topic
Provisioning Users for Netskope Client

---
## SAML Client Profile
**URL:** https://docs.netskope.com/en/saml-client-profile/
**Last Modified:** 2026-05-14T17:36:44+00:00
**Scraped:** 2026-06-26T09:12:39.754048+00:00

SAML Client Profile
The Client SSO integration allows organizations to enforce steering cloud application traffic to Netskope Cloud for very precise and granular analysis. In scenarios where the Netskope Client is not present or disabled on the end user’s device, the user is redirected from the Single Sign On (SSO) portal to a location from where the user can download the Netskope Client or request for the Client.
Create Enterprise Application
To create an enterprise application:
Log into
Microsoft Azure
.
Go to
Microsoft Entra ID
>
Manage
>
Enterprise Applications
.
Click
+New Application
.
Click
Create your own application
.
In
Create your own application
, perform the following:
Add Netskpe Client in
What’s the name of your app?
Continue with the default option
Integrate any other application you don’t find in the gallery (Non-gallery)
in
What are you looking to do with your application?
Click
Create
.
Setup Single Sign On
After you complete creating your application, proceed to set up a single sign on. In the Overview page, click
Set up single sign on
under
Getting Started
.
To set up single sign on:
Click
Set up Single Sign On
>
SAML
.
In
Set up Single Sign-On with SAML
, click the edit icon for
Basic SAML Configuration
.
In the
Basic SAML Configuration
window, enter the following:
Identifier(Entity ID)
Reply URL(Assertion Consumer Service URL)
Click
Save
.
Under
SAML Certificates
, download the certificates in the Base64 format.
Assign the Enterprise Application
Assign the enterprise application to the desired users and groups using the following instructions:
Go to
Manage
>
Users and groups
.
Click
+User/group
.
Assign users and groups to the application.
Click
Assign
.
Netskope SAML Account Configuration
To configure account in the Netskope tenant, perform the following:
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
SAML
.
Click
New Account
.
In the
New Account
window, enter the following details:
Name:
Enter a name for the app.
Application:
Microsoft Accounts.
ACS URL:
The Microsoft Entra Identifier. Paster the identifier from the Entra admin center.
IdP SSO URL:
Paste the Login URL copied from the Entra admin center.
IdP Certificate:
Paste the contents of the SAML Signing Certificate downloaded from the Entra admin center.
Click
Save and View Netskope Settings
.
After you review the Netskope Settings, copy and paste the SAML Proxy IdP URL and SAML proxy ACS URL in the Identifier and Reply URL fields respectively in the Basic SAML Configuration.
View Netskope Client
After completing the entire configuration, the user can now see Netskope Client added in their SSO.
In this Topic
SAML Client Profile

---
## Uninstalling the Netskope Client
**URL:** https://docs.netskope.com/en/uninstalling-the-netskope-client/
**Last Modified:** 2026-06-09T04:02:18+00:00
**Scraped:** 2026-06-26T09:12:43.151910+00:00

Uninstalling the Netskope Client - Netskope Knowledge Portal
Uninstalling the Netskope Client
This section describes various options to uninstall Netskope Client from the end-user devices.
Client uninstallation does not automatically remove tenant certificates. For more related details, reach out to Netskope support.
Windows
Option 1
Option 2
Use the Add or Remove Programs option in the Windows control panel to uninstall the Client.
Microsoft Endpoint Configuration Manager
@echo off
REM ---------------------------------------------------------------
REM Improved Uninstall Netskope Client (Password Protected)
REM Uses PowerShell to read registry and extract MSI GUID
REM ---------------------------------------------------------------
setlocal
set "LOGFILE=%PUBLIC%\nscuninstall.log"
set "PASSWORD=<password>"
echo Searching for Netskope Client...
powershell -NoLogo -NoProfile -Command ^
    "$apps = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*,HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Where-Object { $_.DisplayName -eq 'Netskope Client' };" ^
    "if (-not $apps) { Write-Host 'Netskope Client not found.'; exit 1 };" ^
    "$success = $false;" ^
    "foreach ($app in $apps) {" ^
    "    Write-Host 'Found:' $($app.DisplayName);" ^
    "    if ($app.UninstallString -and $app.UninstallString -match '\{[A-F0-9\-]+\}') {" ^
    "        $guid = $matches[0];" ^
    "        Write-Host \"Uninstalling $($app.DisplayName) with GUID: $guid\";" ^
    "        try {" ^
    "            Start-Process msiexec.exe -ArgumentList \"/x $guid PASSWORD=`\"%PASSWORD%`\" /qn /l*v `\"%LOGFILE%`\"\" -Wait -PassThru | Out-Null;" ^
    "            Write-Host 'Uninstall completed for:' $($app.DisplayName);" ^
    "            $success = $true;" ^
    "        } catch {" ^
    "            Write-Error \"Failed to uninstall $($app.DisplayName): $_\";" ^
    "            exit 2;" ^
    "        }" ^
    "    } else {" ^
    "        Write-Host 'No MSI GUID found for:' $($app.DisplayName);" ^
    "    }" ^
    "};" ^
    "if (-not $success) { exit 2 } else { exit 0 }"
set "ec=%ERRORLEVEL%"
if %ec%==0 (
    echo Uninstallation completed successfully.
) else if %ec%==1 (
    echo Netskope Client not found.
) else (
    echo Uninstallation failed. Check the log file: %LOGFILE%.
)
endlocal
exit /b
– You can also save this script as a .bat file and execute it locally from Windows Command Prompt.
– This script works only in Admin mode.
Microsoft Group Policy Object(GPO)
Uninstalling can be done through GPO using a batch script similar to installation. Use the following uninstallation script (works only in admin mode):
Get-WmiObject Win32_Product | Where-Object Name -eq "Netskope Client" | % { $_.Uninstall() }
To uninstall NS Client with Password Protection using GPO Batch Script use the following uninstallation script:
@echo off
SetLocal
    set newver=117.0.0.2087
    set newVernum=%newver:.=%
for /f "tokens=2 delims==" %%f in ('wmic product where "Name like 'Netskope Client'"
get Version /value ^| find "="') do set "instVer=%%f"
IF NOT DEFINED instVer (
    msiexec /x "<path_to_file>/STAgent.msi" PASSWORD=<uninstall_password_set_in_tenant>! /q 
) ELSE (
    set instVerNum=%instVer:.=%
    IF instVerNum LSS newVernum (
        msiexec /x "<path_to_file>/STAgent.msi" PASSWORD=<uninstall_password_set_in_tenant>! /q
    )
)
EndLocal
macOS
The following options list the steps to uninstall Netskope Client in your macOS device:
Option 1
Option 2
Option 3
This option describes how to manually run the Remove Netskope Client application from the device’s Applications folder to begin the uninstall process.
Go to
Applications
and click the
Remove Netskope Client
icon.
Enter your credentials to proceed with the uninstallation of the client.
When uninstalling Netskope Client on devices running Big Sur (macOS 11), users are prompted to enter their credentials twice to uninstall the Network extension app proxy and to remove the Netskope client.
This option includes a script to launch the Remove Netskope Client application and begin the uninstall process.
Create a shell script (for example,
uninstall.sh
) using the following command and execute it on the user’s device to uninstall the Client.
#!bin/bash
/Applications/Remove\ Netskope\ Client.app/Contents/MacOS/Remove\ Netskope\ Client uninstall_me exit
To uninstall using a password, use the following command:
#!/usr/bin/env bash
UNINSTALL_PASSWORD='password'
/Applications/Remove\ Netskope\ Client.app/Contents/MacOS/Remove\ Netskope\ Client uninstall_me $UNINSTALL_PASSWORD
Ensure to add a blank space before
Netskope
and
Client
in this script.
The following section provides the instructions to uninstall the Netskope Client using various MDMs.
Netskope provides an uninstallation script as a part of
JAMFScripts.zip
that can be used across MDMs.
JAMFScripts.zip
is available for download from the Scripts section in
Netskope Support
portal. Extract JAMFScripts.zip to find the uninstallation script “jamfuninstall.sh”. This downloads JAMFScript_v22_Nov2024 that contains two files:
jamfuninstall.sh – Use this file for uninstallation.
nsclientconfig.sh
When using this script for uninstalling, enter your password as the fourth parameter in the script  in the JAMF policy using the set command below:
set -- 0 0 0 <yourUninstallPassword>
– Auto-removal of extensions is currently supported only from release 95.1.2 onwards and not for versions prior to 95.1.2. However, when creating profiles in JAMF, selecting the
Removable System Extension
option under the
System Extension Type
option will prevent user approval requests during manual Client un-installation. This is applicable for macOS Monterey (version 12) and later.
– Setting the System Extension to Removable results in the extension unloading and the Netskope client disables as a result.  To ensure proper execution, you must configure your MDM to make the System Extension Removable and then run the uninstall script.
– It is recommended that you create a separate configuration profile and script for the uninstallation for specific machines or users as required. Changing the existing configuration profile for the system extension will result in clients disabling and users receiving  requests for manual approval.
Jamf
This section describes the steps to uninstall Netskope Client in macOS devices using Jamf.
Configuration Profile and Policy
Perform the following instructions to mark the system extension as removable:
In JAMF, go to
Computers > Configuration Profiles > New.
Provide a
Name
for the Configuration Profile.
Select
System Extensions > Configure.
Select
Allow users to approve system extensions
.
Under Allowed Team IDs and System Extensions, select
System Extension Types
as Removable System Extensions.
Add Network Extension Team ID:
24W52P9M7W
Click
Add
to include the following System Extension:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Click
Save
under Removable System Extensions.
Click
Save
in the bottom right to save the Configuration Profile.
Once the Configuration Profile is configured, you must upload and configure the uninstall script in a Policy.  Refer to
Scripts
for instructions to add a script. After you upload the script:
Go to
Computers > Policies > New.
Give the Policy a name.
Select
Login
for the trigger and the frequency as
Once per computer
.  You can optionally configure a different trigger if you’d like the script to run sooner or at a different interval.
Click
Scripts > Configure
.
Click
Add
on the uninstall script you uploaded.
Click
Save
.
You can now assign the Configuration Profile and Policy to users and computers in JAMF.  It is recommended to use a Smart Group or ensure you remove users and computers from the Configuration Profile and Policy that are configured to install the client.
Intune
This section describes the steps to uninstall Netskope Client in macOS devices using Intune.
Create Configuration Profile
Perform the following instructions to mark the system extension as removable:
In Intune, go to
Devices
>
macOS
>
Configuration Profiles
>
Create
>
New Policy
.
Select
macOS
under
Platform
and
Settings catalog
under
Profile Type
.
Click
Create
.
Under
Basics
, provide a name for the profile.
Click
Next
.
Under Configuration Settings, click
+Add settings
.
In the Settings Picker window, select
System Configuration
>
System Extensions
.
Select the checkbox for
Removable System Extension
s.
Go to
Configuration Settings
on the left-pane and click
+Edit Instance
.
Enter the following:
Removable System Extensions name
: com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Team Identifier:
24W52P9M7W
Click
Save
.
Click
Next
to continue.
Provide
Scope tags
(optional).
Click
Next
to continue.
In
Assignment
, Add user or device assignments to uninstall the Netskope client.
Click
Next
to continue.
In
Review+Create
, you can review the policy configurations.
Click
Create
.
Run Uninstall Script
Once the Removable System Extension policy is configured, you must upload and configure the uninstall script. Refer to
Shell Scripts
for instructions to add a script. Intune does not support passing parameters to the script and hence you must add a set command to the script.
Perform the following instructions to run the uninstall script:
In Intune, go to
Devices
>
macOS
>
Shell scripts
.
Click
+Add
.
In
Basics
, enter a Name and Description.
Click
Next
.
In Script Settings, select to upload the uninstall script  from your local storage in your computer. Make the following changes:
Run script as signed-in user – No
Hide script notifications on devices – Not configured
Script frequency – Not configured
Max number of times to retry if script fails – Not configured
Selecting
Not Configured
for all other parameters implies that the script runs only once.
Include
set -- 0 0 0 <yourUninstallPassword>
in the script to unsintall using password parameter.
Click
Next
.
Assign proper groups based on user or Devices by clicking Add groups and checking the box next to the appropriate groups.
Click
Select
.
Click
Next
to continue.
Click
Add
.
Kandji
Kandji does not support marking system extensions as removable. The steps provided for the Netskope install allow for any extension type from the Netskope team identifier.
Perform the following instructions to run the uninstall script:
In Kandji, go to
Library
.
Click
+Add new
.
Click
Custom Scripts
>
Add & Configure
.
Select the Blueprint you want to uninstall clients.
In
ExecutionFrequency
, select the option:
Run once per device
.
Enter the following script in the Audit Script text box:
#!/bin/bash
#script for installing NSAgent on OSX machines
#will check to see if Netskope is Installed
function Test_NSClient(){
xz=$(/usr/bin/mdfind kMDItemFSName == Netskope Client.app -onlyin /Library/Application\ Support/)
if [ -e "$xz" ]; then
    echo "$xz found netskope client is installed"
exit 1
else
    echo "client does not exist"
exit 0
fi
}
Test_NSClient
#end script
Click
+Add Remediation Script
.
Download “kandji_uninstall.sh” script from the
Support
portal.
Paste the contents of the uninstall script in the Remediation Script field.
Click
Save
.
Omnissa Workspace One
This section describes the steps to uninstall Netskope Client for macOS devices using Omnissa Workspace One.
Add Removable System Extension
Omnissa Workspace One supports Removable System Extensions and smart groups with exclusions. Perform the following instructions to mark the system extension as removable:
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add
.
Click
Add Profile
from the Add dropdown options.
Select
Apple macOS
from the platform list.
Select
Device Profile
in Select Context.
Provide a name for the profile.
Start typing ‘System’ in the search text box of the configuration profile.
Expand System Extensions option and click Add.
Configure Removable System Extensions as follows:
Team Identifier:
24W52P9M7W
Bundle Identifier:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Click
Next
.
Assign the profile to a Smart Group and necessary exclusions.  This structure will depend on your environment.
Click
SAVE & PUBLISH
.
Run Uninstall Script
Once the Removable System Extension policy is configured, you must upload and configure the uninstall script.  Follow the steps below to use the
Scripts
functionality of Omnissa WorkSpace One.  Omnissa WorkSpace One also supports
Files/Actions
which allows for more granular scheduling based on specific triggers such as Logon or recurring checking.
Go to
Resources
>
Scripts
.
Click
ADD
>
macOS
.
In
General
, provide a
Name
for the uninstall script.
Click
NEXT
.
Click
UPLOAD
and select the file you have configured with the uninstall password.
Click
NEXT
.
Click
SAVE
.
Select the script that you previously uploaded and click
ASSIGN
.
Click
NEW ASSIGNMENT
.
Enter a name for the Assignment.
Select a SmartGroup for uninstall based on the devices or users that need the client uninstalled.
Click
NEXT
.
Select the deployment trigger.  You can select
Run Once Immediately
if you want the script to push immediately.
Click
ADD
.
Linux
Use the command
sudo /opt/netskope/stagent/uninstall.sh
to uninstall Netskope Client in Linux.
In this Topic
Uninstalling the Netskope Client

---
## Install and Test the Client
**URL:** https://docs.netskope.com/en/install-and-test-the-client/
**Last Modified:** 2025-08-31T01:55:37+00:00
**Scraped:** 2026-06-26T09:14:33.291323+00:00

Install and Test the Client
With SAML configured in Google and Netskope, now install the Client on your devices.
If you have access to the Netskope support portal, download the Netskope Client from here:
https://support.netskope.com/s/article/Download-Netskope-Client-and-Scripts
If you do not have access to the Netskope support portal, reference the download locations here:
For Windows: https://download-<
tenant-URL
>/dlr/win/get
For Mac: https://download-<
tenant-URL
>/dlr/mac/get
Double-click the Netskope Client and install the software.
The Client will open an enrollment window. Enter your tenant name.
Log in with your Google username and password.
If you see the following error, make sure the user exists in the Netskope tenant under
Settings > Security Cloud Platform > Netskope Client > Users
.
The following message indicates successful enrollment, and the Client will appear in the system tray or menu bar, and be automatically enabled within 10-15 seconds.
You’ll see the Netskope icon in color when the Client is enabled.
After validation of enrollment and SSO works as expected, proceed with using software deployment tools to push out to the remainder of your pilot group or user base. Assistance can be found on the Support site or via your Netskope Sales Engineer or Technical Customer Success Manager.
In this Topic
Install and Test the Client

---
## Netskope Client IdP Mode with Google SAML Auth
**URL:** https://docs.netskope.com/en/netskope-client-idp-mode-with-google-saml-auth/
**Last Modified:** 2025-08-31T01:55:35+00:00
**Scraped:** 2026-06-26T09:15:14.393435+00:00

Netskope Client IdP Mode with Google SAML Auth - Netskope Knowledge Portal
Netskope Client IdP Mode with Google SAML Auth
This document focuses on the Netskope Client deployed in IdP Mode. These instructions apply to multiple types of tenants (Cloud App, NPA, or Web).
Workflow
The integration is described in these sections:
Get the Netskope SAML Settings
Configure Google IdP for Netskope SAML Forward Proxy
Install and Test the Client
In this Topic
Netskope Client IdP Mode with Google SAML Auth

---
## Client Steering
**URL:** https://docs.netskope.com/en/client-steering/
**Last Modified:** 2026-06-25T17:39:29+00:00
**Scraped:** 2026-06-26T09:17:36.742873+00:00

Client Steering
The Client Steering page provides information about user requests that the Netskope Client directs to the Netskope Cloud. You can get a granular view of the different users, applications being accessed, Netskope Client version used to process user requests, user activities, and other valuable insights.
Client Steering Overview
The Client Steering Overview widgets provide a summary of the users, client versions, and data usage for the last 7 days. You can view the total number of active users, licensed users, client versions in use, and data usage. Changing the date range with the Event Date filter at the top of the page does not affect the timestamp of the following four widgets:
Active User Count
refers to the total number of unique users sending requests to all apps. This widget is RBAC-enabled.
Licensed Users for Your Tenant
are the total number of user seats assigned to your tenant.
Client Versions by Device Count
shows the total number of unique devices using a specific client version and has connected to a Netskope POP at least once in the past 7 days.
Uploaded & Downloaded Bytes
is a bar graph that shows the total number of uploaded bytes and downloaded bytes. When you mouseover each bar, you can see the total number of bytes uploaded or downloaded. This widget is RBAC-enabled.
Tip
To apply your selections from the filter menu, click the update  icon on the top-right corner of the page.
Filtered Widgets
You can view the logged in user count, daily session count, and client versions usage trends on a specific date in a specific Netskope datacenter. The filtered widgets also provide details about the number of unique active devices. You can view the active device count by point of presence (POP) and Operating System (OS) version. If an OS version is not part of Netskope’s database, the OS version is shown as “Unknown”. By default, the widgets show the data for all POPs unless filters are selected in the Netskope POP dropdown menu.
Client Connection Request Count
: The Client Connection Request Count widget displays the number of unique users and connection requests per hour.
Daily Session Count
: The Daily Session Count widget displays the number of sessions seen per day. This widget is RBAC-enabled.
Note
The Daily Session Count widget displays a maximum of 30 days of data by default.
Client Versions Usage Trend
: The Client Versions Usage Trend widget displays the daily aggregation of the number of sessions using each client version utilized in your organization.
Active Device Count by POP
: The Active Device Count by POP widget displays the number of devices seen per POP. This widget is RBAC-enabled.
Active Device Count by OS Version
: The Active Device Count by OS Version widget displays the number of devices seen per OS version.
Active Device Count by POP Per Hour
: The Active Device Count by POP Per Hour widget displays the number of devices seen by POP for each hour in the time range.
Active Device Count by OS Per Hour
: The Active Device Count by OS Per Hour widget displays the number of devices sorted by OS for each hour in the selected time range. This widget is RBAC-enabled.
In this Topic
Client Steering

---
## Netskope Client Enforcement
**URL:** https://docs.netskope.com/en/netskope-client-enforcement/
**Last Modified:** 2025-08-31T01:48:07+00:00
**Scraped:** 2026-06-26T09:18:29.166999+00:00

Netskope Client Enforcement - Netskope Knowledge Portal
Netskope Client Enforcement
The Client SSO integration allows organizations to enforce steering cloud application traffic to Netskope’s cloud for very precise and granular analysis. If the Netskope Client is not present or disabled on the device, the user will be redirected from the SSO portal to the Netskope and the client installation and activation is enforced.
Netskope supports and integrates with the following SSO providers:
Okta: The Netskope-Okta integration allows organizations to enforce steering cloud application traffic to Netskope’s cloud for very precise and granular analysis. If the Netskope Client is not present on the device, the source IP coming to Okta is not going to be a Netskope proxy IP. The user is redirected to the Netskope page (Client checker) for Client installation and activation.
OneLogin: The Netskope-OneLogin integration allows organizations to enforce steering cloud application traffic to Netskope’s cloud for very precise and granular analysis. You can configure the Netskope Client with OneLogin’s application policies. When a user accesses a SaaS app, traffic is redirected through a SAML redirection from OneLogin to the Netskope (Client checker) page. Once the Client is installed and activated, the user can access the SaaS app.
SAML Proxy-based Client enforcement: In this case, Netskope acts as a SAML proxy and integrates with the SAML SPs and SAML .
You can access the Enforcement page by clicking
Settings > Security Cloud Platform > Netskope Client > Enforcement
.
In this Topic
Netskope Client Enforcement

---
## Get Client Data
**URL:** https://docs.netskope.com/en/get-client-data/
**Last Modified:** 2025-08-31T01:39:20+00:00
**Scraped:** 2026-06-26T09:18:46.169243+00:00

Get Client Data - Netskope Knowledge Portal
Get Client Data
This endpoint returns information related to the Netskope Client.
Request Endpoint
https://
<tenant-
URL
>
/api/v1/clients
Valid query parameters are:
Key
Value
Description
token
string
Required. The token obtained from the REST API page in the Netskope UI (
Settings > Tools > Rest API v1
) is required. We recommend that you place the token in the body of the request, not in the endpoint URL.
query
Valid query on the various fields.
This acts as a filter on all the entries in the database.
limit
Positive integer less than 5000
REST API responses can return up to 5000 events in a single response. You can use pagination to retrieve more results.
skip
Positive integer
Skip over some of the events (useful for pagination in combination with limit).
Note
The query fields for this endpoint are slightly different from the others. The way to figure it out is to first get a list of clients, see the data returned, and then figure out the query accordingly.
Example Client Data Request
POST https://
<tenant-
URL
>
/api/v1/clients
{    
    "token": "f32a973eddd7bc1602fc0f48dc0a",
    "query": "host_info"}
Response
Hostname is returned as follows:
{
     "_id": ,
     "client_install_time": 
     "device_id": ,
     "host_info":
     {
        "device_make": ,
        "device_model": ,
        "hostname": ,
        "os": ,
        "os_version":
        "nsdeviceuid":  
     },
      "last_event":
     {
        "actor": ,
        "event": ,
        "status": ,
        "timestamp": 
      },
      "users":
      [
       {
        "_id": ,
        "client_version": ,
        "device_classification_status": ,
        "last_event":
        {
           "actor": ,
           "event": ,
           "status": ,
           "timestamp": 
        },
        "user_added_time":,
        "user_source": ,
        "userkey": ,
        "username": 
       }
      ]
     }
So the query for a particular host should like
host_info.hostname eq 'xxx'
or
host_info.hostname eq 'yyy'
.
The backend returns the status of many fields as numeric values. In the UI they are converted to readable text, but not in the REST API. The mappings are provided below:
"device_classification_status": {
    "managed": 0,
    "unmanaged": 1,
    "unknown": 2
},
"last_event": {
    "status": {
        "Disabled": 0,
        "Enabled": 1,
        "Uninstalled": 2
    },
    "event": {
        "Installed": 0,
        "Tunnel Up": 1,
        "Tunnel Down": 2,
        "Tunnel down due to Secure Forwarder": 3,
        "Tunnel down due to config error": 4,
        "Tunnel down due to error": 5,
        "User Disabled": 6,
        "User Enabled": 7,
        "Admin Disabled": 8,
        "Admin Enabled": 9,
        "Uninstalled": 10,
        "Installation Failure": 11
    },
    "actor":{
        "User": 0,
        "Admin": 1,
        "System": 2
    }
},
"user_source": {
    "Directory": 0,
    "Manual": 1
}
"host_info": {
    os: {
        "Windows": 0,
        "Mac": 1,
        "Android": 3,
        "Windows Server": 4
    }
}
The hierarchy is important, so to query for last events the query should be
last_events.status = 0
to find the Disabled events.
In this Topic
Get Client Data

---
## Netskope Client Enforcement using Okta
**URL:** https://docs.netskope.com/en/netskope-client-enforcement-using-okta-1/
**Last Modified:** 2025-08-31T01:48:08+00:00
**Scraped:** 2026-06-26T09:24:04.850754+00:00

Netskope Client Enforcement using Okta - Netskope Knowledge Portal
Netskope Client Enforcement using Okta
The Netskope with Okta integration allows organizations to enforce steering cloud application traffic to Netskope’s cloud for very precise and granular analysis. If the Netskope client is not present on the device, the source IP coming to IDP is not going to be a Netskope proxy IP. The user is redirected to the Netskope page (Client checker) for client installation and activation.
Installing Netskope client on end user machines using an IdP is one of the automated mechanisms apart from using distribution mechanisms, like SCCM or JAMF.
Prerequisites
Users must be imported in the Netskope UI using one of these methods:
Manually importing using CSV
AD importer
Okta(SCIM)
Create SAML 2.0 APP on IDP
Click play to watch a video.
Configure an Okta App
Go to your Okta Admin Dashboard.
Go to the Applications and click
Create App Integration
.
Select
SAML 2.0
from the list and click
Next
.
Enter an App Name.
Copy SAML Configuration details from your Netskope Tenant. Go to
Security Cloud Platform > Enforcement
and select
Okta
.
Paste the ACS URL in the Audience URI field in the SAML settings, and then click
Next
.
Download the public certificate from your SAML Okta Application and upload it in the Netskope tenant.
Create a Security Zone for Netskope IP Addresses
Go to
Security > Networks
in Okta and click
Add zone
.
Provide the Zone Name and copy all the Netskope IPs and paste into them Gateway IPs section. To get all the Netskope IPs, go to
Security Cloud Platform > Enforcement > Netskope IP Ranges
. After pasting all the IPs, click
Save
.
The Network Zone has been created.
Create an Authentication Policy
Go to
Security > Authentication Policies
and click
Add a policy
.
Click
Add rule
.
Create the Rule by selecting the specific group and zone (e.g. NetskopeZones) created in the last setup section and set the access to
denied
. With this configuration, any user logging into Okta from an endpoint that does not have a Netskope client installed and running will see only this application on the OKTA dashboard. This one available app will help to install the Netskope Client, making the user compliant and enabling them to see all of their permitted applications.
Click
Save
.
Also add the Client Enforcement Application in the Policy.
Validate Client Enforcement
Enable the Client and you will see the lock on the Netskope Client Enforcement Application.
Similarly when you don’t have the client, the application will be in the unlocked stage.
When you click the unlocked application it will redirect you to the download page for the Netskope Client for your tenant.
In this Topic
Netskope Client Enforcement using Okta

---
## Troubleshooting Guide for iOS Netskope Client App
**URL:** https://docs.netskope.com/en/troubleshooting-guide-for-ios-netskope-client-app/
**Last Modified:** 2025-08-31T01:48:14+00:00
**Scraped:** 2026-06-26T09:24:14.983226+00:00

Troubleshooting Guide for iOS Netskope Client App - Netskope Knowledge Portal
Troubleshooting Guide for iOS Netskope Client App
Introduction
This guide is designed to streamline the troubleshooting process with the MDM-based deployments.
Prerequisites
No specific prerequisites to follow the troubleshooting guide.
Troubleshooting Scenarios
This section provides a common scenario that you can troubleshoot  when you set up Netskope Client for iOS devices using MDM.
Scenario: Client Enrollment Fails After MDM Pushes the Client Configuration
Problem 1:
The enrollment process starts after you add the Netskope Client app from the public store in the MDM. In the MDM, you can configure the required configurations to enroll Client to the respective user endpoints.
The enrollment failure denotes either one of the following:
The
Netskope Client
failed to receive the required details.
The Netskope Client received incorrect information.
Solution:
You can verify the following details in your MDM to rectify this issue:
The
configuration object
carrying enrollment data (either App Configuration or VPN profile) is delivered to the device.
The configuration object has appropriate assignments in MDM.
The keys name syntax match the following:
OrgKey
AddonHost
UserEmail
enrollauthtoken
enrollencryptiontoken
Add
enrollauthtoken
and
enrollencryption
tokens only if they are created in
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distribution
>
Secure Enrollment
Delete and recreate configuration objects carrying enrollment data from MDM and repeat correct assignments.
Unenroll device if possible and delete or redeploy Netskope Client along with other associated configuration objects.
Problem 2:
The enrollment fails even after the Netskope Client receives accurate enrollment data with the correct key names.
Solution:
In such cases, tap the
Netskope Client
icon in the top-right corner of your screen and tap
Configuration
. In the event of a configuration failure, the following screen is displayed:
Click the
Update again
link to retry the configuration update. If there is no progress in the update for more than five minutes, it indicates that the enrollment values are incorrect. You can verify the following details to rectify the issue:
Enrollment key value data type are strings (most MDMs default to strings, some allow other data type to be specified).
Correct syntax for OrgKey and AddonHost values.
Correct MDM variable pointing to user identity.
MDM provided an identity match the UPN provisioned with Netskope tenant.
If a VPN profile is used for bringing in enrollment variables, ensure that it has On-Demand settings enabled in MDM configuration.
Click the Netskope Client icon, export Netskope client logs and search in nsAppUI.log file for enrollment data received from MDM.
In this Topic
Troubleshooting Guide for iOS Netskope Client App

---
## Deploy Client on Android Using IBM MaaS360
**URL:** https://docs.netskope.com/en/deploy-client-on-android-using-ibm-maas360/
**Last Modified:** 2025-08-31T01:48:35+00:00
**Scraped:** 2026-06-26T09:24:28.618436+00:00

Deploy Client on Android Using IBM MaaS360 - Netskope Knowledge Portal
Deploy Client on Android Using IBM MaaS360
This topic covers the steps to deploy Netskope Client for Android mobile devices using IBM MaaS360.
Prerequisites
On the Netskope UI, go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distributio
n. Download the Netskope Root Certificate and Intermediate certificates. These are needed to configure IBM MaaS360 certificate profiles.
On the MDM Distribution page, scroll down to
Create VPN Configuration
section to find your
Organization ID
.
User accounts provisioned within the MDM/EMM platform must match with those provisioned with the Netskope tenant.
Add Netskope Client App
The following section describes the steps to add the application from Google Play app in the IBM MaaS360 console.
To add Netskope Client:
In the IBM MaaS360 console, go to
Apps
>
Catalog
.
In the App Catalog page, click
Add
>
Android
>
Google Play App
.
The
Add Google Play App
window is displayed. In the text field, search for Netskope Client.
Click the Netskope Client app to select.
Click
Select
and
Approve
the permissions to the app.
Click
Add
to add Netskope Client to the App Catalog.
Distribute and Assignment
This section describes the steps to distribute and assign the Netskope Client app to devices in a group after adding Netskope Client to the App Catalog. To learn more, view
Deploy Apps to Devices
.
To distribute and assign NS Client:
In the
App Catalog
page, click Netskope Client.
On the top-right corner of the Netskope Client app page, click
Distribute
.
In
Distribute App: Netskope Client
, make an assignment to the appropriate group.
Click
Distribute
.
Setting up Netskope Client
Setting up Netskope Client for  Android devices with IBM MaaS360 includes the following mandatory steps:
Automatic Netskope Client deployment along with enrollment data
.
Deployment VPN Profile Configuration
.
Deployment of  Trusted Root Netskope Certificate Profile
.
Automatic Installation and App Configuration
You need to set up automatic app installation and enrollment settings for Netskope Client from the MaaS360 Portal. To learn more, view
Configure Automatic App Installation
.
To install Netskope Client automatically:
In the
App Catalog
page, click Netskope Client.
In the Netskope Client app page, scroll down to
Install Settings
and select the following options:
Install Automatically
Retry Installation
In the
App Configurations
section, click
Add Configuration
.
In the
Configuration
tab, provide the following:
UserEmail:
%email%
Host:
addon-<tenant-URL>
Token:
<Organization ID>
This value is retrieved from Netskope tenant.
Click
Next
.
Select the checkbox for
Set as default configuration
.
Click
Publish
.
Push VPN Profile Configuration
To provide a seamless Netskope Client deployment in IBM MaaS360, you need to create a VPN profile controlled through security policies. You can either create a new security policy or a VPN profile to an existing policy. To learn more, view
Create Security Policy
.
To add a VPN profile in a security policy:
In the IBM MaaS360 console, go to
Security
>
Policy
.
Click
Add Policy
.
Provide the following details:
Type: Android MDM
Start From: Business Templates Based Policies
Business Usecase – Select an appropriate one and click Continue.
The
Policy Details
page is displayed.
Select
VPN
and click
Edit
to configure the settings.
Enable Always On VPN: Select the checkbox to enable this option
Always on VPN Package Name: Enter com.netskope.netskopeclient
Enable Lockdown: Select this checkbox to enable this option.
Click
Next
.
Assign the policy to the appropriate group.
Click
Save and Publish
.
Create a Trusted Netskope Root Certificate Profile
Adding certificates enables you to perform SSL inspection. To learn more about SSL Inspection for Android, view
SSL Inspection
.
To upload the Intermediate and Root certificates:
In the IBM MaaS360 console, go to
Security
>
Policy
.
Click
Add Policy
.
Provide the following details:
Type: Android MDM
Start From: Business Templates Based Policies
Business Use Case – Select an appropriate one and click Continue.
The
Policy Details
page is displayed.
Select
Certificates
and click
Edit
to upload the certificates.
Click
+
to upload a new certificate.
In the
Upload New Certificate
window, provide the certificate name and upload the Netskope Root Certificate.
Click the refresh icon on the right and select the uploaded certificate name from the dropdown.
Repeat the steps 6 to 8 for uploading and selecting the Intermediate certificate.
Click
Next
,
Next
and
Publish
.
You can add the Certificate and VPN profile details under one security policy and assign them to an appropriate group. If you are creating separate policies for Certificate and VPN profiles, you must add them to appropriate groups separately.
In this Topic
Deploy Client on Android Using IBM MaaS360

---
## Deploy Client on iOS Using Omnissa Workspace ONE
**URL:** https://docs.netskope.com/en/deploy-client-on-ios-using-omnissa-workspace-one/
**Last Modified:** 2026-02-19T13:39:42+00:00
**Scraped:** 2026-06-26T09:24:39.194627+00:00

Deploy Client on iOS Using Omnissa Workspace ONE - Netskope Knowledge Portal
Deploy Client on iOS Using Omnissa Workspace ONE
This article describes how to deploy Netskope Client on iOS devices using Omnissa Workspace ONE.
Prerequisites
Administrators must possess proficient working knowledge of Omnissa Workspace ONE UEM.
Administrators must review
Netskope Client Client Enrollment Methods
to understand the Client User Enrollment methods available for their environment.
Import users into the Netskope tenant – see
Provisioning Users for Netskope Client
.
Download
Netskope Root and Tenant Certificates
and ensure the certificates are available when needed.
See
Deploy Netskope Client via IdP
when using IDP as the method of user enrollment.
Supported Platforms and Enrollment Methods
This article outlines the Netskope Client deployment instructions for the following user enrollment methods and supported platforms. User enrollment methods not documented here are not supported at this time.
Enrollment Method
Single User
Multi-User
PLIST
Y
N
Configuration Profile Setup
Profiles manage the core configuration for Client installation. The following sections detail how to configure these profiles effectively.
Administrators must choose the VPN profile type that best fits their requirements, either
On-Demand VPN
or
Per-App VPN.
Netskope Client does not allow the coexistence of multiple VPN profiles on the same device. You can create multiple VPN profiles in the Workspace One console and assign them to various smart groups to accommodate corporate and BYOD use cases.
On-Demand VPN
The following steps explain how to configure a Profile for an On‑Demand VPN deployment.
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple iOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
VPN
in the search text box of the configuration profile.
Expand
VPN
and click
Add
.
Configure the following settings to allow access to a service or an app:
Connection Name:
Enter a descriptive name for the Connection Name.
Connection Type:
Select Custom.
Identifier:
com.netskope.Netskope
Server:
Enter your VPN server name from the Netskope UI. For example, gateway-<tenant-URL>.
Account:
Click the + symbol and select EnrollmentUserID.
Custom Data: Add the following Key:value pairs:
OrgKey: Use the tenant organizational key
AddonHost: Use the addon URL for the tenant: addon-<tenant-URL>.
UserEmail: Use the variable that contains the user identity for the enrolment: {EmailAddress}
enrollauthtoken: ​​ Enter the Authentication Token.
​​enrollencryptiontoken:​​ Enter the Encryption token(Optional).
ForceDisabledSteering: True.
Use this key-value pair if you want Netskope Client to steer only Private Access traffic.
User Authentication:
Select Certificate.
Enable VPN On Demand:
Select the checkbox to enable this option.
Use new on-demand Keys:
Select the checkbox to enable this option.
Click
Next
.
Enter these parameters:
Smart Groups: Start typing to select a smart group.
Exclusions: No
Deployment: Managed
Assignment Type: Auto
Allow Removal: Always( You can select the desired option)
Managed By: Netskope Inc.
Click
Save & Publish
.
Per-App VPN
The following steps explain how to configure a Profile for a Per-App VPN deployment.
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple iOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
VPN
in the search text box of the configuration profile.
Expand
VPN
and click
Add
.
Configure the following settings to allow access to a service or an app:
Connection Name:
Enter a descriptive name for the Connection Name.
Connection Type:
Select Custom.
Identifier:
com.netskope.Netskope
Server:
Enter your VPN server name from the Netskope UI. For example, gateway-<tenant-URL>.
Account:
Click the + symbol and select EnrollmentUserID.
Custom Data:
Add the following Key:value pairs:
OrgKey: Use the tenant organizational key
AddonHost: Use the addon URL for the tenant: addon-<tenant-URL>.
UserEmail: Use the variable that contains the user identity for the enrolment: {EmailAddress}
enrollauthtoken: ​​ Enter the Authentication Token.
​​enrollencryptiontoken:​​ Enter the Encryption token(Optional).
ForceDisabledSteering: True.
Use this key-value pair if you want Netskope Client to steer only Private Access traffic.
OnDemandConnectionsHoldTimeout: 20
To define timeout to control the iOS On-demand connections hold feature, add the key-value pair: OnDemandConnectionsHoldTimeout: <numeric value in seconds>. This numeric value in the VPN profile can hold the connection for a longer time until it establishes the tunnel successfully and handles traffic. Netskope recommends using values that are large enough to cover normal connection time.
Per-App VPN Rules: Toggle to enable this option.
Connect Automatically: Toggle to enable this option.
Provider Type: Select Packet Tunnel from the options in the dropdown menu.
User Authentication: Select Certificate.
Click
Next
.
Enter these parameters:
Smart Groups: Start typing to select a smart group.
Exclusions: No
Deployment: Managed
Assignment Type: Auto
Allow Removal: Always( You can select the desired option)
Managed By: Netskope Inc.
Click
Save & Publish
.
Associate Per App VPN Profile With Managed App Configuration
The following section describes the steps to associate managed applications with Per App VPN profile in Omnissa Workspace ONE.
Go to
Resources
>
Apps
>
Native
.
Click the
Public
tab.
Select managed application (For example, Box) and click the application.
Click
Assignment
and click on assignment rule.
Select
Tunnel & Other Attributes
, click
Edit
and select Per App VPN profile from the dropdown.
Click
Save
and
Publish.
Zero-Touch Enrollment
Netskope client is capable of enrolling silently without any user action when enrollment data supplied through a VPN profile. For a limited number of use cases such as testing mapped to single identity, kiosks deployments and alike enrollment data should be populated through VPN profile and email key must use static email address value (which is provisioned in Netskope tenant).
Push Netskope Root and Tenant Certificates
Provide additional trust to end users by pushing certificates during client installation. Before you can push the root and tenant certificates, ensure that you do the following:
Download root and tenant certificates from Netskope MDM distribution page.
Login to Netskope tenant admin console with admin credentials.
Go to
Settings
>
Security Cloud Platform
>
MDM Distribution
. The certificate download options are displayed in the Certificate Setup section.
Convert the downloaded certificates to
.cer
format by renaming the .pem files to .cer.
Perform the following steps to add certificates to Omnissa Workspace ONE:
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple macOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
Credentials
in the search text box of the configuration profile.
Expand
Credentials
and click
Add
.
Enter the following details:
Credential Source: Select
Upload
.
Credential Name: It auto-populates the name after uploading the certificate.
Certificate: Click
Choose File
> Browse for the rootcaCert.cer file you downloaded from the Netskope tenant.
Click
Attach Certificate
.
Once you click
Attach Certificate
, the webUI displays the uploaded certificate details such as validity, thumbprint, and so on.
Click
+Add
to add another certificate.
Click
Choose File
>
Browse
for the
caCert.cer file you downloaded from the Netskope tenant.
Click
Attach Certificate
.
The webUI now displays two Credentials tabs in your Credentials payload.
Click
Next
.
Add the assignment details.
Click
Save & Publish
.
Add Netskope Client App
Public Apple Store
The following section describes the steps to add the application from the public store in Omnissa Workspace ONE.
Perform the following steps to add Netskope Client:
Go to
Resources
>
Apps
>
Native
.
Click the
Public
tab.
Click
+ADD APPLICATION
.
Select
Apple iOS
from the Platform dropdown menu.
In
Source
, click
SEARCH APP STORE
.
Purchased App via Apple Business / School Manager
Purchase Netskope Client through the respective tools if your organization is leveraging Apple Business Manager or Apple School Manager. The Netskope Client shows up in the list of applications available for deployment after the tokens are synchronized.
Go to
Resources
>
Apps
>
Native
.
Click
Purchased
tab.
Click
+Select
for Netskope Client application.
Netskope Client Assignment Settings
To configure the assignment settings:
In the
Add Application – Netskope Client
window, click
Save & Assign
.
After you click
Save & Assign
, it navigates to the assignment configuration for the App.
In
Netskope Client – Assignment > Distribution
, enter the assignment Name and select a target smart group.
In
Netskope Client – Assignment > Restrictions
, configure the
app restrictions.
Click
Create
and save the assignments.
Click
Publish
once you review the app setting.
In this Topic
Deploy Client on iOS Using Omnissa Workspace ONE

---
## Netskope Client Supported OS and Platform
**URL:** https://docs.netskope.com/en/netskope-client-supported-os-and-platform/
**Last Modified:** 2026-05-22T06:55:27+00:00
**Scraped:** 2026-06-26T09:24:54.952940+00:00

Netskope Client Supported OS and Platform
This article describes the versions that are supported for each operating system.
The following table lists the supported major versions for each platform. Netskope support coverage includes all minor versions within the listed major versions, unless a specific minor version is explicitly called out. Where a minor version is specified, only that particular release is supported for the corresponding major version.
Beta versions of any operating system are unsupported.
Category
Supported Versions
Notes
Windows Operating System
Desktop
Windows 10, Windows 11
Windows 365
Server
Windows Server 2012 R2
**
, 2016, 2019, 2022, 2025
Netskope Private Access (NPA) is supported for devices running Windows 11 on Snapdragon-based PC.
Cloud Access Security Broker(CASB) or Security Web Gateway (SWG) is supported on Windows 11 with the Snapdragon chipset.
Netskope Endpoint Data Loss Prevention (Endpoint DLP) is supported on devices running Windows 11 on 64-bit processors.
**
There are a few limitations for Netskope Client support with
Windows 2012 R2
:
Protect Client configuration and resources
option is not supported.
All Traffic steering modes are not supported. Netskope Client falls back to the Web Traffic mode if All Traffic is selected in the Steering Configuration.
Do not support auto-upgrade of Netskope Client.
Apple macOS / iOS
macOS
14(Sonoma), 15(Sequoia), 26(Tahoe)
iOS
15.1, 16, 17, 18, 26
Netskope supports Apple x86, M1, M2, M3, M4, and M5 chipset hardware.
Netskope Endpoint Data Loss Prevention (Endpoint DLP) is supported on macOS devices 14 (Sonoma), 15 (Sequoia), and 26 (Tahoe) running either on Intel x64 or Apple Silicon AND Full Disk Access.
macOS 26 (Tahoe) is supported only from version 131.0.0 or higher
Linux
Ubuntu 22.04, 24.04 LTS desktop version
Linux Mint Desktop Versions 21 (Cinnamon Edition)
Red Hat Enterprise Linux versions 9.4, 9.6 (Plow)
Debian 12 (Bookworm)
Cloud Firewall (CFW) support on Netskope Client for Linux will be provided in the future release.
Netskope Private Access (NPA) also supports Ubuntu 24.04.
System reserved domains like .local for Private Apps are not supported on Ubuntu.
Netskope also supports WSLv2(Beta).
Netskope announces end-of-support for Ubuntu 20.04 and Linux Mint versions 19 and 20 by May 31, 2025. To learn more, view
End-of-support for Linux versions
.
Netskope Private Access periodic re-authentication is not supported on Linux CLI mode.
Google
Android
13 (Tiramisu), 14 (Upside Down Cake), 15(Vanilla Ice Cream), 16 (Baklava)
ChromeOS
ChromeOS 120 to 148
Android Runtime Version 9, 11
Netskope supports ARM64 for Android devices.
Netskope supports ARM64 and x86_64 bit architectures for ChromeOS devices.
Cloud Firewall (CFW) support on Netskope Client for Android will be provided in the future release.
Netskope Private Access periodic re-authentication is not supported on Android and Chromebook.
Multi-user Platforms
Windows Terminal Server
2016, 2019, 2022
VDI
Citrix Virtual Apps and desktops 7 2203 LTSR CU4(2203.0.4000.4310), Citrix Virtual apps and Desktops 7 2402 LTSR CU2 (2402.0.2510.2566)
Supported OS: Windows 11, Windows Server 2019 (Multi Session), Windows Server 2022
Azure Virtual Desktop
Supported OS: Windows 10 and 11
Ominssa Horizon
Supported OS: Windows 11, Windows Server 2019 (Multi Session)
Amazon Workspaces
Netskope Private Access now supports multi-user virtual desktop environments based on Windows, such as Citrix VDI and Azure Virtual Desktop.
– Netskope ended extending support for a few operating systems. To learn more, view
Netskope Client End of Support Announcement for Older OS Versions
.
– See the
Netskope Client Interoperability
topic to learn more about Netskope Client compatibility with third-party apps.
In this Topic
Netskope Client Supported OS and Platform

---
## Device Client Data Collection
**URL:** https://docs.netskope.com/en/advanced-analytics-device-client-data-collection/
**Last Modified:** 2026-06-10T05:03:12+00:00
**Scraped:** 2026-06-26T09:25:14.289270+00:00

Device Client Data Collection - Netskope Knowledge Portal
Device Client Data Collection
The Advanced Analytics Device Client Data collection and accompanying dashboards provide an overview of the most recent organization wide client status.
Client version management ensures your clients are updated with the supported versions, which includes enhancements and future patches. In addition, a dashboard filter, ‘Client Update Reason’ provides insight to the reasons why clients are disabled.
This data collection provides the following key benefits:
Current Device Status
:
What is the current status of devices?
Client Versions in Use
: Which client versions are in use? How many devices are on unsupported, supported, or Golden release versions?
Device Investigation & Troubleshooting
: How many times has a user disabled their client? What is the history of client changes for a given user/device? What are the reasons that a client was disabled?
Current Device Status
This dashboard provides the following:
# Devices
: total number of installed devices
# Users
: total number of users with the client installed
# Users With Currently Disabled Devices
: total number of users that do not have an active client enabled
# Users Who Turned Off Their Clients
: total number of user that disabled their clients manually
Client Status (# of Users)
: percentage breakdown of users that have disabled clients or enabled clients. To learn more:
Client Status
Internet Security Status
: Type of client status. To learn more:
Internet Security Service Status
Private Access Status
: Type of client status. To learn more:
Private Access Apps Status
Client Status
There are several Client Status fields that display to differentiate among Client Status (overall status), Internet Security Status, and NPA Status.
For each row of data, you may see the following statuses:
Client Supported Status
: Shows the last updated status at a moment in time (i.e. timestamp date); you’ll see this value change for different event timestamps.
Current Client Version
: Status of the client at the moment the query runs. This is the same record repeated multiple rows at different event timestamps, until the status changes.
Historical Client Status
: This field contains data if the status changed for that particular record at a moment in time.
Null
: A ‘null’ client status/internet security/private access value means the service is not active or is not activated for the device.
Client Versions in Use
The Devices by Current Version widget is updated to show the status of the latest supported and unsupported client versions. The widget is color-coded based on the ‘Client Supported Status’ and is automatically updated in the future. This dashboard identifies any unsupported client versions in use. Best practice is to upgrade the devices listed as ‘Unsupported’ to supported client versions.
This widget provides the following:
Current Client Version
Colored column: color-coded based on the ‘Client Supported Status’.
Client Supported Status: Supported – Golden Release, Supported- Latest Release, Supported, Unsupported
# Devices
# Hostnames
# Users
In addition, you can drilldown to view details such as ‘Why were clients disabled?’ and ‘Top Users Disabling Devices.’
Client Version Trend
This dashboard provides the number of updated hostnames based on their major version, and the date on which the client version was updated.
Device Investigation & Troubleshooting
This set of dashboards helps to look at a particular device, hostname, or user and filter to view details such as:
Top Users By Update Events
Top Users Disabling Devices
Overall Device Status & Change Reasons (# Events)
: This view is helpful to look at a single user’s device change history
Internet Security Status (# Events)
Private Access Status (# Events)
Device Events –  Detailed View
: Detailed view of a single user’s device change history
Top Users By Update Events
Top Users Disabling Devices
Overall Device Status & Change Reasons (# Events)
This view is helpful to look at a single user’s device change history.
To learn more:
Client Status
Internet Security Status (# Events)
To learn more:
Device Custom Filters
Private Access Status (# Events)
To learn more:
Device Custom Filters
Device Events –  Detailed View
This is a detailed view of a single user’s device change history.
Monitoring and Troubleshooting
The information provided by the Advanced Analytics device client data collection and accompanying dashboards help to monitor and troubleshoot the overall performance and health of your network.
Advanced Analytics data has a roughly ~1 hour data lag, please keep this in mind as you look at the “current status” information.
Data Retention
The system enforces data retention based on your licensing. To learn more:
Advanced Analytics Data Retention
Key Fields
The following table lists and describes the various fields that appear in the Advanced Analytics Device Client Data collection and accompanying dashboards.
DISPLAY NAME
GROUP
DESCRIPTION
TYPE
City
General
Location of user based on IP
String
Client Installation Date
General
Date of last successful client installation
Date
Client Installation Time
General
Time of last successful client installation
Time
Client Supported Status
General
This field shows the current client support status for the selected device client (e.g. Supported - Golden Release, Supported, Unsupported, etc.)
String
Client Version
General
Client version
String
Client Version (Major Release)
General
Current major client version
Number
Current Client Version
General
Current client version
String
Current Device Classification Status
General
Current device classification status
String
Current Device Make
General
Current manufacturer name (e.g. Dell, HP, Apple)
String
Current Device Management ID
General
Current device management ID
String
Current Device Model
General
Current device model (e.g. Inspiron, MacPro, MacMini)
String
Current Hostname
General
Current hostname
String
Current OS
General
Current OS
String
Device Classification Status
General
Device classification status
String
Device ID
General
Device ID
String
Device Make
General
Device manufacturer name (e.g. Dell, HP, Apple)
String
Device Management ID
General
Device management ID
String
Device Model
General
Device model ( e.g. Inspiron, MacPro, MacMini)
String
Hostname
General
Hostname
String
Last Event Actor
General
The source/actor that generated the event such as the system, user, or admin
String
Netskope Host POP
General
Netskope POP to which the client connected
String
OS
General
Operating system
String
OS Version
General
OS version
String
Client Status
Status
Last received device status
String
Client Status Update Reason
Status
Client status change reason
String
Current Client Status
Status
Current last received device status
String
Current Client Status Update Reason
Status
Current client status change reason
String
Current Internet Security Status
Status
Current internet security status
String
Current Private Access Status
Status
Current private access status
String
Current Service Name
Status
Shows which service the client status is associated with (e.g. Private Access, NPA, etc.)
String
Internet Security Status
Status
Display devices with respect to the internet security status such as Enabled, Disabled, Errored, Fail Closed, Backed Off, etc.
String
Private Access Status
Status
Last received Secure Access tunnel (Private Access)
String
Service Name
Status
Shows which service the Client Status is associated with (e.g. Private Access, NPA, etc.)
String
Historical Data Client Status
Historical
Client status at the last update time
String
Historical Data Client Status Update Date
Historical
Date when the Client Status was last updated
Date
Historical Data Client Status Update Reason
Historical
Client Status Update Reason at the last update time
String
Historical Data Client Status Update Reason Update Date
Historical
Date when the Client Status Update Reason was last updated
Date
Historical Data Client Status Update Reason Update Time
Historical
Date when the Client Status Update Reason was last updated
Date time
Historical Data Client Status Update Time
Historical
Date when Client Status was last updated
Date time
Historical Data Client Version
Historical
Client version at the last update time
String
Historical Data Client Version Update Date
Historical
Date when Client Version was last updated
Date
Historical Data Client Version Update Time
Historical
Date when Client Version was last updated
Date time
Historical Data Device
Classification Status
Historical
Device classification status at the last update time
String
Historical Data Device
Classification Status Update Date
Historical
Date when Device Classification Status was last updated
Date
Historical Data Device
Classification Status Update Time
Historical
Date when Device Classification Status was last updated
Date time
Historical Data Event Actor
Historical
Event actor at the last update time
Date
Historical Data Event Actor Update Date
Historical
Date when Event Actor was last updated
Date
Historical Data Event Actor Update Time
Historical
Date when Event Actor was last updated
Date time
Historical Data Hostname
Historical
Hostname at the last update time
String
Historical Data Hostname Update Date
Historical
Date when Hostname was last updated
Date
Historical Data Hostname Update Time
Historical
Date when Hostname was last updated
Date time
Historical Data Internet Security Status
Historical
Internet security status at the last update time
String
Historical Data Internet Security Status Update Date
Historical
Date when Internet Security Status was last updated
Date
Historical Data Internet Security Status Update Time
Historical
Date when Internet Security Status was last updated
Date time
Historical Data OS Version
Historical
OS Version at the last update time
String
Historical Data OS Version Update Date
Historical
Date when the OS version was last updated
Date
Historical Data OS Version Update Time
Historical
Time when OS version was last updated
Date time
Historical Data Private Access Client Status
Historical
Private Access Client Status at the last update time
String
Historical Data Private Access Client Status Update Date
Historical
Date when Private Access Client Status was last updated
Date
Historical Data Private Access Client Status Update Time
Historical
Date when Private Access Client Status was last updated
Date time
Historical Data User
Historical
User assigned to the device at the last update time
String
Historical Data User Update Date
Historical
Date when User assigned was last updated
Date
Historical Data User Update Time
Historical
Date when User assigned was last updated
Date time
In this Topic
Device Client Data Collection

---
## Netskope Client Troubleshooting Guide
**URL:** https://docs.netskope.com/en/netskope-client-troubleshooting-guide/
**Last Modified:** 2026-04-06T12:13:37+00:00
**Scraped:** 2026-06-26T09:25:58.797287+00:00

Netskope Client Troubleshooting Guide
This guide is designed to help troubleshoot issues with end-users and administrators using Netskope Client.
Netskope Client
steers traffic from the end-user device to the Netskope Cloud. The Client creates an SSL tunnel from the end device and terminates it at the Netskope forward proxy in the Cloud. The tunnel carries traffic that is selected by the administrators as part of the
steering configuration
. All
intermediate and root CA Certificates
are installed in the system cert store during the Netskope Client installation to facilitate the SSL termination.
General Troubleshooting Methods
Is my Netskope Client installed and active?
The easiest way is to check the taskbar or menu bar for an active Netskope icon on your screen.
Windows
macOS
Linux
If Netskope Client is hidden by your administrator, use the Task Manager (Windows) or Activity Monitor(macOS) to check the Netskope Client service.
To learn more, view
Using Netskope Client
.
Where can I view more details about the Netskope Client?
To view details, do the following:
Click the Netskope Client icon.
Select
Configuration
to display the window. The following details are constant including Organization, Gateway, Steering Configuration, and so on.
Organization
Gateway: The Gateway IP however will be intelligently identified based on your location. In this case, A user based out of Austin, TX is redirected to the closest Netskope datacenter of Dallas for gateway-tenant.goskope.com.
Gateway IP
User Email: The User Email will typically be the UPN derived from the iDP and unique to each user.
To learn more, view
Netskope Client.
Is my Netskope Client disabled?
An administrator or end-user can enable a disabled Client. If disabled, click the Netskope Client icon and select
Enable Netskope Client
option to activate the Client again.
How can I know if I am connected to the nearest datacenter?
The Netskope Client always routes traffic to the nearest datacenter (with Client assisted GTM). The
Gateway
IP in the Netskope Client Configuration must display the location of the nearest datacenter.
How do I know if a specific website is steered through Netskope?
The Netskope Client steers traffic from the user machine to the Netskope Cloud.
Cloud Apps – Only defined SaaS app traffic over ports 80, 443 is steered.
All Web Traffic – All traffic going to ports 80,443 is steered. Non-standard ports configured on the webUI are also steered.
All Traffic – Steer all HTTP(S) and non-HTTP(S) to the Netskope cloud for deep analysis.
In CASB/Cloud Apps mode, Netskope does not steer All Web traffic today and is limited to specific applications defined in the steering configuration. The easiest way is to view the application browser certificate and check if the Issuer is signed by Netskope.
The following example shows the browser certificate details when the traffic from box.com is steered through Netskope.
Steered through Netskope
Not steered through Netskope
For non-web traffic, you can check SkopeIT in your tenant and view whether your traffic was bypassed or blocked by Netskope.
How does the Netskope Client determine what to steer?
The Netskope Client inspects the end device packets using OS packet filtering capabilities (Traffic mode and exceptions). This process varies according to the OS and the presence of Explicit Proxy in the network.
Will my applications/web sites see my IP address or Netskope address?
All sites that are steered through Netskope will see the source (egress) IP as coming from Netskope IP address space.
If applications require source IP allowlisting, they will need to allowlist the Netskope IP ranges found here:
Consolidated List of IP Ranges for Allowlisting
.
Private Access
How can I know if my Client is connected to NPA?
Right-click on the Netskope Client icon in the system tray and select
Configuration
. Private Access should show as
Connected
.
For Windows, you can also check one of the following options:
The tooltip of Netskope Client icon in the tray icon shows the NPA status. Or,
Click the Netskope Client icon and check the
Services
section. It displays
Private Access
if the NPA status is enabled.
If the Configuration shows Private Access as
Disabled
, make sure the
Steer all Private Apps
option is enabled in the Steering Configuration settings for your tenant. Go to
Settings > Security Cloud Platform > Steering Configuration
.
If you are using only the Default tenant configuration, click
Edit
in the upper right corner. If you have multiple Steering Configurations, click on the name of the Steering Configuration you are using for NPA to open the details page.
What can I do when the NPA Tunnel is getting disabled?
If you cloned a VM snapshot and installed it on multiple machines, this will cause the NPA tunnel to become disable. The NPA backend requires the netskope-device-id to be unique, which is derived from the machine-id.
You need to regenerate unique machine-ids following these steps:
Stop the client service.
sudo systemctl stop stagentd.service
Remove NPA certificates from /opt/netskope/stagent/data. The following certificates needs to be removed:
npaccesscert.pem
npaccesskey.pem
npatenantcert.pem
Remove the machine-id.
rm /etc/machine-id 
rm /var/lib/dbus/machine-id
Regenerate the machine-id.
dbus-uuidgen --ensure
systemd-machine-id-setup
Verify the new machine-id.
cat /etc/machine-id
host namectl
Reboot the machine.
sudo reboot
Endpoint DLP
Where can I enable Endpoint DLP to my client configuration?
Endpoint DLP is an add-on feature for the Netskope Client. To enable Endpoint DLP for the Netskope Client, contact your sales representative.
Select Enable Endpoint DLP to enable
Endpoint Data Loss Prevention
for the client configuration and apply Content and Device Control policies to the devices. You can enable Endpoint DLP for the Default Tenant Config to apply policies to all client users or for custom client configurations to apply policies to specific users.
Troubleshooting Configuration Issues
How can I perform a speed test on the connected Netskope POP?
Click the Netskope Client icon.
Select
Advanced Debugging
.
Click
Speed Test
.
Select the desired
File Size
option.
Click
Start
.
For example, view the following screenshots for macOS:
How can I restart the Netskope Service on my Windows, macOS, or Linux devices?
Use the following commands:
Windows
Ensure that Protect Client configuration and resources field is disabled in Client Configuration.
Start Service:
stagentsvc -start
Stop Service:
stagentsvc -stop
macOS
Pre Big Sur
Start Service:
sudo launchctl load
/Library/LaunchDaemons/com.netskope.stagentsvc.plist
Stop Service:
sudo launchctl unload
/Library/LaunchDaemons/com.netskope.stagentsvc.plist
BigSur/Monterey or later
There is no command to stop network extension. You need to disable the client from the UI.
Linux
Start service:
sudo systemctl start stagentd.service
Stop service:
sudo systemctl stop stagentd.service
How can I gather information about the Netskope Client using API?
https://<tenant-URL>/api/v1/clients
– This endpoint returns information related to the Netskope Client. To learn more, view
Get Client Data
.
How do I save my Netskope Client logs?
To save Client logs, go to Netskope Client icon >
Save Logs
. You can save the
.zip
log file to a specific folder.
If the Client is hidden by your administrator, use command-line options to save the
.zip
log files.
Windows =
Nsdiag.exe –o mylogs.zip
Mac =
./nsdiag –o mylogs.zip
Linux =
/opt/netskope/stagent/nsdiag -o mylogs.zip
Android =
NetskopeLogs.zip
How can I collect the log details from my Netskope account?
Go to
Settings
>
Security Cloud Platform
>
Devices
page, search for the username and click the device name.
Click
Collect Log
on the top right-hand corner.
Once the log file is generated, the admin (requestor) receives an email with the link to download the log to their local computer in zip format.
The link redirects to your Netskope tenant Devices webUI.
Click
Download Log
.
Where can I find the Netskope certificates and branding files?
Windows:
C:\ProgramData\netskope\stagent
macOS:
/Library/Application\ Support/Netskope/STAgent
Linux:
/opt/netskope/stagent/
Android:
Settings
>
Biometrics and Security
>
Other Security Settings > View Security Certificates
. Tap on the
User
tab. You can see the Security certificates for Netskope.
iOS:
Settings
>
VPN
>
VPN Profile
>
More Details
. The branding file is protected and not viewable.
Where can I find the Netskope Log files?
Windows
Processes
Log Location
Netskope Client services and other processes running as admin
%ProgramData%/Netskope/stagent/Logs
User process
%APPDATA%/Netskope/STAgent/Logs
Service crash dump
%ProgramData%/Netskope/stagent/Logs
UI Crash dump
%APPDATA%/Netskope/stagent/Logs
macOS
Processes
Log Location
System extensions and other processes with root privilege
/Library/Logs/Netskope
User process
~/Library/Logs/Netskope
Linux
Processes
Log Location
Service and installation logs
/opt/netskope/stagent/logs
UI and stAgentApp
~/.netskope/stagent/logs
Android
Go to the Netskope
Client app
.
Click the three dots.
Select
Send Logs
.
You can download it to the desired location.
iOS
Users cannot read Netskope logs on iOS devices, but you can download Netskope logs zip files and share them through AirDrop and email.
Where can I find the Netskope executables and diagnostic tools?
Windows:
32-bit: C:\ProgramFiles (x86)\Netskope\STAgent\
64-bit: C:\ProgramFiles\Netskope\STAgent\
macOS:
/Library/Application\ Support/Netskope/STAgent
Linux
: /opt/netskope/stagent/
Diagnostic command in Windows:
32-bit: C:\Program Files (x86)\Netskope\STAgent\nsdiag.exe
64-bit: C:\Program Files\Netskope\STAgent\nsdiag.exe
Diagnostic command in Mac:
/Library/Application Support/Netskope/STAgent/nsdiag
Diagnostic command in Linux:
/opt/netskope/stagent/nsdiag
Netskope Client’s stAgent process failed to initialize and the stAgentUI failed to launch when resuming  an active session from a locked or disconnected state after installing/upgrading/reconfiguring  Netskope Client from single to multi-user mode on Windows environment with IDP enrollment. How should I fix this?
When the Netskope Client is deployed/upgraded/reconfigured from single user mode to multi-user mode using IdP enrollment on a Windows device, the stAgent process fails to initialize for users who transition from an inactive or locked state back to an active session.
For example, Two users User A, and User B use a Windows system.
User B is active on the system and User A who is logged in but inactive.
Netskope Client gets installed/upgraded/reconfigured from single user mode to multi user mode and the session for User B is created successfully.
User B locks the screen, which moves the session into an inactive state.
User A unlocks the screen but the Netskope Client doesn’t initialize for User A and there is no stAgentUI process for User A. This disrupts the traffic steering for User A and keeps the Client inactive.
To restore stAgentUI process and ensure proper traffic steering for User A, Netskope recommends performing log off and login for user A to eliminate any inactive Netskope Client issue.
In this Topic
Netskope Client Troubleshooting Guide

---
## Deploy Client on iOS Using Ivanti Neurons
**URL:** https://docs.netskope.com/en/deploy-client-on-ios-using-ivanti-neurons/
**Last Modified:** 2026-05-06T09:02:45+00:00
**Scraped:** 2026-06-26T09:26:26.215091+00:00

Deploy Client on iOS Using Ivanti Neurons - Netskope Knowledge Portal
Deploy Client on iOS Using Ivanti Neurons
The following sections explain how to upload and enroll certificates and how to configure an iOS profile for Ivanti Neurons (formerly known as MobileIron Cloud) for on-demand or per-app VPN. For information about iOS VPN fail-open, refer to
iOS VPN Fail Open
.
Create Certificates in Ivanti Neurons
To configure Ivanti Neurons, you need to create a local standalone CA, or use a third-party CA, and also Identity certificates in Ivanti Neurons.
Create a Standalone CA Certificate
To create a standalone CA certificate:
In the
Mobile Iron Cloud
admin console, go to
Admin > Certificate Authority
.
Click
Add
.
Click
Continue
under
Create a Standalone Certificate Authority
.
Click
Actions
, and then select
Download Certificate
. Note where you saved the certificate.
On macOS, open
Terminal
and use openssl to convert the certificate from .cer format to .pem format. Use the following command to convert the certificate from .cer to .pem format:
sudo openssl x509 -inform der -in cert.cer -out cert.pem
Verify the .pem file using this command:
cat cert.pem
Upload the certificate to Netskope using the following instruction:
Go to
Settings > Security Cloud Platform > Netskope Client > MDM Distribution
.
Scroll to the
Upload Certificate to Netskope
section under Deployment Resources for iOS.
Click
Upload/Replace Certificate
.
Click
Select File
to locate and select your certificate file.
Click
Upload/Replace Certificate
, and then click
Select Certificate
to locate and select your certificate file.
Create an Identity Certificate
To create an identity certificate:
In the
Mobile Iron Cloud
admin console, select Configurations and click
Add
.
Select
Identity Certificate
. Select
Identity Certificate
.
Enter the following parameters:
Name:
Enter a unique name for the certificate.
In the Configuration Setup section:
Select
Dynamically Generated
from the
Certificate Distribution
dropdown list.
Source:
Select the standalone certificate you created.
Signature Algorithm:
Select
SHA256 with RSA
.
Subject
:
emailAddress: ${userEmailAddress}
CN: ${userEmailAddress}
OU: <Tenant OU from the Netskope UI>
O: <Organization Name from the Netskope UI>
L: <Your city>
ST: <Your state> (in two letter format)
C: <Your country> (in two letter format)
Subject Alternate Name Type
: (Optional)
Key Size
: 2048
Save the configuration and distribute the certificate to the relevant devices.
Here’s an example of an identify certificate configuration:
Netskope Client Distribution
Administrators can manage and distribute public, in-house, and AppConnect-enabled iOS applications.
To add an application:
Navigate to
Apps
>
App Catalog
and search for “
Netskope
”.
Click
Netskope Client for iOS
.
This opens the Netskope Client application details.
Click the
Distribution
tab.
In
App Distribution
, assign the app to the appropriate
Users
and
Device Groups
.
Click the
App Configurations
tab
.
Click
+
for
Install on device
.
In
Configuration Setup
, enter a configuration name in the
Name
field.
Toggle
ON
to select the
Device Installation Configurations
option.
Click the radio-button to select
Require installation on device
.
Select the checkbox for
Enable
MDM App Auto-Updates
.
Assign the app to the appropriate
User
and/or
Device Group
.
Click
Save
.
Provision Netskope Certificates to Devices
To provision Netskope certificates to devices:
Locate the
Netskope Root certificate
you downloaded from the Netskope UI (
Settings > Security Cloud Platform > Netskope Client > MDM Distribution
).
In the
MobileIron Cloud
admin console, select
Configurations
, and click
Add
.
Select
Certificate
, enter a name, and upload the
Netskope Root certificate
.
Distribute the certificate configuration to the relevant devices.
Create VPN Profile
Administrators must select the preferred VPN profile type according to their requirement. There are options to use either On-Demand VPN or Per App VPN. Netskope Client does not allow coexistence of multiple VPN profiles on the same device. You can create multiple VPN profiles in the Workspace One  console and assign them to various smart groups to accommodate corporate and BYOD use cases.
Configure On-Demand VPN
To configure an On-Demand VPN:
In the
MobileIron Cloud
admin console, select
Configurations
, and click
Add
.
Select
VPN On-Demand
.
Enter the following parameters:
Name:
Enter a unique name.
Connection Type:
Custom SSL
Identifier:
com.netskope.Netskope
Server:
gateway-[tenant].goskope.com.
Account:
Leave blank.
Custom Data:
OrgKey: Use the tenant organizational key
AddonHost: Use the addon URL for the tenant: addon-<tenant-URL>.
UserEmail: Use the variable that contains the user identity for the enrolment:
${userEmailAddress}
.
enrollauthtoken: Use Secure Enrollment Authentication token.
enrollencryptiontoken: Use Secure Enrollment Encryption token.
Use enrollauthtoken and enrollencryptiontoken only if you have enabled secure enrollment in your tenant.
User Authentication:
Certificate.
Credential:
Select the identity certificate you created.
Proxy Setup:
None
Enable VPN On Demand:
On
Enable iOS Rules:
Selected
Choose whether to apply this configuration to
All Devices
,
No Devices
, or
Custom
to specify target devices.
When finished, click
Done
.
Configure Per-App VPN
By default all Netskope tenants are set to On-Demand iOS VPN. If you want to use the Per-App iOS VPN profile, contact your sales rep, professional services rep, customer success manager, or Support to have Per-App VPN enabled.
To configure a Per-App VPN:
In the
MobileIron Cloud
admin console, select
Configurations
, and click
Add
.
Select
Per-App VPN
.
Enter the following parameters:
Connection Type:
Custom SSL
Identifier:
com.netskope.Netskope
Server:
gateway-[tenant].goskope.com (for example, gateway-nsclientauto02.goskope.com)
Account:
Leave blank.
Custom Data:
OrgKey
: Use the tenant organizational key
AddonHost
: Use the addon URL for the tenant: addon-<tenant-URL>.
UserEmail
: Use the variable that contains the user identity for the enrolment:
${EmailAddress}
enrollauthtoken
: Use the Secure Enrollment Authentication token.
enrollencryptiontoken
: Use the Secure Enrollment Encryption token.
Use enrollauthtoken and enrollencryptiontoken only if you have enabled secure enrollment in your tenant.
User Authentication:
Select
Certificate
.
Credential:
Select the identity certificate you created.
Proxy Setup:
None
Enable VPN On Demand:
On
Enable iOS Rules:
On
On Demand Match App Enabled:
On
Provider Type:
packet-tunnel
When finished, click
Save
.
Select Apps for the Per-App VPN
To select apps for the Per-App VPN:
In the
MobileIron Cloud
admin console, select
Apps
, and click
Add
.
Select
App Catalog
to open the wizard and choose the apps to distribute to devices
Select
App Configurations
, and then select
Per-App VPN
.
Enter the following parameters:
Name
: Enter a name.
Enable Per-App VPN for this App
: Select On
Dropdown list
: Select the
Per-App VPN
configuration you created.
When finished, click
Save
.
Distribute to Devices
To validate that the device has the necessary configurations:
In the
MobileIron Cloud
admin console, select
Devices
.
Force a device check-in.
Select
Configurations
to view the device details.
iOS VPN Fail Open
The
Fail Open
feature allows iOS devices using VPN to temporarily bypass Netskope and connect directly to an app or service.
When
Fail Open
is enabled, iOS devices will not steer traffic through Netskope until the service resumes or the feature is manually disabled.
This function is useful during service interruptions or planned maintenance.
To enable fail open for iOS VPN:
In the
Netskope UI
, go to
Settings > Security Cloud Platform > MDM Distribution
.
In the Create VPN Configuration section, confirm that your iOS VPN is operational. If it is, click the
(
settings
) icon to open the
Advanced Configuration
dialog box.
Enable
the toggle and then click
Save.
In this Topic
Deploy Client on iOS Using Ivanti Neurons

---
## Deploy Client on Android Using Ivanti Neurons
**URL:** https://docs.netskope.com/en/deploy-client-on-android-using-ivanti-neurons/
**Last Modified:** 2025-08-31T01:48:41+00:00
**Scraped:** 2026-06-26T09:26:27.596846+00:00

Deploy Client on Android Using Ivanti Neurons
This topic describes the instructions to deploy Netskope Client on Android devices using Ivanti Neurons(formerly known as MobileIron Cloud).
Non-Zero Touch Deployment With Ivanti Neuron
Netskope supports two methods prescribed by MobileIron to enable Android Enterprise devices in Ivanti Neurons:
Using Managed Google Accounts.
Using Managed Google Play Accounts (Recommended method).
Managed Google Accounts
To use Android Managed Configurations in Ivanti Neurons, first set up Android for Work in Google. After Android for Work is configured, copy the MDM token from
admin.google.com
and .json file generated from
console.developer.google.com
. When you have these, follow these instructions.
To configure Android Managed Configurations in Ivanti Neurons:
Log in to your Ivanti Neurons Admin Portal.
Click
Admin
in the top menu bar, and then click
Android Enterprise
in the left nav panel.
In the Android Enterprise window:
Enter the MDM token generated from admin.google.com.
Enter the domain for your google account.
Upload the .json file from console.developer.google.com.
Click
Connect
, and then authorize the G Suite account.
Click
Users
in the top menu bar, and then click +
Add > Single User
.
Create a new user with the domain used for Android Enterprise above, and then enable Google Sync for the user.
Click
Apps
.
On the App Catalog page, click
Add+
.
Enter
Netskope
in the Find Apps field.
Select
Netskope Client
, and then enter these values:
User Email Address: ${userEmailAddress}
Host: addon-<tenant-URL>.
Token: <OrgKey>. Use the Organization ID from the VPN Configuration section in the Netskope UI for the OrgKey value (Settings > Security Cloud Platform > Netskope Client > MDM Distribution).
enrollencryptiontoken: Enter the enrollment encryption token
enrollauthtoken: Enter the enrollment authentication token
Use
enrollauthtoken
and
enrollencryptiontoken
if only secure enrollment is enabled for your tenant.
Click
Done
and then click
Publish
.
Managed Google Play Accounts
To use Android Enterprise devices in Ivanti Neurons, first setup a Managed Google Play account.
Prerequisite:
Register your Android enterprise in Ivanti Neurons through Managed Google Play Accounts. To learn more, view
Ivanti Neurons
.
Environment
Netskope Client Playstore Version: 96.0.0.1009
Android Enterprise Modes
Android enterprise devices enabled in Ivanti Neurons supports one of the following device modes:
Work Managed Device (Company Owned)
Work Profile (BYOD)
Managed Device with Work Profile (Company owned personally enabled devices)
To learn more, view
Device Modes
.
Netskope supports the Work Profile (BYOD) variant of the Android Enterprise and you can modify the default configuration to only apply to select device groups- for instance a subset of Android devices.
Deploying Android Applications
Perform the following steps to deploy your Android applications:
Go to
Apps
>
App Catalog
.
Click the
+Add
.
Select
Google Play
.
Search and select
Netskope Client
.
Add Netskope configuration.
Enter User Email Address and {EmailAddress} for the Configuration Key and Configuration Value, respectively.Enter token and your
<Orgkey>
value (Organization ID in the Netkkope UI) for the Configuration Key and Configuration Value, respectively. Enter host and the addon-
< tenant-URL>
value for the Configuration Key and Configuration Value, respectively.
Click
Approve
.
To learn more, view
Android Enterprise
.
Perform the following to setup BYOD with the work profile:
Download and Install the Mobileiron Go app from Playstore.
Open the MobileIron Go app and select CONTINUE.
Enter in the username and password.
Select
CONTINUE
again to create the Work Profile.
Accept the Terms and Conditions.
Select
SET UP
.
Wait for the profile to finish set up.
The application will restart and the MobileIron Go application will be moved to the Work Profile.
Select
FINISH
to complete the setup.
The device is now fully registered and configured with Android For Work.
Zero-Touch Deployment With Ivanti Neurons
This section describes the steps for a silent deployment of Netskope Client for Android without any user action using a VPN profile.
Prerequisites
On the Netskope UI, go to
Settings
>
Manage
>
Certificates
. Here, click the Signing CA tab to download the Netskope Root and Intermediate Certificate.
On the same page locate and save Organization ID token value.
User accounts provisioned within the MDM/EMM platform must match with those provisioned with the Netskope tenant.
Create a Trusted Netskope Root Certificate Profile
To create a Netskope root certificate profile:
On the Ivanti UI, from the left-pane, click
Configurations
.
In
Configurations
, click
+Add
.
Click
Certificate
. Or you can search for
Certificate
in the Search Configurations text-box.
It opens the
Create Certificate Configuration
window.
In
Create Settings
, perform the following actions:
Enter the configuration Name.
Upload the root certificate in
Configuration Setup
.
Click
Next
.
In
Distribute
, click to select the checkbox for
Enable this configuration
.
Perform appropriate assignments to the User and/or Device group.
Click
Done
.
Repeat the same steps to upload Netskope Intermediate Certificate.
Add Netskope Client
To add Netskope Client for Android:
On the left-pane, go to
Apps
>
Apps Catalog
.
Search for
Netskope
in the text-box.
Click
Netskope Client
for
Android
.
In Netskope Client, click
Distribution
.
Perform appropriate assignments to the User and/or Device group.
Click
App configurations
.
Click
Managed Configurations for Android
.
Click
Add
.
Enter the configuration name.
Under Managed Configurations, click to select the option
Block the user from uninstalling the app
.
Expand
Managed Configurations
and enter the following configuration values:
User Email Address:
${userEmailAddress}
Host:
addon-[tenant].goskope.com
Token:
<organization ID>. Retrieve Organization ID token value from your Netskope tenant.
enrollencryptiontoken:
Enter the enrollment encryption token.
enrollauthtoken:
Enter the enrollment authentication token.
Use
enrollauthtoken
and
enrollencryptiontoken
if only secure enrollment is enabled for your tenant.
In
Distribute this App Config
, Perform appropriate assignments to User and/or Device group.
Click
Save
.
Add VPN Profile Configuration
To achieve Zero-touch deployment, it is imperative to add a VPN profile that is tied to Netskope Client.
To create a VPN Profile:
On the Ivanti UI, from the left-pane, click
Configurations
.
In Configurations, click
+Add
.
Search for
VPN
in the Search Configurations text-box.
Click
Always On VPN
.
This opens
Create Always On VPN Configuration
.
In
Create Settings
, enter a Profile Name.
In
Select OS
, click
Android
.
It opens the
Configuration Settings
section.
In
Select App,
click the
Select Manually
tab.
Enter the package name:
com.netskope.netskopeclient
.
Click
Select App
.
After you click
Select App
, you can view Netskope client details in the
Selected App Details
tab.
Click
Next
.
Perform appropriate assignments to the User and/or Device group.
Click
Save
.
Device Classification for Android
You can classify Android devices based on these criteria:
Minimum OS version
Passcode required
Device not compromised
Primary storage encrypted
Managed configuration
Go to
Settings > Manage > Device Classification
and select
Android
on the New Device Classification dropdown list, and then follow these steps to classify your Android device. Select options and enter the requested parameters.
Rule Name: Enter a name for this classification rule.
Classification Criteria: Select an
Any
or
All
criteria match.
Minimum OS Version: Select an OS version from the dropdown list or create a custom OS version.
Passcode Required: No parameters required.
Device Not Compromised: No parameters required.
Primary Storage Encrypted: No parameters required.
Managed Configuration: If you already added a managed configuration for this device on the MDM Distribution page, the key-value pair is shown here. This key-value pair is sent from the MDM to the device so the Netskope app can validate the key-value pair and mark it as Managed or Unmanaged. To regenerate the key-value pair, click
Regenerate
.
Note
Managed Configuration does not work when an app is installed on an Android device using the onboarding email or with the AirWatch SDK.
When finished, click
Save
.
After creating a device classification rule, you can use it in a Real-time Protection policy.
To use this Device Classification in a Real-time Protection policy, click
Policies > Real-time Protection
in the Netskope UI. Select an existing policy or click
New Policy
and choose a policy type.
Proceed through the Users, Cloud Apps + Web, DLP/Threat Protection, and Select Activities sections.
For Additional Attributes, click
Access Method
and select either
Client
,
Mobile Profile
, or
Reverse Proxy
, and then click
Save
. Click
Device Classification
, and then select
Managed
or
Unmanaged
, based on the devices you just classified.
Managed
means the device is managed; the device information sent by the Client matches at least one of the device classification checks configured for that Client’s OS.
Unmanaged
means the device is unmanaged; the device information sent by the Client matches none of the device classification checks configured for that Client’s OS.
When finished, click
Save
and then
Next
.
Combine device classification with other policy elements, like using the Block Action for specified applications for activities like uploading files from managed or unmanaged devices. Finish creating or updating this policy to establish this device classification. Click
Apply Changes
for this policy.
After the policy has been created, perform the process for which the policy was created. Next, go to
Skope IT > Application Events
and click the magnifying icon for an event to open the Application Event Details panel. In the User section you’ll see a Device Classification field, which shows one of these device classifications.
In this Topic
Deploy Client on Android Using Ivanti Neurons
Deploy Client on Android Using Ivanti Neurons - Netskope Knowledge Portal

---
## Deploy Client on macOS Using Ivanti Neurons
**URL:** https://docs.netskope.com/en/deploy-client-on-macos-using-ivanti-neurons/
**Last Modified:** 2026-04-06T12:05:48+00:00
**Scraped:** 2026-06-26T09:26:28.730266+00:00

Deploy Client on macOS Using Ivanti Neurons - Netskope Knowledge Portal
Deploy Client on macOS Using Ivanti Neurons
This topic describes the procedure to configure Ivanti Neurons (formerly known as MobileIron Cloud) for macOS.
Prerequisites
Download Netskope Root and Intermediate certificates and convert them to .cer extension. To learn more, see
Certificates
.
Download MobileIron Packager (MIP) from the
MobileIron Support
portal. To install MIP, install the MobileIron Packager (MIP) app and then download the Netskope agent .pkg file. Upload the Netskope package in the tool to convert it to .mip.
Create Script for App Deployment
You can create your scripts in the All Scripts section. Netskope Client use the instructions held in the script to enroll the user to a device.
Perform the following steps to create the script:
Go to
Admin
>
Scripts
>
All Scripts
.
Click
Add
to create the Installation Script.
Enter the
Script Name
,
Description
, and select
Script Type
as ‘bash’.
Click
On Import code from script
and upload the  minsclientconfiig_<version-number>.sh script.
Click
Add
in Script Input to define the Input Environmental Variables.
Provide the
Environment Variable Name
and
Environment Default value
.
To include secure enrollment tokens, add the two additional parameters while adding the script in
Environment Variable Default Value
:
enrollauthtoken
and
enrollencryptiontoken
.
Click
Save
.
MacOS Configuration Script for Installation
Here, you can define a configuration to distribute the script to the end-user device.
Go to
Configuration
>
Add
>
Search
and select Mobile@Work for macOS Script.
Enter
Name
and select your script in the Configuration Setup.
After the script Execution select
Execute Once On Deployment
.
Click
Next
.
Select the Device/Users/Custom.
Adding Netskope App in App Catalog
Adding the Netskope application to Omnissa Workspace ONE for deployment in the mac Device.
Go to
Apps
>
App Catalog
.
Click
Add
.
Select
In-house
app.
In the
Choose
section, upload .mip netskope client pkg
Click
Next
. Ensure the file upload is successful.
In the
Describe
section, ensure to update the Package ID as.com.netskope.client.Netskope-Client when importing Packager in-house macOS apps and click Next.
In the
Scripts
section, define or select the application scripts.
Pre Install Scripts – Enter the script name to select the script to run before app installation. The preinstall scripts execute or rerun until the script execution success status is received from the client. Once the script execution is completed, the app install command is sent. You can view the script run status in the device details page in the Logs tab.
Uninstall Scripts: Enter the script name that server sends to a device when it detects an app that  is no longer distributed to the device.
Select the desired options in
Add Screenshots
,
Delegate
, and
Distribute
sections.
In the
App configuration
section, click Install Application configuration settings and  toggle on
Install on Device
and select
High
from the
Set App install Priority
dropdown menu.
Click
Done
.
Approve Network Extension
System Extension configuration allows installation of extension types like Driver Extension, Network Extension and Endpoint Security Extension, without kernel-level access.
Go to
Configuration
>
Add Configuration
>
Search
for ‘MacOS System Extensions.
Under
Allowed System Extension
s
, add
Allowed Team Identifiers
and
Allowed System Extensions
.
Add
Network Extension Team ID:
24W52P9M7W.
Click
Add
to add the following System Extension:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Also provide the same details in Remove System Extensions.
Select the
Allow user overrides
option.
Click
Next
.
Associate to Device/Users/Custom.
Pre-Approve Full Disk Access Permission For macOS
The Netskope Client on macOS requires Full Disk Access permissions for various foundational functionalities. The following configuration pre-approves these permissions and suppresses end-user notifications requesting approval. To learn more, view
macOS System Extension configuration
.
Go to
Configurations
from the left pane.
Click
+Add
.
Search and select
Privacy Preference
.
In
Create Privacy Preference Configuration
:
Enter
Name
of the configuration.
Under
Configuration Setup
go to
System Policy (All Files)
.
Click
Actions > Add
.
Under
Identity Dictionary Key
:
Enter
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
in
Identifier
.
Select
Bundle ID
in
Identifier Type
.
Enter the following anchor apple generic and identifier in Code Requirement.
"com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
Select
Allowed
.
Click
Save
.
Select
Next
.
In
Create Privacy Preference Configuration
, select the following:
Select
Custom
.
Select
Users/User Groups
or
Devices/Devices Groups
.
Select respective options based on selection.
Click
Done
.
Onboarding macOS device with Ivanti Neurons
Perform the following steps to onboard the macoS device:
Click
Getting Started
in the Welcome email to Onboard your endpoint.
Enter the
Email
and
password
.
Choose one of the following options:
I own the Device.
Company owns the Device.
Install the MDM Profile.
Verify the app installation process in the ‘install.log’ file.
Enter the IDP login details such as email address.
In this Topic
Deploy Client on macOS Using Ivanti Neurons

---
## Deploy Client on iOS Using IBM MaaS360
**URL:** https://docs.netskope.com/en/deploy-client-on-ios-using-ibm-maas360/
**Last Modified:** 2025-08-31T01:48:35+00:00
**Scraped:** 2026-06-26T09:27:38.767261+00:00

Deploy Client on iOS Using IBM MaaS360 - Netskope Knowledge Portal
Deploy Client on iOS Using IBM MaaS360
This topic covers the steps to deploy Netskope Client for iOS mobile devices using IBM MaaS360.
Prerequisites
In the Netskope UI, go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distributio
n. Download the Netskope Root Certificate and Intermediate certificates. These are needed to configure IBM MaaS360 certificate profiles.
In the MDM Distribution page, scroll down to
Create VPN Configuration
section to find your
Organization ID
.
User accounts provisioned within the MDM/EMM platform must match with those provisioned with the Netskope tenant.
Setting up Netskope Client
Setting up Netskope Client for  iOS devices with IBM MaaS360 includes the following mandatory steps:
Deployment of  Trusted Root Netskope Certificate Profile
To upload the Intermediate and Root certificates:
In the IBM MaaS360 console, go to
Security
>
Policy
.
Click
Add Policy.
Or, you can also edit an existing policy.
Provide the following details:
Name: Enter a policy name
Type: iOS MDM
Start From: Business Templates Based Policies
Business Use Case: Select an appropriate one. For example, BYOD.
Click
Continue
.
It navigates to the policy page where you can configure settings, add assignments, and review changes.
Expand
Advanced Settings
under
Configure Settings
.
Click
Certificates
.
Click
Edit
at the top-right corner of your screen.
Select the checkbox for
Configure Trust or Credential Certificates on the Device
.
Click
Trust or CA Certificates
>
Netskope Root Certificate
.
Provide the certificate name.
Click
+
icon to upload Netskope Root certificate.
Click
Save
.
Click the refresh icon on the right and select the uploaded certificate name from the dropdown.
Repeat the process for uploading and selecting the Intermediate certificate.
Assign the appropriate policies to user/device groups and click
Next
.
Review the policy.
Click
Publish
.
Push VPN Profile Configuration
To provide a seamless Netskope Client deployment in IBM MaaS360, you need to create a VPN profile controlled through security policies. You can either create a new security policy or a VPN profile to an existing policy. To learn more, view
Create Security Policy
.
To add a VPN profile in a security policy:
In the IBM MaaS360 console, go to
Security
>
Policy
.
Select an existing policy.
The policy details page is displayed.
From
Configure Settings
>
Device Settings
, select
VPN
.
Click
Edit
at the top-right of your screen to configure the settings.
Select Custom SSL from the list of dropdown options.
Enter a VPN Connection Name and provide the configuration details:
Identifier: com.netskope.Netskope
Host Name of the VPN Server: gateway-<tenant>.goskope.com
User Authentication Type: Select Password.
VPN on Demand Dictionary Rule: OnDemandEnabled
Custom Data 1: OrgKey=<ORG-ID TOKEN>
Custom Data 2: AddonHost=addon-<TENANT>.goskope.com
Custom Data 3: UserEmail=%email%
Custom Data 4: ForcedDisabledSteering=true
Add Custom Data 4 if the deployment requires NPA only traffic steering.
Bundle Identifier: com.netskope.Netskope
Assign the appropriate policies to user/device groups and click
Next
.
Review the policy.
Click
Publish
.
Add Security Policy
The following section describes the steps to add appropriate iOS policies in the IBM MaaS360 console.
To add a security policy:
Go to
Devices
>
Groups
.
Choose the desired policy and click
More
..
Click
Change Policy
.
Select an appropriate iOS policy from the list of dropdown items.
Click
Submit
.
Add Netskope Client App
The following section describes the steps to add the application from iTunes App in the IBM MaaS360 console.
To add Netskope Client:
In the IBM MaaS360 console, go to
Apps
>
Catalog
.
In the
App Catalog
page, click
Add
>
iOS
>
iTunes App Store App
.
The iTunes App Store App window is displayed. In the App field, search for Netskope Client.
Click the Netskope Client app to select.
Click
Add
to add Netskope Client to the App Catalog.
Distribute and Assignment
This section describes the steps to distribute and assign Netskope Client app to devices in a group after adding NS Client to the App Catalog. To learn more, view
Deploy Apps to Devices
.
To distribute and assign NS Client:
In the
App Catalog
page, click Netskope Client.
On the top-right corner of the Netskope Client app page, click
Distribute
.
In
Distribute App: Netskope Client
, make an assignment to the appropriate group.
Click
Distribute
.
In this Topic
Deploy Client on iOS Using IBM MaaS360

---
## Deploy Client on iOS Using Kandji
**URL:** https://docs.netskope.com/en/deploy-client-on-ios-using-kandji/
**Last Modified:** 2025-08-31T01:48:34+00:00
**Scraped:** 2026-06-26T09:27:41.012260+00:00

Deploy Client on iOS Using Kandji - Netskope Knowledge Portal
Deploy Client on iOS Using Kandji
This document  illustrates the procedure to deploy Netskope Client on iOS devices and this process ensures reduced user interaction while deploying tenant certificates, system and network extensions.
Deployment Prerequisites
In the Netskope UI, go to
Settings
>
Manage
>
Certificates
>
Signing CA
. Download the
Netskope Root
and
Intermediate
Certificate
.
Convert the downloaded certificates to .cer format by renaming the .pem files to .cer.
In the Netskope UI, go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM
, locate and save
Organization ID
token value.
Download
AppVPN Proxy Script for iOS Kandji.mobileconfig
from Netskope Support.
Before you upload the .mobileconfig file, perform the following modifications in the downloaded script:
– Lines 48 and 57: Provide addon host name associated with Netskope tenant. For example, addon-example.goskope.com.
– Line 59: Provide the Organization ID token value mentioned in prerequisites.
– Line 61: Replace Kandji variable
$EMAIL
with the user email address. For spot tests and kiosk type deployments, replace this value with static e-mail provisioned at Netskope tenants.
– Line 63: Secure Enrollment auth token.
– Line 65: Secure Enrollment encryption token.
Administrator access to Kandji.
Administrator access to Netskope.
Upload Netskope Certificates to Kandji
To upload certificates to Kandji:
It is mandatory to upload the Netskope Root Certificate and Netskope Intermediate Certificate.
Login to
Kandji
and go to
Library
>
Add New
.
Select
Profiles
from the dropdown menu.
Click
Certificate
>
Add and Configure.
Upload
Netskope Root Certificate
(.cer format).
Enter a name for this certificate. For example: Netskope Root Certificate.
In
Assignment
,  select the required blueprints and limit installation to iPhone and iPad.
In
Settings
, select
Certificate type
as PKCS#1-formatted certificate.
Drag and drop the .cer certificate in the upload box.
Click
Save
.
Repeat this step to upload the
Netskope tenant Intermediate Certificate
. When uploading, give a name, for example, Netskope Tenant Certificate.
Netskope Client Distribution
Login to Kandji and click
Library
.
Select Auto App and search for
Netskope Client
.
Click the
Netskope Client
app.
In
Assignment
, select the required
Blueprints
and limit installation to iPhone and iPad.
In
Settings
, ensure the
Installation
dropdown setting is set to
Install and Continuously Enforce
.
Click
Save
.
Upload VPN Configuration to Kandji
Netskope client requires user identity information to enroll and provide user attribution during its operation. Kandji provides this user identity information and Netskope Client uses it as a variable that results in a fully transparent SSO experience.
To upload the script to Kandji:
Go to
Library
>
Add New
>
Custom Profile
.
Click
Add and Configure
.
Select the required
Blueprint
.
In
Install On
, limit the installation to iPhone and iOS.
Under
Settings
, upload the
.mobileconfig
file that you downloaded from the Netskope Support.
Click
Save
.
You can attempt to generate traffic after the device enrollment is complete according to the configured Blueprint and the applications get distributed. Netskope Client self enrolls and enables connectivity for all mobile apps on the device according to the Netskope
Steering Configuration
.
In this Topic
Deploy Client on iOS Using Kandji

---
## Netskope Client Resource Utilization
**URL:** https://docs.netskope.com/en/netskope-client-resource-utilization/
**Last Modified:** 2025-08-31T01:48:06+00:00
**Scraped:** 2026-06-26T09:27:57.875533+00:00

Netskope Client Resource Utilization - Netskope Knowledge Portal
Netskope Client Resource Utilization
The Netskope Client is designed as a lightweight agent providing operability across a diverse set of operating systems (OS). Its core functionality encompassing traffic interception and processing, necessitates the utilization of system resources, including CPU, memory, disk space, and device power (battery).
The following table provides general guidance on the resource utilization of Netskope Client on supported operating systems:
The values in the following table are for guidance and the actual results may vary.
Operating System
CPU Utilization (Range)
Battery Utilization (Range)
Disk Space
Memory
Notes
Windows and macOS
0 - 5 %
Not Applicable
~100 MB for installation
~50 MB for Log and Configuration
Between 100 - 150 MB
Log retention space might vary depending on the level of logging.
CPU utilization can vary with the traffic processing.
Linux
~45 MB for installation, log and configuration storage
~0.5 %
Android, iOS, and ChromeOS
Not Applicable
10 - 20 %
iOS and Android:
~20 MB for installation
ChromeOS:
~35 MB for installation
Between 4 - 12 MB for Log and configuration storage.
-
Log retention space might vary depending on the level of logging.
Battery utilization can increase intermittently when the Client is processing traffic.
It is important to note that other external factors can affect battery life of mobile devices. For example, battery drain due to poor cellular network.
For mobile devices, Netskope Client uses cellular data when the device is not connected to Wifi.
For measuring the network performance of Netskope Client, view
Netskope Performance Troubleshooting Guide
.
In this Topic
Netskope Client Resource Utilization

---
## Deploy Netskope Client In Restricted Regions
**URL:** https://docs.netskope.com/en/deploy-netskope-client-in-restricted-regions/
**Last Modified:** 2025-08-31T01:48:35+00:00
**Scraped:** 2026-06-26T09:28:26.069781+00:00

Deploy Netskope Client In Restricted Regions - Netskope Knowledge Portal
Deploy Netskope Client In Restricted Regions
If an administrator wants to deploy Netskope Client in regions where Google Play Store or Apple App Store is not available or Netskope is unable to publish Netskope client, such as China, Netskope recommends performing certain custom configurations. These limitations prevent users from downloading Netskope Client from App stores.
This section mainly lists down the options that the administrators or end-users can leverage to deploy Netskope Client and enroll users located in these regions.
Deploy Netskope Client For iOS In Restricted Regions
Deploy Netskope Client For Android In Restricted Regions
In this Topic
Deploy Netskope Client In Restricted Regions

---
## Deploy Netskope Client For iOS In Restricted Regions
**URL:** https://docs.netskope.com/en/deploy-netskope-client-for-ios-in-restricted-regions/
**Last Modified:** 2025-08-31T01:48:36+00:00
**Scraped:** 2026-06-26T09:28:27.187325+00:00

Deploy Netskope Client For iOS In Restricted Regions - Netskope Knowledge Portal
Deploy Netskope Client For iOS In Restricted Regions
This document describes the various methods to deploy Netskope Client using MDM in restricted regions.
The admin can choose one of the following options:
Using Volume Purchase Program (VPP)
Apple Developer Enterprise Program (ADEP)
Option 1: Deployment Using Volume Purchase Program (VPP)
Prerequisites
Ensure that
Apple Business Manager
(ABM) is linked with Mobile Device Management (MDM).
This method can be used if the ABM account is from a non-restricted region. Go to
Preferences
>
Organization Information
to verify the region of the ABM account.
Deployment Procedure
Configuration in Apple Business Manager
Perform the following steps to initiate a purchase in ABM:
Login to
Apple Business Manager
.
Go to
Apps and Books
.
Search for Netskope Client.
Initiate a purchase depending on the number of users.
You need not pay any amount during the purchase as the Price reflects 0.
Configuration in Microsoft Intune
After you make the purchase in Apple Business Manager, check for the Netskope Client app in  Microsoft Intune MDM.
In Microsoft Intune, go to
Apps
>
iOS/iPadOS
.
Search for
Netskope Client
app with
Type
as iOS volume purchase program app as the Client app was synchronized from Apple Business Manager.
Once this is complete, you can
distribute
the Netskope Client app to the users in the restricted region.
Option 2: Deployment Using Apple Developer Enterprise Program (ADEP)
Using this option, large organizations can develop and deploy proprietary applications for their employees. This option is mostly applicable for cases that require private distribution directly to employees using secure internal systems or through a Mobile Device Management (MDM) solution.
Deployment Procedure
Invite one of Netskope developers to your team in a developer role.
The admin needs to create provisioning profiles.
Netskope provides xcharchive file.
This method is safe since there is no need to share any signing certificates – developer cert is produced by Apple just for the developer(invited) and can be used only on certain devices under full control of the Enterprise account holder.
The admin can now sign the application and distribute with their preferred method such as MDM or any other methods already being utilized.
In this Topic
Deploy Netskope Client For iOS In Restricted Regions

---
## Deploy Netskope Client For Android In Restricted Regions
**URL:** https://docs.netskope.com/en/deploy-netskope-client-for-android-in-restricted-regions/
**Last Modified:** 2025-11-26T04:25:40+00:00
**Scraped:** 2026-06-26T09:28:28.314647+00:00

Deploy Netskope Client For Android In Restricted Regions - Netskope Knowledge Portal
Deploy Netskope Client For Android In Restricted Regions
This document describes the various methods to deploy Netskope Client in restricted regions. The admin can choose one of the following options:
Deployment by hosting the APK file in a company drive.
Deployment using Microsoft Intune MDM.
Option 1: Deployment By Hosting APK File In Company Drive
Step 1: Admin can host the Android APK file in company drive.
Using this option, the admin can host the Android APK file in a company drive from where users can download and install the software.
To host the APK file:
Go to the
Netskope Support
portal.
Download the APK file for Android provided under the
Latest Golden Release
.
Upload it to your company drive.
Step 2: Send Email Invite to the end-users.
Using this option, the admin can create a template for sending an email to the end-users on the Netskope webUI.
In Netskope tenant webUI, go to
Settings
>
Tools
>
Templates
.
Edit the
Email Invitation
template.  Refer to the sample email invite template provided under the heading “
Sample Email Invite Template
“.
Go to
Settings
>
Security Cloud Platform
>
Users
.
Click
Send Invitation
.
To learn more, view:
Email Invite
.
Sample Email Invite Template
<div>
	    <p>Welcome,</p>
	    <p>{{NS_ADMINEMAIL}} at {{NS_ORGNAME}} has requested this message be sent to you.</p>
{{NS_ORGNAME}} is using a new solution that enables you to securely use various cloud based apps to further increase your productivity.
</div>
<div>
	    <p>Please follow the link below and the security system will be automatically applied. Each type of device requires the proper Client. Please install the correct Client type for your device.</p>
	    <p><a href="{{NS_MACADDON}}">macOS Client</a></p>
	    <p><a href="{{NS_WINADDON}}">Windows Client</a></p>
	    <p><a href="{{NS_IOSPROFILE}}">iOS Profile</a></p>
	    <p><a href="{{NS_ANDROIDCLIENT}}">Android Client</a></p>
<p>Users in restricted regions can download the Netskope Client from here: <a href=<your Drive Location>>Android Client</a></p>
<div style="{{NS_IOSCLIENT_FLAG}}">
		<p><a href="{{NS_IOSCLIENT}}">{{IOSCLIENT_TEXT}}</a></p>
	    </div>
	    <div style="{display: block}">
		<p><a href="{{NS_LINUXADDON}}">Linux Client</a></p>
	    </div>
</div><div>
	       <p>If you have any concerns about this communication, please contact your administrator directly either via email or phone.
</p>
<p>Please note that this invitation can only be used by you and will not be usable by other users. In case, someone else in the organization needs this service, just let us know and we will get additional invitations sent out to the relevant folks. Thank You.
    </p>
	    <p>----------------------------</p>
	    <p>Detailed Instructions:</p>
<p>Each of these installers will apply the Netskope Client to your system. The Netskope Client will secure your access to all of your cloud apps.
</p>
</div>
<div>
	    <p>If at any time you have any issues or questions do not hesitate to email <a href="mailto:support@netskope.com">Netskope Support</a></p>
	    <p>- Netskope Team</p></div>
The drive location must be the place where the admin decides to host the APK file.
Step 3: End-user can download and install Netskope Client.
End-users can now Install the Client application and enroll.
Option 2: Deployment Using Microsoft Intune MDM
Prerequisites
Download the APK file from the
Netskope Support Portal
.
Install Netskope Client
To install the Netskope Client:
In the
MS Endpoint Manager admin
console, go to
Apps
>
All Apps
.
Click
Android
.
Click
+Add
.
From
Select app type
, choose
Line-of-business app
.
Click
Select
.
This navigates to the
Add App
screen.
Under
App information
, select an app package file in
Select File
.
In
App Package file
, upload the package file.
Click
OK
.
After you click OK, enter the following details:
Publisher: Enter Netskope.
Targeted Platform: Select Android device administrator.
Minimum Operating System: Select Android 9.0(Pie).
Click
Next
.
Under
Assignments
, select the user groups or users to which the app is to be deployed in the
Required
section (options
+Add group
, +Add all users,
+Add all devices
).
Click
Next
.
Under
Review and Create
, validate the configured details.
Click
Create
.
The created app is displayed in the Android Apps page.
To learn more, view
Add an Android line-of-business app to Microsoft Intune
.
User Enrollment
User Enrollment with Email Invite
To send an email invite:
Go to
Settings
>
Security Cloud Platform
>
Users
.
Click
Send Invitation
.
Once the application is deployed on devices, do not open the app. Otherwise, Netskope Client goes into IDP mode.
Click the
Android Client
link in the email and then select
Download Android Configurations
.
User Enrollment By Manually Entering Credentials
Netskope Admin would have to supply the tenant URL to the end users.
After entering the tenant URL, users would be presented with the IDP page where they have to enter the login credentials.
IDP enrollment fails if
Secure Enrollment
is enabled.
In this Topic
Deploy Netskope Client For Android In Restricted Regions

---
## Deploy Client on MacOS Using Jamf Pro
**URL:** https://docs.netskope.com/en/deploy-client-on-macos-using-jamf-pro/
**Last Modified:** 2026-04-10T07:11:37+00:00
**Scraped:** 2026-06-26T09:28:40.538115+00:00

Deploy Client on MacOS Using Jamf Pro
Jamf Pro is an enterprise mobility management tool that manages endpoints for Apple iOS and macOS devices. This article provides instructions to install the Netskope Client on MacOS devices using Jamf Pro.
Prerequisites
Administrators must possess proficient working knowledge of Jamf Pro.
Administrators must review
Netskope Client Client Enrollment Methods
to understand the Client User Enrollment methods available for their environment.
Import users into the Netskope tenant – see
Provisioning Users for Netskope Client
.
Download
Netskope Root and Tenant Certificates
and ensure the certificates are available when needed.
See
Deploy Netskope Client via IdP
when using IDP as the method of user enrollment.
For a PLIST user enrollment method:
Jamf must have a pre-existing user (email) to device mapping.
Jamf Pro with push enabled.
JAMF Pro entry for computers must have an email field available for all computers in scope.
Download the latest JAMF scripts (JAMFScripts.zip) from the
Netskope Support
portal. This downloads a file JAMFScript_v22_Nov2024 that contains two files:
jamfuninstall.sh
nsclientconfig.sh – Use this file while adding script.
Supported Platforms and Enrollment Methods
This article outlines the Netskope Client deployment instructions for the following user enrollment methods and supported platforms. User enrollment methods not documented here are not supported at this time.
Enrollment Methods
Single User
Multi-user
IDP
Y
Y
PLIST
Y
N
Configuration Profile Setup
Jamf Configuration Profiles manage the core configuration for Client installation. The following sections provide a detailed overview of how to configure these profiles effectively. You can add the following to a New or Existing Configuration Profile.
To create a New Configuration Profile:
In the Jamf console, go to
Computers
>
Configuration Profiles
>
New
.
Under
Options
>
General
.
Enter the display name. For example, Netskope Client Configuration Profile.
Choose the following:
Category:
None
Level:
Computer Level
Click
Scope
.
Click
Targets
, then select the specific user(s) or device(s) to assign the configuration profile.
Click
Save
.
Pre-Approve Network Extension
The Netskope Client on macOS installs a network extension that requires administrator approval to function. The following configuration pre-approves the network extension and suppresses end-user notifications requesting approval.
In the Jamf console, go to
Computers
>
Configuration Profiles
> select required Configuration Profile.
Go to
Options
>
System Extension
.
Click
Configure
or
Edit
.
Select
Allow users to approve system extensions
.
Under
Allowed Team IDs and System Extensions
, enter a display name. For example, Netskope System Extension.
Choose the following:
System Extension Types:
Allowed System Extensions
Team Identifier:
24W52P9M7W
Click
Add
to add the following System Extension:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
In the
Scope
tab, assign the target computers.
Click
Save
.
Pre-Approve Full Disk Access Permission For macOS 14 (Sonoma) and Later
The Netskope Client on macOS requires Full Disk Access permissions for various foundational functionalities. The following configuration pre-approves these permissions and suppresses end-user notifications requesting approval.
In the Jamf console, go to
Computers
>
Configuration Profiles
> select required Configuration Profile
Go to
Options
>
Privacy Preferences Policy Control
.
Click
Configure
or
Edit
.
Under
App
Access
, enter the following:
Identifier:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Select
Bundle ID
for
Identifier
Type.
Code Requirement:
anchor apple generic and identifier "com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
Click
+Add
to allow or deny access to a service or app.
Select
SystemPolicyAllFiles
under
App or Service
and
Allow
under
Access
.
Click
Save
.
Save the configuration profile.
For Endpoint DLP, you can add the following Identifier and Code Requirement:
– Identifier:
com.netskope.epdlp.client
– Code Requirement:
anchor apple generic and identifier "com.netskope.epdlp.client" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
To learn more:
Enabling Endpoint DLP on the Netskope Client for macOS
.
Pre-Approve VPN Popup for App Proxy
The Netskope Client on macOS installs a network extension that triggers updates to the device’s Network settings. The following configuration pre-approves these updates and suppresses end-user notifications requesting approval.
In the Jamf console, go to
Computers
>
Configuration Profiles
> select required Configuration Profile.
Go to
Options
>
VPN
.
Click
Configure
or
Edit
and configure the VPN with following:
Connection Name:
Any Name
VPN Type:
Select Per-App VPN
Per-App VPN Connection Type:
Select Custom SSL
Identifier:
Enter
com.netskope.client.Netskope-Client
Server:
Enter the Netskope Gateway URL for the tenant: gateway-<tenant_hostname>.goskope.com
Provider Bundle Identifier:
Enter
com.netskope.client.Netskope-Client
Provider Type:
Select App-Proxy
Select
Include All Networks
For
Specify Provider Designated Requirement
, enter the following:
anchor apple generic and identifier"com.netskope.client.Netskope-Client" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
Select
Prohibit users from disabling on-demand VPN settings
.
Click
Save
.
Prevent Disabling of System Extensions in macOS 15 (Sequoia) or Later
Netskope recommends adding two optional deployment parameters
Prevent Disabling of System Extensions
and
Restrict App Proxy Removal
to manage user permissions regarding System Extensions in macOS 15 (Sequoia) and above. These controls prevent the removal of the specified system extension by the user.
In the Jamf console, go to
Computers
>
Configuration
Profiles
> select required Configuration Profile.
Go to
Options
>
System
Extensions
.
Click
Configure
or
Edit
.
Select
Allow users to approve system extensions
.
Under
Allowed Team IDs and System Extensions
, enter a display name. For example, Netskope System Extension.
Choose the following:
System Extension Types:
Non-removable system extensions from UI
Team Identifier:
24W52P9M7W
Click
Add
to add the following System Extension:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
In the
Scope
tab, assign the target computers.
Click
Save
.
Restrict App Proxy Removal
Netskope recommends adding two optional deployment parameters
Prevent Disabling of System Extensions
and
Restrict App Proxy Removal
to manage user permissions regarding System Extensions in macOS 15 (Sequoia) and above. These controls prevent the removal of the specified system extension by the user.
In the Jamf console, go to
Computers
>
Configuration
Profiles
> select required Configuration Profile.
Go to
Options
>
Restrictions
.
Click
Configure
or
Edit
.
Under
Preferences
, select
Restrict items in System Preferences
.
Select items (Network in this case).
Add the scope (machine) and push the profile.
Click
Save
.
Push Netskope Root and Tenant Certificates via Jamf
Provide additional trust to end users by pushing certificates during client installation. Before you can push the root and tenant certificates, ensure that you do the following:
Download root and tenant certificates from Netskope MDM distribution page.
Login to Netskope tenant admin console with admin credentials.
Go to
Settings
>
Security Cloud Platform
>
MDM Distribution
. The certificate download options are displayed in the Certificate Setup section.
Convert the downloaded certificates to
.cer
format by renaming the .pem files to .cer.
Perform the following steps to add certificates to Jamf:
In the Jamf console, go to
Computers
>
Configuration
Profiles
> select required Configuration Profile
Go to
Options
>
Certificate
.
Click
Configure
or
Edit
.
Enter a name for the certificates.
Select
Upload
to upload the converted root and tenant certificates.
To add a certificate click the “+” icon.
In the
Scope
tab, select the target computers.
Click
Save
.
Jamf Policy Setup
Additional core configuration for Client installation is carried out using Jamf policies. The following sections provide a detailed explanation of how these policies are configured.
The following can be added to a New or Existing Jamf Policy.
Add Installation Script to Jamf
Perform the following steps to add the Netskope Client installation script to Jamf using the script editor:
In Jamf, go to
Settings
>
Computer
management
.
Click
Scripts
.
Click
+New
.
In the
General
tab, add the
Display
Name
and other basic settings for the script.
In the
Script
tab, copy and paste the script contents in the script editor.
Copy and paste the shell script from the file: nsclientconfig.sh downloaded from the Netskope Support portal. For more information, view
Prerequisites
.
In the
Options
tab, provide the additional settings for the script, including the priority and parameter labels (Optional).
For
Priority
, select
Before
. The script must be executed before the installation process, so Priority must be Before.
(Optional)In the
Limitations
tab, provide the operating system requirements for the script.
Click
Save
.
For more information on adding a script, view
Add Script
.
Upload Client Package to Jamf
Perform the following steps to upload the Netskope Client macOS package to Jamf.
To upload a package:
In Jamf, go to
Settings
>
Computer management
.
Click
Packages
.
Click
+New
.
In the
General
tab:
Add the
Display Name
and other basic settings for the package.
In
Filename
, drag and drop the Netskope Client installer package for macOS or click browse for a file to select and upload the package.
(Optional) If you are uploading an enrollment package, you can upload a custom manifest file by dragging and dropping or clicking browse for a file in the Manifest file field.
In the
Options
tab, add the additional settings for the package, including the priority.
(Optional) In the
Limitations
tab, provide the operating system and architecture type requirements.
Click
Save
.
Configuring the Jamf Policy
Perform the following steps to build the Jamf Policy.
The following can be added to a New or Existing Jamf Policy. If using an existing Policy navigate to the Policy and skip to step 5:
In the Jamf console, go to
Computer
>
Policies
.
Click
+ New
.
Under
Options
>
General
.
Enter a
Display Name
, for example: Netskope Client Policy.
For
Trigger
, select
Login
.
Run Scripts using other options such as Logout and Network State Change; according to the administrator requirements.
For
Execution
Frequency
, select
Once per computer
.
Select
Options
>
Packages
.
Click
Configure
.
Click
Add
to include the Client installer package that you uploaded in this
section
.
After you click
Add
, the Package UI displays the selected package.
On the
Package
screen, select
Install
from the dropdown options in
Action
.
Select
Options
>
Scripts
.
Click
Configure
.
Click
Add
to include the .sh script configured in this
section
.
For
Priority
, select
Before
. The script must be executed before the installation process, so Priority must be Before.
Update the script options for the parameters depending on the deployment mode below. Refer to the table below the instructions to understand the available enrollment methods and associated parameters required for the script.
Click the
+
button to add another script.
When finished, click
Save
.
Deployment Mode
Configuration Parameters
IDP Single-User mode
Parameter 4
: Enter
idp
to specify the Client deployment mode is IDP. This parameter is case-sensitive. Enter the letters in lowercase.
Parameter 5
: Domain name. Example, if your tenant URL is
https://corp.goskope.com
, then enter
goskope.com
Parameter 6
: Tenant name. Example: If your tenant URL is
https://corp.goskope.com
, enter
corp
.
Parameter 7
: Email Address request option. Enter
0
, if you do not want request user's email address. Enter
1
to request user's email address.
Parameter 8
: Enter the Encryption Token including the key name, “=”, and the token value, with no spaces between. For example, enrollencryptiontoken=51696332b0116axxxxxxxxxxxxxxxxxx
Parameter 9
: Enter the
Steering Profile ID
. For example, ENFORCEENROLLSTEERINGPROFILEID=<steering profile ID value>
Parameter 10
: Enter the enforce enroll frequency value. For example, ENFORCEENROLLFREQUENCY=<value between 1 minute - 24 hours>
Use parameters 9 and 10 only if you want to
enforce enrollment
for users during Netskope Client installation.
Get your
Encryption token
from Settings > Security Cloud Platform > MDM Distribution > Secure Enrollment.
To learn about FIDO authentication support, see
External Browser-based Authentication
.
IDP Multi-User mode
Parameter 4
: Enter
idp
to specify that the Client deployment mode is IDP. This parameter is case-sensitive. Enter the letters in lowercase.
Parameter 5
: Domain name. Example, if your tenant URL is
https://corp.goskope.com
, then enter
goskope.com
Parameter 6
: Tenant name. Example: If your tenant URL is
https://corp.goskope.com
, enter
corp
.
Parameter 7
: Email Address request option. Enter
0
, if you do not want request user's email address. Enter
1
to request user's email address.
Parameter 8
: Enter
peruserconfig
to specify multi-user IDP deployment mode.
Parameter 9
: Enter the Encryption Token including the key name, “=”, and the token value, with no spaces between. For example, enrollencryptiontoken=51696332b0116axxxxxxxxxxxxxxxxxx
Parameter 10
: Enter the
Steering Profile ID
. For example, ENFORCEENROLLSTEERINGPROFILEID=<steering profile ID value>
Parameter 11
: Enter the enforce enroll frequency value. For example, ENFORCEENROLLFREQUENCY=<value between 1 minute - 24 hours>
Use parameters 10 and 11 only if you want to
enforce enrollment
for users during Netskope Client installation.
Get your
Encryption token
from Settings > Security Cloud Platform > MDM Distribution > Secure Enrollment.
To learn about FIDO authentication support, see
External Browser-based Authentication
.
For macOS devices (single-user installations) that are not AD joined.
Parameter 4
: Your tenant URL.
If your tenant URL is https://corp.goskope.com, enter addon-corp.goskope.com.
Parameter 5
: Your Organization ID.
Parameter 6
: Preferences file (
plist
)  name. When entering the filename, enter the complete filename including the
.plist
extension.
Example: netskope.plist
. Do not add
HTTP:
to the URL in the plist file.
Note
The name must match as defined in the
JAMF
>
Computers
>
Configuration Profiles
>
Custom Settings
>
Preference Domain
. The Preference Domain will not include the .plist extension but the JAMF script parameter 6 must include the
.plist
extension.
Parameter 7
: Enter the keyword
preference_email
.
Parameter 8
: Enter the Authentication Token including the key name, “=”, and the token value, with no spaces between. For example, enrollauthtoken=98774b6e6916f54axxxxxxxxxxxxxxxx
Get your
Authentication token
from Settings > Security Cloud Platform > MDM Distribution > Secure Enrollment.
Parameter 9
: Enter the Encryption Token including the key name, “=”, and the token value, with no spaces between. For example, enrollencryptiontoken=51696332b0116axxxxxxxxxxxxxxxxxx
Get your
Encryption token
from Settings > Security Cloud Platform > MDM Distribution > Secure Enrollment.
To learn about creating a PLIST, view
Create PLIST File
.
Adding the Silent Mode (silent_mode) parameter as the last parameter in the script options for any deployment mode can suppress the Netskope Client Installer failure pop-up in the event of any deployment failure.
External Browser-based Authentication
The Netskope Client supports FIDO authentication on macOS devices via external browser integration with our SAML forward proxy. When you enable external browser support during the deployment of the Netskope Client, the authentication flow transitions from the client’s built‑in browser to the operating system’s default browser. This adjustment enables the use of more advanced and robust web authentication mechanisms.
External browser support is available for Safari, MS Edge, and Google Chrome when set as the default browser (Firefox is not supported).
Configure the following additional parameters in the needed Jamf Policy when deploying the Client in IdP mode (single user and multi-user):
The following parameters are to be appended to the Jamf Policy as the next available:
Mode
: Mode is a string value used to enable external browser support
Embedded
: Default value and opens the existing mini-browser.
Scheme
:  Opens the external browser (system default browser).
preferEphemeral
:
True
: An ephemeral (private) browser window will be launched from the default browser.
False
: A regular (non-private) browser window will be launched from the default browser.
httpmethod
: httpmethod alters the web authentication flow in efforts to alleviate issues with the Safari browser and redundant WebAuth.html notification pop-ups. If Safari is not the default browser, this parameter (httpmethod) is not needed.
httpmethod=get
These parameters require the latest JAMFScript_v20_Jan2023 available in Netskope
Support
portal.
For example,
sudo ./nsclientconfig.sh 1 2 3 idp goskope.com corp 0 mode=scheme preferephemeral=true httpmethod=get
Create .plist File for PLIST User Enrollment
This section contains the steps to install the Netskope Client using PLIST user enrollment.
The “peruserconfig” attribute (multi-user mode) cannot be supported as part of this deployment method.
Step 1: Save PLIST File
Save the following
com.netskope.client.plist
file and use it with your MDM for Netskope Client PLIST deployments.
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
	<dict>
		<key>email</key>
		<string>$EMAIL</string>
	</dict>
</plist>
Step 2: Configure Jamf to Push the PLIST File to the macOS Machine
The following can be added to a New or Existing Configuration Profile. If using an existing Configuration Profile navigate to the Profile and skip to step 3:
In the Jamf console, go to
Computers
>
Configuration
Profiles
>
New
.
Under
Options
>
General
.
Enter the display name. For example, PLIST File Deployment.
Choose the following:
Category:
None
Level:
Computer Level
Distribution Method:
Install Automatically
Go to
Application and Custom Settings
.
Click
Upload
.
Click
Add
to enter the details of the previously created plist file.
The
Preference Domain
should be the name of the plist file you generated without .plist. For example, if using the instructions above, the preference name should be com.netskope.client.
Click
Upload
to upload the previously created plist file and see the contents displayed under
Property List
.
Click
Scope
and assign the plist payload you created to the appropriate user or machine groups.
Click
Save
.
Verifying Client Installation
Check the installation logs on the user’s machine in the /var/log/install.log folder. If the user configuration download script fails and the Netskope client installer is executed, the installer will exit and display the
Configuration file missing, aborting installation!
error message.
Check Netskope Client Installation Status
To verify the status of each device, go to
Computer
>
Policies
and click on the policy you created.
Click the
Logs
button at the bottom to view the log files for each device and then click the
Show
button.
Confirming the Netskope Client Extension Approval
To confirm that the Netskope Client extension has been approved and the client is running, run the following command in your macOS terminal window:
systemextensionsctl list
The output should look like this:
% systemextensionsctl list  
1 extension(s)
--- com.apple.system_extension.network_extension
enabled active teamID bundleID (version) name [state]
* * 24W52P9M7W com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy (85.2.0.269/1) 
NetskopeClientMacAppProxy [activated enabled]
Additionally, inspect the system preferences and Network UI to confirm that Netskope Client extension is active.
Uninstalling the Netskope Client
See
Uninstalling the Netskope Client
for instructions on uninstalling the Netskope Client.
In this Topic
Deploy Client on MacOS Using Jamf Pro

---
## Netskope Client Network Configuration
**URL:** https://docs.netskope.com/en/netskope-client-network-configuration/
**Last Modified:** 2026-06-15T13:24:30+00:00
**Scraped:** 2026-06-26T09:28:41.658306+00:00

Netskope Client Network Configuration
This topic describes the various network configuration requirements for Netskope Client with respect to Global Server Load Balancing (GSLB) and how it works.
Client Outbound Connectivity Requirements
For normal functioning, the Netskope Client must be allowed to connect outbound directly to the subnets, domains, ports, and protocols as given in the following tables:
– Firewalls and Proxies: Allow these connections without decryption.
– Full Tunnel VPNs: Add these connections as exceptions or exclusions.
– Split Tunnel VPNs: Do not include these connections.
– The following document includes references to
Internet Security
which includes NG-SWG, Cloud Inline, Inline CASB, Cloud Firewall, and DNS Security.
– The following document includes references to
Private Access
which is also known as Netskope Private Access, NPA, and ZTNA Next L7.
– HTTP/2: We negotiate HTTP/2 for all domains if the origin server supports it, otherwise, we fallback to HTTP 1.1. All other traffic will continue to leverage HTTP 1.1.The protocol change is completely transparent to users, no configuration is required by admins. Contact Support to enable this feature in your account.
–  In addition, the Netskope Client and GRE / IPSEC and iOS access methods are fully supported.
Client Version: 109.0.0 or later
The following section applies to tenants with Client version 109.00 or later where the GSLB feature is enabled for Internet Security and Private Access.
All Clients connecting to the tenant should be running version 109.0.0 or later before enabling GSLB.
Netskope Products
Destination Subnets and Domains
Protocols/Ports
Purpose
Internet Security
Private Access
All Netskope NewEdge Data Center Subnets
TCP/443
TLS connectivity to Netskope NewEdge data plane for Internet Security and Private Access.
UDP/443
DTLS connectivity to Netskope NewEdge data plane for Internet Security.
ICMP Type 8 and 11
UDP/33434
GSLB Automated Route Control.
PDEM latency metrics collection.
Internet Security
Private Access
Endpoint SD-WAN
DNS Servers
UDP/53
DNS lookups for connectivity to Netskope services. This can be a private or public DNS server, but must resolve public domains.
Private Access
*.npa.goskope.com
Contact Netskope Support, or Sales Representatives if tenant-specific domains or IP subnets are required.
TCP/443
Client enrollment and re-enrollment for Private Access.
Endpoint DLP
epdlp.gslb.goskope.com
*.epdlp.goskope.com
epdlp-prod.netskope.io
TCP/443
Endpoint DLP connectivity and policy updates.
Internet Security
Private Access
enrollment.goskope.com
enrollment.*.goskope.com
enrollment.*.govskope.ca
enrollment.*.govskope.us
Contact Netskope Support or your Sales Representative if tenant-specific domains are required.
TCP/443
Secure Enrollment connectivity.
Internet Security
Private Access
gateway.gslb.goskope.com
TCP/443
GSLB latency-based Gateway Selection for Internet Security and Private Access (API call to request the list of nearby data centers).
GSLB
Netskope NewEdge IP space
ICMP type 8 and 11
UDP 33434-33498
Network path telemetry to Netskope data centers.
Endpoint SD-WAN
Admin managed Borderless SD-WAN Gateway Hub
UDP/443
L3 Tunnel from Endpoint to Gateway Hub.
*.googleapis.com
TCP/443
Application Detection using First Packet Detection.
Client Version: 103.0.0 to 108.x.x
This section applies to tenants with Client version 103.0.0 or later where the GSLB feature is enabled for Internet Security and disabled for Private Access.
All Clients connecting to the tenant should be running version 103.0.0 or later before enabling GSLB.
Netskope Products
Destination Subnets and Domains
Protocols/Ports
Purpose
Internet Security
Private Access
All Netskope NewEdge Data Center Subnets
TCP/443
GSLB latency-based Gateway Selection for Internet Security.
TLS connectivity to Netskope NewEdge data plane Internet Security and Private Access.
UDP/443
DTLS connectivity to Netskope NewEdge data plane for Internet Security.
Internet Security
Private Access
DNS Servers
UDP/53
DNS lookups for connectivity to Netskope services. This can be a private or public DNS server, but must resolve public domains.
Private Access
dns.google
8.8.8.8
8.8.4.4
TCP/443
EDNS geolocation-based Gateway Selection for Private Access. If this is blocked or fails, LDNS geolocation-based Gateway Selection will be used which can result in higher latency connectivity.
Private Access
*.npa.goskope.com
Contact Netskope Support, or Sales Representatives if tenant-specific domains or IP subnets are required.
TCP/443
Client enrollment and reenrollment for Private Access.
All Client Versions
This section applies to all tenants with any Client version where the GSLB feature is disabled for Internet Security and Private Access.
Netskope Products
Destination Subnets and Domains
Protocols/Ports
Purpose
Internet Security
Private Access
dns.google
8.8.8.8
8.8.4.4
TCP/443
EDNS geolocation-based Gateway Selection for Internet Security and Private Access. If this is blocked or fails, LDNS geolocation-based Gateway Selection will be used which can result in higher latency connectivity.
Internet Security
Private Access
DNS Servers
UDP/53
DNS lookups for connectivity to Netskope services. This can be a private or public DNS server, but must resolve public domains.
Internet Security
Private Access
addon- < tenant > [.region].goskope.com
TCP/443
Downloading configuration files and dynamically detecting proxies.
Internet Security
Private Access
download- < tenant > [.region].goskope.com
TCP/443
Downloading client package updates.
Internet Security
Private Access
nsauth- < tenant > [.region].goskope.com
TCP/443
IdP-based Client Enrollment and Periodic Re-authentication for Private Apps.
Internet Security
gateway- < tenant > [.region].goskope.com
gateway-backup- < tenant > [.region].goskope.com
TCP/443
Primary and Backup TLS connectivity to Netskope NewEdge data plane for Internet Security.
UDP/443
Primary and Backup DTLS connectivity to Netskope NewEdge data plane for Internet Security.
Internet Security
achecker- < tenant > [.region].goskope.com
TCP/443
Client enforcement. This is required to enforce the end-user to install the Client on their device. If the Client is not installed in the users’ device, access to an app or domain specified in the steering configuration is restricted and the user is redirected to a browser page with instructions to install the Client.
Private Access
gateway.npa.goskope.com
TCP/443
TLS connectivity to Netskope NewEdge data plane for Private Access.
Private Access
*.npa.goskope.com
Contact Netskope Support, or Sales Representatives if tenant-specific domains or IP subnets are required.
TCP/443
Client enrollment and re-enrollment for Private Access.
Publisher Outbound Connectivity Requirements
This section applies to all Private Access Publisher versions starting with 109.0.0 where the GSLB feature is enabled for Private Access publishers.
Netskope Products
Destination Subnets and Domains
Protocols/Ports
Purpose
Private Access Publisher
All Netskope NewEdge Data Center Subnets
TCP/443
TLS connectivity to Netskope NewEdge data plane.
Private Access Publisher
gateway.gslb.goskope.com
TCP/443
GSLB latency-based Stitcher Selection for Private Access Publishers (API call to request the list of nearby data centers).
Private Access Publisher
DNS Servers
UDP/53
DNS lookups for connectivity to Netskope services. This can be a local or public DNS server, but must resolve public domains.
Private Access Publisher
*.docker.com
*.docker.io
*.ubuntu.com
TCP/443
Publisher updates
Private Access Publisher
*.ubuntu.com
TCP/80
Publisher updates
Private Access Publisher
*.npa.goskope.com
Contact Netskope Support, or Sales Representatives if IP subnets are needed instead of FQDNs.
TCP/443
Publisher registration
NewEdge Traffic Management Gateway Selection
NewEdge Traffic Management 2.0 (GSLB) is a latency-based gateway selection method that uses a proprietary Netskope-hosted API service instead of relying on third-party services such as Google DNS. Global Server Load Balancing (GSLB) provides a better user experience by allowing Netskope to quickly identify and address network issues, improve performance, improve stability, and improve resilience. The Netskope Client now considers many nearby NewEdge data centers and calculates latency (RTT) to each, then selects the data center with the lowest latency. If GSLB cannot be reached then the Netskope Client falls back to the previous extended DNS(EDNS) and local DNS(LDNS) geolocation-based gateway selection behavior.
GSLB services are available for Internet Security and  Private Access.
NG-SWG:
This feature is enabled by default for tenants created after the release of platform version 109. To enable this feature for tenants created earlier, contact your Sales Representative or Netskope Support.
Private Access:
GSLB services are available for all tenants. To enable this feature contact your Sales Representative or Netskope Support.
In the event of GSLB call failure, Publisher and Netskope Client fallback to EDNS or LDNS.
By default GSLB will return 10 nearby data centers to test for latency. Contact Support to modify this value.
For Private Access:
The minimum version for Client and Publisher must be 109.0.0. Older versions continue to work with EDNS/LDNS. Restart of Netskope Client and Publisher may be required upon enabling the feature:
If GSLB functionality is enabled for Netskope Client versions 108.0.0 or lower, updating to 109.0.0 activates GSLB automatically without requiring a restart.
If the GSLB functionality is enabled for Netskope Publisher versions 108.0.0 or lower, updating to 110.0.0 activates GSLB automatically without requiring a restart.
You can now configure New Edge Traffic Management Zones per tenant. Contact Support to configure this feature.
Do not support Periodic RTT checks during the session.
Fallback to EDNS/LDNS can be disabled. Contact Support to configure this feature.
Supported Operating Systems
GSLB is supported on all operating systems. For more details, view
Netskope Client Supported OS and Platform
.
Prerequisites
Refer to the tables in the previous sections of this page for Client version and network connectivity requirements. Refer to the
Support
portal to understand the allowed IP ranges for outbound access on your firewall.
FedRAMP High IPs are different and the current list can be found here:
https://support.netskope.com/s/article/NewEdge-Consolidated-List-of-IP-Range-for-Allowlisting
(Requires a Support account).
To collect Client logs through the Netskope tenant, view
Unable to collect client debug logs remotely
(Requires a Support account).
Also, ensure that your VPN is not configured to tunnel those IP ranges through a VPN tunnel. To learn more about VPN compatibility, view
VPN Applications
.
GSLB Gateway Selection Process
The Netskope Client connects to Netskope’s API (gateway.gslb.goskope.com) using HTTPS (tcp/443) to request a list of nearby Netskope data centers.
Netskope’s API uses the public IP of the API request to look up the geolocation of the endpoint.
Netskope’s API then responds with a list of geographically nearby Netskope data centers.
The Netskope Client tests latency to each of the nearby Netskope data centers.
The Netskope Client utilizes these latency measurements to pick the best data center (DC). This is generally the one with the lowest latency (RTT); however, in some cases a nearby DC with similar latency characteristics may be selected.
If the HTTPS connection to Netskope’s API is steered through a VPN, this will change the public IP of the request and incorrectly geo locate the user, which can result in the Netskope Client connecting to a Netskope data center far from the endpoint.
If the endpoint’s public IP is incorrectly registered with geolocation databases, this can result in the Netskope Client connecting to a Netskope data center far from the endpoint.
If the HTTPS connection to Netskope’s API is blocked, the Netskope Client will attempt to use EDNS and LDNS for gateway selection.
Netskope Private Access tenants may now take advantage of NewEdge Traffic Management intent-based Zones. Some organizations have inline (or “data in motion”) compliance requirements that restrict inline traffic processing to specific geographical regions.Now, the  Private Access tenants can restrict traffic to supported Zones. To learn more:
Configure NewEdge Traffic Management Zones per NPA Tenant
.
Gateway Selection Behavior Using EDNS and LDNS
NewEdge Traffic Management 1.0 is a geolocation-based gateway selection method that uses DNS. Initially, the Netskope Client used
EDNS
to resolve one of the following gateway fully qualified domain names(FQDN):
gateway-<tenant>[.region].goskope.com
gateway-backup-<tenant>[.region].goskope.com
If EDNS resolution fails then the Netskope Client uses
LDNS
to resolve the gateway FQDNs.
EDNS Gateway Selection Process
Refer to the following instructions to understand the EDNS gateway selection process:
The Netskope Client connects to Google DNS (dns.google) using DNS over HTTPS (tcp/443) to request an IP for gateway-<tenant>[.region].goskope.com.
Google DNS uses the public IP of the DNS over HTTPS request to look up the geolocation of the endpoint.
Google DNS then resolves gateway-<tenant>[.region].goskope.com to the Netskope data center geographically closest to the endpoint’s public IP.
The Netskope Client connects to the Netskope data center using the provided IP.
If the DNS over HTTPS connection is steered through a VPN, this changes the public IP of the request and incorrectly geo-locates the user, which can result in the Netskope Client connecting to a Netskope data center far from the endpoint.
If the endpoint’s public IP is incorrectly registered with geolocation databases, this can result in the Netskope Client connecting to a Netskope data center far from the endpoint.
If the DNS over HTTPS connection is blocked, the Netskope Client attempts to use LDNS to resolve gateway-<tenant>[.region].goskope.com.
LDNS Gateway Selection Process
Refer to the following instructions to understand the LDNS gateway selection process:
The Netskope client uses the endpoint’s configured DNS server using standard DNS (udp/53) to resolve gateway-<tenant>[.region].goskope.com.
The Netskope Client connects to the Netskope data center using the provided IP.
If the DNS server’s public IP is registered geographically far from the endpoint, this can result in the Netskope Client connecting to a Netskope data center far from the endpoint. For example, if the endpoint is in San Jose, CA, but it is configured to use a corporate DNS server located in Ashburn, VA, the endpoint will connect to a Netskope data center near Ashburn, VA. This would result in significant additional latency for all Internet and Private Access connectivity through Netskope.
GSLB Fallback in China
With the release of version 121.0.7, for tenants using Netskope’s POPs in China, devices running Netskope Client outside China can now fallback to EDNS and then to LDNS when GSLB is not reachable. At the same time, devices with Netskope Client in China continue to use GSLB exclusively to ensure that those users only connect to Netskope POPs within China.
This is the default behavior for all tenants using Netskope’s POPs in China.
Validate EDNS/LDNS
You can check for the country code in your logs while debugging:
If the location is in China:
2024/09/25 17:33:58.421 stAgentSvc p1d14 t1ed8 info GatewaySelection.cpp:139 gslb [NSClient] Pops fetched begin rtt_protocol:tcp
country:CN
If the location is outside China:
2024/09/25 09:09:52.105766 stAgentNE p14257 t15367 info GatewaySelection.cpp:139 gslb [NSClient] Pops fetched begin rtt_protocol:http
country:US
Netskope Client in a Non-Proxy Environment
Here are the packet flow details of how the cloud app traffic is intercepted and sent through the tunnel when the client is installed in a non-proxy environment:
The Client establishes the SSL tunnel between the Client and the Netskope gateway.
Browser/App sends a DNS request for a managed cloud service (
For example: Box.com
).
Browser/App receives a DNS response (
For example: 74.112.184.73
).
The Client driver captures DNS response and creates a map of domain and IP (
For example: Box.com = 74.112.184.73 for cloud app domains
).
Browser/App sends packets to Box.com (
For example: DST IP 74.112.184.73
).
Client tunnels Box traffic (
For example: DST IP 74.112.184.73
) through the SSL tunnel.
Netskope Client in an Explicit Proxy Environment
Here are the packet flow details of how the Cloud app traffic is intercepted and sent through the tunnel when the client is installed in an explicit proxy environment:
The Client establishes the SSL tunnel between the Client and the Netskope gateway. The Client first tries to connect directly through default gateway to establish the SSL tunnel. If this is blocked, then it looks for system proxy settings, such as PAC (proxy auto-config) files, WPAD (Web Proxy Auto-Discovery Protocol), and manual configuration. The client uses the proxy settings and connects to the Netskope gateway via HTTP Connect.
The Netskope gateway should be SSL allowlisted if the proxy is configured for SSL decryption. If your environment uses firewall or proxy, ensure that you process the backup gateway URL in the same manner as the primary gateway URL. The backup gateway URL is suffixed with
gateway-backup
to your primary URL.
The browser or native app reads the proxy settings (PAC file, explicit proxy setting) and opens a connection to an explicit proxy server, for example:
ep.customer.com
.
The client parses the initial header of the connection.
If the initial header indicates the connection is:
Cloud mode (SaaS app): The initial header indicates the hostname of the SaaS application. If the hostname is not a part of the managed SaaS application exception configuration, the Client bypasses the traffic to a local proxy server.
Web and All Traffic mode: The initial header indicates the hostname of the web application. If the hostname is a part of the exception, the Client bypasses the traffic to a local proxy server. Otherwise, the traffic is tunneled to the Netskope gateway.
If the initial header does not indicate SaaS app HTTPS access, the Netskope Client bypass the traffic and forwards the entire payload to the explicit proxy server. For example:  ep.customer.com.
Netskope Client Log Messages with On-prem Proxy
Steering traffic flow and Log message
: With on-prem proxy, the Netskope Client monitors for HTTP CONNECT requests. It checks for the domain name in these requests against the managed domain list. If the name matches then it will reconstruct the TCP SYN packet and send it through the Netskope Tunnel and at the same time it will send TCP RST to on-prem proxy, and it will take control of that connection. After the TCP 3-way handshake with Netskope proxy, it sends the HTTP CONNECT request and the flow continues with Netskope proxy. Since TCP flow will be with destination IP of on-prem proxy when Netskope Client logs the message, it will show destination IP as on-prem Proxy and the domain name will be the managed domain.
Assuming on-prem Proxy IP is 10.10.10.11 and Proxy port is 8080 and the managed domain is www.box.com then you will see the log line as below:
2021/07/18 17:16:11.282 stAgentSvc pfbc t296c 4 tunnel.cpp:618 nsTunnel TLS [sessId 1]
Tunneling flow from addr: 192.168.13.40:49614, 
process: chrome.exe to host: www.box.com,addr: 10.10.10.11:8080
In this Topic
Netskope Client Network Configuration

---
## Netskope Client For Android and ChromeOS
**URL:** https://docs.netskope.com/en/netskope-client-for-android/
**Last Modified:** 2026-04-14T07:07:08+00:00
**Scraped:** 2026-06-26T09:29:51.421995+00:00

Netskope Client For Android and ChromeOS
This document describes the available deployment methods and user enrollment options when installing the Netskope Client on Android and ChromeOS devices.
Supported versions
Refer to
Netskope Client Supported OS and Platform
for more details on the supported versions for Android and ChromeOS.
Deploy Client in Android and Chrome OS
Refer to the following sections to understand the various Client deployment methods in Android and ChromeOS devices:
Netskope Client installation methods are the same for Android and ChromeOS devices.
Netskope Client for Android does not coexist with any
third-party VPN
applications due to Android limitation that stops an existing service when a new service is started. To learn more, view
VPN
.
Email Invite
You can install Netskope Client using the email invitation sent from the admin console.
After you receive the email:
Check your email from Netskope Onboarding and click Android Client.
Follow the instructions on your screens to install Netskope Client from Google Play Store.
Click
Install
.
After you install, Click
Open
.
Click
Allow
for notifications.
The app opens after it completes downloading the configurations.
To learn more, view
Email Invite
.
MDM Deployment Options
Netskope offers support for a wide range of MDM solutions. For MDM-specific instructions on deploying the Netskope Client, see
Netskope Client Deployment Options
.
Google Admin Console
The following sections describes the deployment instructions for ChromeOS and Android.
ChromeOS Deployment
You can configure the tenant name in
Devices
>
Chrome
>
Apps&extensions
>
Users &browsers
. The administrators can configure deployment parameters using one of the following methods:
Configuration Option 1
User Email Address: The user email address. For example, < emailID@example.com >
Host: The addon host. For example, addon-< tenant-name >.skope.com
Token: The organization ID
For more information on deployment parameters, see
Client Deployment Parameters
.
Configuration Option 2
Tenant: The tenant name. For example, <tenant-name>.skope.com.
The application inspects for any pre-deployed app configuration and applies them immediately. If both the configurations contain valid data, then
Configuration Option 1
always takes precedence.
Android Deployment
Administrators may configure deployment parameters in
Apps
>
Web and mobile apps
>
Netskope Client
>
Managed Configurations
to select the configuration. Select an available configuration or click
Add Managed Configuration
to create a new configuration.
Use Google Admin Console to install CA Certificates. Navigate to
Device
>
Chrome
>
Settings
>
Users&Browsers
>
Android Applications
>
Certificate Synchronization
.
Enrollment Workflow in ChromeOS and Android Devices
The following steps illustrate the Netskope Client deployment and enrollment workflow in ChromeOS and Android devices from Google Play Store:
Important
Netskope recommends that you consider the following before proceeding with deployment:
End-user devices must support Android AppLink feature for auto enrollment process.
Firewall must allow  access to
Applink
. If Android OS encounters a network glitch or Android OS applink binding API error while connecting to
Applink
, then Netskope recommends you to uninstall and reinstall the Netskope Client to fix the issue.
Netskope recommends the use of Google Admin console or your MDM tool for deploying CA certificates. See Traffic Steering > Explicit Proxy >
Traffic Steering from Chromebooks
for more information.
Visit Google Play Store and download
Netskope Client
.
Install Netskope Client. After the installation is complete, a pop-up is displayed to the user to enter the
tenant name
and select the
tenant domain
as shared with the user by their respective IT.
Click
Next
to continue with enrollment. User is redirected to their IdP login screen. Authentication status message is displayed in the browser.
Once the user enrollment is complete, the Client will initiate configuration download and establish tunnel.
After the Client is connected, user can click the mobile menu icon (
3 vertical dots in the top right corner of the client
) for options to view configuration details.
SSL Inspection for Android
SSL/TLS inspection is a foundational capability that enables Netskope  to perform efficient threat and data protection services. Netskope performs SSL inspection and serves as a Man-in-the-Middle. In order to establish trust between source applications and Netskope it is required to install CA certificate into appropriate OS store. To learn more, view
Certificates for SSL/TLS Inspection
.
SSL decryption policies allow you to specify the traffic you want to leave encrypted and not further analyzed by Netskope via the Real-time Protection policies. To learn more, view
SSL Decryption
.
In Android devices, a CA certificate can only be  installed in the user cert store irrespective of device ownership and enrollment method. Starting with Android Nougat (7.0), Netskope certificates stored in the user certificate store are not trusted by Android and 3rd party app services, since Google does not trust the certificates installed in the user store. This leads to errors during SSL inspection due to broken chain of trust – native or 3rd party mobile applications would drop SSL handshake because server certificates presented by Netskope SWG won’t get recognized as trusted. However web-browsers (such as Chrome, Edge etc) will still be able to verify chain of trust against user cert store and therefore SSL inspection won’t cause issues.
There are two options to get around Android limitations:
Disable SSL inspection for Android. At the time of Netskope client distribution & enrollment (and irrespective of enrollment method and device ownership) CA certificate distribution can be skipped. Netskope Client won’t find a CA certificate on the device and will signal upstream proxy that SSL inspection should not be performed. The traffic will still be tunneled via NewEdge according to Steering Configuration.
Enable selective SSL inspection on Android based on the source App. Once a CA certificate is detected on the device by Netskope client, SSL inspection would be enabled for the entire device (or Work profile, depending on device enrollment method). All apps except browsers would have to be added to Netskope Steering Exceptions.
You can start bypassing traffic from SSL inspection by adding exceptions.
To add a Certificate Pinned Application exception type, view
Certificate Pinned Application
. In the
Definition
field, you can select the
RegEX
option and add the desired app identifier.
Application ID can be found in GooglePlay Store as a part of its URL. An example below illustrates that CNN App is defined in PlayStore as
com.cnn.mobile.android.phone
.
Instead of adding every single application as an exception (which is not scalable) regular expressions could be used. The goal is to use least amount of configurations and describe applications in bulls. For example
com\.google\.android\..*
. This regular expression contains the following:
com.google.android.tts
com.google.android.apps.maps
com.google.android.calendar
com.google.android.gms
com.google.android.gms.persistent
com.google.android.webview
com.google.android.play.a.h.e
com.google.android.googlequicksearchbox
An example on how to bypass all Apps but Microsoft Edge will look like the following
:
^(?!.*(com\.microsoft\.emmx)).*$
An example on how to bypass all Apps but Microsoft Edge and Google Chrome will look like the following:
^(?!.*(com\.microsoft\.emmx|com\.android\.chrome|com\.sample\.application)).*$
While bypassing SSL inspection through Certificate Pinned Apps, you can either
Block
or
Bypass
traffic.
Traffic Steering Exceptions on Android and ChromeOS
Netskope steers all traffic except for ones configured as Certificate Pinned Application, Domain, and Destination Locations exceptions. Netskope validates the exceptions setup in the steering configured and bypass the traffic from the selected source and sent directly to their respective destination. If you want your Apps to be bypassed in the steering configuration you can configure it in
Settings
>
Security Cloud Platform
>
Steering Configuration >  Your <Steering Configuration> Exception
other than those that needs to be inspected by Netskope. To learn more, view
Exceptions
.
Uninstall Netskope Client In Android
The uninstallation of Netskope Client from your Android device with a personal account is simple:
Open the Google Play Store app.
Tap your Profile icon.
Tap Manage apps & devices > Manage.
Tap Netskope Client.
Tap Uninstall.
To learn more, view
Uninstall Apps in Android
.
Netskope restricts a user to uninstall Netskope Client (provisioned by your organization) from your Work profile.
Limitation
Netskope Private Access periodic re-authentication is not supported on Android and Chromebook.
In this Topic
Netskope Client For Android and ChromeOS

---
## Netskope Client Enforcement Using OneLogin
**URL:** https://docs.netskope.com/en/netskope-client-enforcement-using-onelogin/
**Last Modified:** 2025-08-31T01:48:08+00:00
**Scraped:** 2026-06-26T09:30:05.411289+00:00

Netskope Client Enforcement Using OneLogin - Netskope Knowledge Portal
Netskope Client Enforcement Using OneLogin
This document guides through the steps to configure the Netskope Client Enforcement application in OneLogin as a self-service option to deploy the Netskope Client.
This document demonstrates the use of Netskope Client enforcement with the pre-configured ‘AARP’ application within OneLogin. The outlined steps are applicable to any similar SaaS application.
The Application AARP is accessible to the end user only when the Netskope Client is active. The access to this application is denied if the Netskope Client is disabled or uninstalled.
Prerequisites
Import user email address information into Netskope tenant. You can add it under
Settings
>
Security Cloud Platform
>
Users
. To learn more, view
User Provisioning
.
Users are assigned to their respective applications in OneLogin.
Access and admin rights in the OneLogin tenant.
Access and admin rights in the Netskope webUI .
Before You Begin
Obtain Netskope Redirect URL and Organization ID
Log into your Netskope Tenant.
Go to
Settings
>
Security cloud platform
>
Netskope Client
>
Enforcement
.
Select
OneLogin
.
Copy the following values:
Netskope Redirect URL
Organization ID
Obtain Netskope IP Addresses
To obtain Netskope IP address:
Log into your Netskope Tenant.
Go to
Settings
>
Security cloud platform
>
Netskope Clien
t >
Enforcement
.
Select
OneLogin
.
Click
Netskope IP Ranges
to copy IP addresses.
OneLogin App Configurations
Perform the following OneLogin configurations to create SAML custom connector to allow Netskope Client download:
Log into
OneLogin
.
Go to
Applications
.
Click
Add App
.
In the Search box, type and select
SAML Custom connector (Advanced)
.
In
Add SAML Custom Connector (Advanced)
window, perform the following:
Add the display name. For example, Netskope Client Enablement.
Upload Netskope logo according to the aspect ratio mentioned on the webUI.
Add the description regarding the purpose of this application.
Click
Save
.
After you save, the webUI opens for more configurations such as Info, Configuration, Rules, and so on.
Click the
Configuration
tab.
Enter the following details according to the values captured from your Netskope tenant (See
here
to view how to obtain values from Netskope tenant):
RelayState: Enter your OneLogin tenant domain URL.
Audience (Entity ID): Enter the Organization ID from the Netskope tenant.
Recipient: Enter the Netskope Redirect URL.
ACS (Consumer) URL: Enter the Netskope Redirect URL.
Add other configurations as displayed in the following image:
Click the
SSO
tab.
Click
View Details
under
X.509 certificate
.
This opens a new webUI with the certificate.You can download the certificate.
Click
Save
.
To learn more, view:
Add apps to OneLogin
.
Upload Certificates in Netskope
Here, you can use the certificate downloaded from your OneLogin application.
To upload your certificate in the Netskope tenant:
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Enforcement
.
Click
Upload
available in the
OneLogin Public Key
field.
After you complete the process of creating your application, you can now assign this application to Users or User Groups within OneLogin.
This enables users to download and install Netskope Client whenever a user clicks the
Netskope Client Enablement
application that you created.
To learn more about adding users or user groups in OneLogin, view
Add Users
.
Configure IP Allowlist
You can configure IP Allowlist to enable access to SaaS Applications within OneLogin from Netskope IPs.
This step ensures that the SaaS Applications are restricted to be accessible from selective Netskope IPs only. If a user tries to access the Application in absence of Netskope Client, the access is denied.
To configure allowlist:
Log into OneLogin.
Go to
Security
>
Policies
.
Click
New App Policy
.
Add a name to the policy.
In the
IP Address Allowlist
, copy and paste the
Netskope IP addresses
captured from your Netskope tenant ( See
here
to view how to obtain Netskope IP addresses).
Click
Save
.
Assign Security Policy to OneLogin Application
In one login, go to
Applications
. For the context of this document, this policy is assigned to AARP application.
Under the selected application, go to the
Access
tab.
Choose the Policy that you had created in
Configure IP Allowlist
.
Click
Save
.
Validate Client Enforcement
Log into OneLogin using the ID that contains the Netskope client enablement application assigned.
Try accessing the AARP application in the absence of Netskope Client. The WebUI displays the following “
Access Denied
” notification.
If you click the Netskope Client enablement application, it redirects you to download the Netskope Client. This ensures that users are enforced to access the SaaS applications with Netskope Client enabled.
In this Topic
Netskope Client Enforcement Using OneLogin

---
## Use the NPA Client in Windows Multi-User Virtual Desktop Environments
**URL:** https://docs.netskope.com/en/use-the-npa-client-in-windows-multi-user-virtual-desktop-environments/
**Last Modified:** 2026-05-28T04:15:00+00:00
**Scraped:** 2026-06-26T09:30:41.761898+00:00

Use the NPA Client in Windows Multi-User Virtual Desktop Environments - Netskope Knowledge Portal
Use the NPA Client in Windows Multi-User Virtual Desktop Environments
This article explains how to configure Netskope Private Access (NPA) for multi-user virtual desktop environments on Windows, where users are logging in simultaneously, enabling secure access for environments with shared system processes (Session ID 0) and dedicated VDI user tunnels, through which a user’s private application sessions are processed through.
Introduction
In Virtual Desktop Infrastructure (VDI) environments, private application traffic originates from both interactive user sessions and system processes (Session ID 0). To address this, NPA introduces a dedicated
VDI User
that creates its own dedicated tunnel to steer traffic from the Netskope Client from processes that can’t be attributed to a user. This design ensures that private app packets, whether from user-initiated or system processes, are securely handled and routed based on defined policies.
Note
If you want to enable this feature, contact your sales team.
Supported Operating Systems
This feature is supported on Windows only. Ensure that your Windows servers and client devices are running a compatible version to fully leverage the NPA VDI support capabilities. Refer to our supported Windows versions here:
Netskope Client Supported OS and Platform
. Also, you need to ensure the platform supports multi-user sessions simultaneously.
Overview
The NPA VDI support solution is designed to:
Steer Session ID 0 Traffic separately from user traffic: Route system-level traffic (e.g., SMB or AD server packets) via a dedicated tunnel using a specially designated VDI user since it cannot be attributed to a user.
Enhance Multi-User Scenarios: Provide secure and consistent private access for environments like Azure Virtual Desktop, Amazon Appstream, and Citrix VDI.
Streamline Client Enrollment: Offers flexible enrollment workflows via UPN or integrated IDP, ensuring that devices receive the correct Client configurations for VDI mode.
Prerequisites
Before proceeding, ensure you have:
Netskope Tenant Access: Permissions to create users, configure Client settings, and set up policies.
VDI User Account: Create a dedicated VDI user using the format:
<username>@vdi.netskope.com
Installer Requirements: Use the latest Client installer build (Build Version: 124+).
Note
Upgrading the current Client does not support VDI mode; a fresh installation is required.
Command Line Access: Required for installing the Client with appropriate flags.
Ensuring Proper VDI Configuration with npavdimode=on
For organizations deploying the Netskope Client in VDI environments, it is essential to enable multi-user support by specifying
npavdimode=on
during installation. This ensures that the appropriate VDI settings are applied, allowing for seamless configuration and operation.
Key Implementation Steps
During Installation:
When installing the Netskope Client on Windows devices, ensure the installer is launched with
npavdimode=on
.
This setting is required for multi-user environments and ensures the correct application of VDI configurations.
Client Enrollment Considerations:
Whether using
UPN Enrollment Mode
(via corporate directory services) or
IDP Enrollment Mode
(leveraging SSO with providers like Azure AD or Okta), the
npavdimode=on
flag must be included to properly configure VDI settings.
Enrollment workflows remain unchanged, but without this setting, multi-user functionality may not be properly applied.
The same configuration parameter needs to be applied when using a MDM-based deployment method.
Configuration Enforcement:
After authentication and device registration, the security cloud platform applies the necessary settings, ensuring that VDI users receive the correct configuration.
For full deployment details, refer to the Netskope client enrollment documentation links:
Deploy Netskope Client via IDP
Netskope Client for Windows
Setup Guide
Web UI Configuration
1. Add the VDI user:
Go to
Setting > Security Cloud Platform > Users
and click
New User
.
User Email Format: Enter the email as
<username>@vdi.netskope.com
.
Click A
dd
. This VDI user is solely used for establishing a dedicated tunnel for Session ID 0 traffic.
2. Create or edit a Client configuration:
Access Client Configurations: Create a new configuration or modify an existing one. Go to
Settings > Security Cloud Platform > Client Configuration
and click
New Client Configuration
.
On the
Private App Segment
tab:
Enable VDI Support: Check the
VDI Support for Private App Segments
option.
Select a VDI User: Use the search in th dropdown (displaying only users with “vdi.netskope.com”) to select the appropriate VDI user. The option to proceed is locked until a VDI user is selected.
Click
Save
.
3. Create a Private App policy:
Go to
Policies > Real-Time Protection > New Policy > Private App Segment Access
.
Policy Settings:
Source: Set to the VDI user (e.g.,
<username>@vdi.netskope.com
).
Access Method: Use the Client.
Destination: Private App Segment, and select the apps (like SMB fileshare, DNS, etc.) that generate Session ID 0 packets.
Action: Set to
Allow
to enable traffic via the dedicated tunnel.
Click
Save
.
Additional Steps: Optionally configure file/folder access rules on your SMB server to control user access.
Client Installation
1. Uninstall the Existing Client and Remove Previous Versions: Ensure any existing Netskope Client is uninstalled from the VDI server.
2. Install the New Client Build:
Download Build 124+: Confirm that you are using the latest installer.
Run the installation command using administrative permissions:
msiexec /I "NSClient.msi" host=
<addon host URL>
token=
<org id>
mode=peruserconfig npavdimode=on
Note
The
npavdimode=on
flag is required to enable VDI support when simultaneous user sessions will be active on this virtual desktop only.
When Secure Enrollment is enabled, you must provide both the authentication token (
enrollauthtoken
) and the encryption token (
enrollencryptiontoken
) in the installer command for secure enrollment of NPA VDI users.
3. Establish a User Session
Log Out and Log In: After installation, sign out and log back in to create a new user session.
Tunnel Creation: The first user session triggers the creation of a dedicated VDI tunnel for Session ID 0 traffic.
Verification: Check client logs (e.g.,
npadebuglog
) to confirm that the tunnel is active and the VDI user is properly enrolled.
Best Practices
Due to the nature of shared Session ID 0 traffic, it is important to adopt the following best practices:
Group Users by Access Profile: To minimize security risks and performance bottlenecks, group users on a multi-user virtual desktop machine based on their access profile.
Rationale: Since Session ID 0 traffic is shared among all users on the VM, grouping users with similar access needs can reduce potential conflicts and streamline policy enforcement.
Implementation: Consider deploying separate VMs or virtual desktop pools for different access profiles (e.g., administrative vs. standard user access). This ensures that private app policies and resource utilization are aligned with user requirements.
Consistent VDI User Assignment: Ensure that every Client Configuration that requires this functionality support has a single designated VDI user. Configuration scenarios where multiple multi-user desktop environments are assigned to user groups with different VDI tunnel users is not supported. This consistency prevents disruptions in the dedicated tunnel due to configuration changes.
Regular Monitoring: Monitor the tunnel status and user sessions to quickly identify and address issues related to Session ID 0 traffic routing or policy mismatches.
Configuration Considerations
Steering Configurations:
Steering functions (enable/disable steering) are not applicable to VDI tunnels.
Steering and client configurations are applied uniformly, regardless of individual policy matches.
Device Classification: Adding device classification for tunnels with a VDI user does not impact policy matching.
Unsynced Users: It is expected that users not synchronized with Netskope may still access VDI tunnel traffic.
Upgrade Process: Upgrading an existing Netskope Client will not enable VDI mode; a fresh installation is required.
SRPv2 Support: Service Routing Protocol v2 (SRPv2) is not supported in the current release and will be added in April 2025.
Additional Notes and Support
Tunnel Persistence: The VDI tunnel remains active as long as at least one user is logged into the VDI system. It disconnects only when the last user logs out. The prelogon user will be active if configured before a user session is established.
User Deletion Restrictions: If a VDI user is assigned to a client configuration, that user cannot be deleted from the Users page to maintain tunnel stability.
Troubleshooting: Review the
npadebug.log
file for detailed log entries regarding tunnel creation and user enrollment.
Further Assistance: For additional help, contact Netskope Support.
In this Topic
Use the NPA Client in Windows Multi-User Virtual Desktop Environments

---
## Deploy Client On Windows Using Intune with Win32 App
**URL:** https://docs.netskope.com/en/deploy-client-on-windows-using-intune-with-win32-app/
**Last Modified:** 2026-03-20T06:27:48+00:00
**Scraped:** 2026-06-26T09:31:29.845328+00:00

Deploy Client On Windows Using Intune with Win32 App - Netskope Knowledge Portal
Deploy Client On Windows Using Intune with Win32 App
This article provides instructions to deploy Netskope Client on Windows devices (either joined to Active Directory or Microsoft Entra ID) using the Microsoft Intune Win32 app.
Prerequisites
Import users into Netskope using Directory Importer or SCIM integration.
Convert the MSI Netskope Client package file to
.intunewin
format. To learn more, view
Prepare Win32 app content for upload
.
Ensure the device is enrolled in Microsoft Intune.
Deployment Procedure
To deploy Netskope Client With Win32 App, perform the following instructions:
Log in to the
Azure Portal
(portal.azure.com).
Click
More Services
.
From the left-pane, click
Intune
.
From the main pane, right-click the
Intune
option and open it in a new tab. This redirects you to
endpoint.microsoft.com
.
From Microsoft Endpoint Manager admin center, select
Apps
>
All Apps
.
Select
+ Add
.
For
App Type
, select
Windows app (Win32)
.
Click
Select
.
This navigates to
Add App
.
Under
App Information
, perform the following:
In
Select file
, click
Select App Package file
.
This opens a separate window.
In
App package file
upload the
.intunewin
file.
Click
OK
.
Name:
Enter the name for the application. For example, Netskope Client Win32.
Description:
Enter the description of the application.
Publisher:
Enter the name of the publisher of the application.
Show this as a featured app in the Company Portal:
Toggle to enable this option. Use this option to display the application on the main page of your organization portal where users browse for apps.
Click
Next
.
Under
Program
, perform the following:
Install Command:
Enter the MSIEXEC command in the following format:
msiexec /I NSClient.msi token=<organization id> host=addon-<tenant-name>.goskope.com mode=peruserconfig enrollauthtoken=<your enrollauthtoken> enrollencryptiontoken=<your encryption token> autoupdate=on /qn
For example, if you are using IDP, enter the following command:
msiexec /I NSClient.msi installmode=IDP tenant=corp domain=eu.goskope.com /qn
To learn more about other MSI command, view
Netskope Client for Windows
.
– Use
mode=peruserconfig
only in multi-user environments.
– Use
autoupdate=on
only if you want to update Netskope Client automatically.
Uninstall Command:
Enter the MSIEXEC command in the following format:
msiexec /I NSClient.msi <Product code> /qn
To get the product code, run the following command in the command prompt:
wmic product where "Name like '%Netskope%'" get Name,Version,IdentifyingNumber
Click
Next
.
Under
Requirements
, enter the following:
Set the
Operating system architecture
to 64-bit.
Set the
Minimum operating system
to Windows 10 1607.
Click
Next
.
Under
Detection Rules
, perform the following:
Select
Manually configure detection rules
from the drop-down options in
Rules format.
Click
+Add
.
This opens a separate window:
Detection Rule
.
Select
Rule Type
as
File
.
Set
Path
to:
For a 32-bit Netskope Client:
C:\Program Files (x86)\Netskope\STAgent
For a 64-bit Netskope Client:
C:\Program Files\Netskope\STAgent
Add
stAgentSvc.exe
in
File or Folder
.
Select
Detection method
as
File or folder exists
.
Click
Next
.
Under
Dependency
, click
Next
.
Under
Supersedence
, click
Next
.
Under
Assignment
, perform the following:
Under
Required
, click
Add group
to add appropriate groups that need to be included.
Click
Next
.
Under
Review + Create
, click
Create
to review and complete the process.
You can monitor the installation process from Intune.
Go to
Apps > Windows > Windows | Windows Apps >
Search for Netskope
> Device Install status.
To learn more, view
Configure Win32 App in Intune
.
Uninstall Netskope Client In Intune
To set up un-installion script for Netskope client in Windows devices follow the procedure as described in this section:
This procedure is applicable only for devices that are AD joined. Also, during subsequent installation, un-assign this app to avoid un-installation of the newly installed Clients.
Select an existing Windows app in
Apps
>
All Apps
.
Go to
Properties
.
Ensure that you have added the uninstall command under
Programs
. If not added, click
Edit
in the
Programs
section and add
the command to remove Netskope Client from the end-user device.
To add the Uninstall Command, enter the MSIEXEC command in the following format:
msiexec /I NSClient.msi <Product code> /qn
To get the product code, run the following command in the command prompt:
wmic product where "Name like '%Netskope%'" get Name,Version,IdentifyingNumber
Under the
Assignments
section, click
Edit
.
Under
Uninstall
, click
Add group
to add appropriate groups that need to be removed.
Ensure that you do not add the same group added under the
Required
section.
Go to
Devices
>
All Devices
.
Select the specific device where you need to uninstall Netskope Client.
Click the
Sync
option.
Go to the endpoint machine Accounts → Access work or school → select info under account name and click sync option. Wait till you receive the command from Intune.
In this Topic
Deploy Client On Windows Using Intune with Win32 App

---
## Netskope Client Deployment Parameters
**URL:** https://docs.netskope.com/en/netskope-client-deployment-parameters/
**Last Modified:** 2025-08-31T01:48:17+00:00
**Scraped:** 2026-06-26T09:32:09.556320+00:00

Netskope Client Deployment Parameters - Netskope Knowledge Portal
Netskope Client Deployment Parameters
This document can assist administrators identify values needed for various deployment methods.
Commonly Used Parameters
Description and WebUI Location
Organization ID
OrgKey
token
These parameters represent the
Organization ID
available in the
MDM Distribution
webUI in your tenant.
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distribution
.
You can find the
Organization ID
under
Deployment Resources for iOS
>
Create VPN Configuration
.
The Organization ID varies with each tenant.
host
AddonHost
addon-<FQDN used to login to the Netskope tenant>
For example, if administrators access Netskope admin console through
acme.goskope.com
then addon URL is
addon-acme.goskope.com
.
VPN server address
Server
These represent the
VPN Server Name
URL in the
MDM Distribution
webUI in your tenant.
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distribution
.
You can find
VPN Server Name
under
Deployment Resources for iOS
>
Create VPN Configuration
.
tenant
If the tenant URL is
acme.eu.goskope.com
, tenant value is
acme
.
domain
If the tenant URL is
acme.eu.goskope.com
, then domain is
eu.goskope.com
.
Authentication token
Encryption token
These represent the Secure Enrollment tokens required to deploy Netskope Client.
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distribution
.
Go to
Secure Enrollment
.
In this Topic
Netskope Client Deployment Parameters

---
## Deploy Netskope Client with Endpoint Central on Windows
**URL:** https://docs.netskope.com/en/deploy-netskope-client-with-endpoint-central-on-windows/
**Last Modified:** 2025-08-31T01:48:31+00:00
**Scraped:** 2026-06-26T09:32:55.112962+00:00

Deploy Netskope Client with Endpoint Central on Windows - Netskope Knowledge Portal
Deploy Netskope Client with Endpoint Central on Windows
This document describes the instructions to deploy Netskope Client using Endpoint Central on Windows devices.
Prerequisites
Install Endpoint Central agent installed in Windows devices.
Download the desired version of the Netskope Client installer for Windows (Golden Release is recommended). Refer
Support
to download the file.
The Windows system with active network connectivity:
Connection to distribution server (On-premises or Endpoint Central Cloud (depending on configuration).
Internet required for direct connection to Endpoint Central Cloud).
Supported Environments
Windows Version
Deployment Mode
Windows 10, 11
AD-joined
Windows 10, 11
IDP
Deployment Procedure
Refer to the following sections to deploy Netskope Client using Endpoint Central.
Create Application Package
To create an application package:
Login to Endpoint Central Cloud Instance at
https://endpointcentral.manageengine.com
.
Navigate to
Software Deployment
>
Packages
.
Click
Add Package
and select
Windows
from the dropdown menu.
Enter the following details:
Package Name:
For example, NSclient for Windows (AD-Joined)
Package Type:
Select MSI/MSP.
License Type
: Select Commercial
Locate Installable:
You can either upload the package from the shared folder or from your local computer.
Click the
Installation
Tab.
MSI / MSP File Name = NSClient.msi
Pre-Deployment Activities = leave blank
Post Deployment Activities = leave blank
MSI / MSP Properties for Installation = Add depending on the
Netskope Client MSIEXEC Commands
.
Example Screenshot for AD-Joined / Silent install
Click
Save
.
Create Installation Script
To create the installation script:
Navigate to
Software Deployment
>
Packages
.
Click the ellipsis (
…
) in the
Action
column to the right of your newly created package.
Select
Install Software – Computer
from the dropdown options.
This navigates to
Install/Uninstall Windows Software (Computer)
.
Enter the following details:
Name:
Install Netskope Client for Windows (or similar)
Package Settings:
Operation Type
: Install.
Package Name:
This is pre-filled for you with the name of the package you created earlier in
Create Application Package
.
Under
Configure Install / Uninstall Options
>
Install As
: Select
System
User
.
Under
Deployment Settings
, select a policy according to your preference in
Apply Deployment Policy
.
In
Define Targe
t, define the target workstations where you want to deploy the configuration. To define a target, view
Defining Targets
.
In
Execution Settings
(Optional), choose the timeframe in which you want to apply the configuration. To learn more, view
Define Execution Settings
.
Click to
Deploy
,
Deploy Immediately
or
Save
(as Draft or Template).
In this Topic
Deploy Netskope Client with Endpoint Central on Windows

---
## Deploy Netskope Client with Endpoint Central on MacOS
**URL:** https://docs.netskope.com/en/deploy-netskope-client-with-endpoint-central-on-macos/
**Last Modified:** 2025-08-31T01:48:32+00:00
**Scraped:** 2026-06-26T09:32:56.248628+00:00

Deploy Netskope Client with Endpoint Central on MacOS - Netskope Knowledge Portal
Deploy Netskope Client with Endpoint Central on MacOS
This document describes the instructions for the silent deployment of  Netskope Client using Endpoint Central on MacOS devices.
Prerequisites
Install Endpoint Central agent installed in MacOS devices.
Download the desired version of the Netskope Client installer for MacOS (Golden Release is recommended). Refer
Support
to download the file.
Download the Root and Intermediate certificates from your tenant. To download the Root and Intermediate certificates, go to
Settings
>
Manage
>
Certificates
>
Signing CA
.
Download the script
NetskopeEndpointCentral.mobileconfig
from the
Support
portal and make the following changes in the script:
#LINES 12 – 33: Replace with contents of rootCaCert file. Do not copy BEGIN or END lines
#LINES 53 – 78: Replace with contents of caCert file. Do not copy BEGIN or END lines
#LINE 83: Replace with <tenantname>.goskope.com. For example, ca.netskopecorp.goskope.com.
#LINE 133: Replace with gateway-<tenantname>.goskope.com. For example, gateway-netskopecorp.goskope.com.
Download the preinstall script
ns-preinstall-endpointcentral.sh
from the
Support
portal and make the following changes in the script:
#LINE 14: Replace with the correct addon-<tenantname>.goskope.com domain.
#LINE 15: Replace with the correct ORGID from your tenant.
To get the ORGID and tenant name, view
Client Deployment Parameters
.
The MacOS system with active network connectivity.
Connection to distribution server (On-premises or Endpoint Central Cloud (depending on configuration).
Internet required for Direct Connection to Endpoint Central Cloud.
Supported Environments
Supported OS:
MacOS Ventura or later
– Netskope does not recommend UPN-based for any MacOS platform. This mode requires active connectivity to the Active Directory environment during install. Without it, the installation will complete in a corrupted state and will not activate – even if the system can reach Active Directory after the install.
– Silent installation is recommended for Multi-user MacOS systems with IDP based enrollment.
Deployment Procedure
Refer to the following sections to deploy Netskope Client using Endpoint Central.
Create Application Package
To create an application package:
Login to Endpoint Central Cloud Instance at
https://endpointcentral.manageengine.com
Navigate to
Software Deployment
>
Packages
.
Click
Add Package
and select
Mac
from the dropdown menu.
Enter the following details:
Package Name:
For example, Netskope Client for MacOS
License Type
: Select Commercial
In the
Installation
tab, browse and upload the package file downloaded from the Support portal in Upload Files.
Click
Add Package.
Create Configuration Profile For Silent Install
To create the configuration profile:
Navigate to
Mobile Device Management
from the top menu.
Click on
Management
>
Profiles
.
Click
+Create Profile
>
macOS
.
This navigates to
Create macOS Profile
.
Enter the
Profile name
. For example, Netskope MacOS Pre-Reqs.
Click
Continue
.
This navigates to
Configure Profile
.
On the left-hand panel, scroll down and click
Custom Configuration
.
In the Custom Configuration profile , click
Browse
and upload the NetskopeEndpointCentral.mobileconfig file that you downloaded and edited previously.
Click
Save
.
Click
Publish
.
On the left-hand panel, click
Groups & Devices
.
Click the name of the device group you wish to target.
Click
Action
on the far right and choose
Associate Profile
from the dropdown options.
Choose your Prerequisite Profile and click
Associate.
Confirm the presence of the configuration profile on your MacOS device.
Configure the Preinstall Script
To configure the preinstall script:
Navigate to
Configurations
from the top menu.
Click
All Configurations
.
Click
+Create Configuration
.
Select
Mac
from the dropdown options.
Hover over
Custom Script
and select the
Computer Configuration
option.
Enter the
Name
for the script. For example, Netskope Pre-Install for MacOS.
In
Execute Script from / Run
, choose
Repository
.
In
Script Name
, click the
Create / Modify Script
link. This launches a new window.
Click
+Add Script
.
In
Script Name
, browse and upload the preinstall script.
In
Platform
, select
Mac
.
Click
Add
.
Confirm the script is now listed in the repository then close the new tab to return to the previous screen.
Click in the
Script
Name
box and you can select the newly uploaded script.
In
Frequency
, you can optionally enable logging for troubleshooting.
In
Define Targe
t, define the target workstations where you want to deploy the configuration. To define a target, view
Defining Targets
.
Click
Deploy
.
In this Topic
Deploy Netskope Client with Endpoint Central on MacOS

---
## Deploy Client On Android Using Intune
**URL:** https://docs.netskope.com/en/deploy-client-on-android-using-intune/
**Last Modified:** 2025-08-31T01:48:27+00:00
**Scraped:** 2026-06-26T09:35:01.733815+00:00

Deploy Client On Android Using Intune - Netskope Knowledge Portal
Deploy Client On Android Using Intune
This documents illustrates the procedure to deploy Netskope Client in Android devices using Intune.
Prerequisites
In the Netskope UI, go to
Settings
>
Manage
>
Certificates > Signing CA.
Download the Netskope Root and Intermediate Certificates.
To locate Organization ID, go to
Settings
>
Security Cloud Platform
>
MDM Distribution
. Scroll down to
Create VPN Configuration
section to find your
Organization ID
.
User accounts provisioned within MDM/EMM platform must match those provisioned in the Netskope tenant.
Bind Android for Enterprise with Intune
Before you begin, ensure that you have configured Android for Enterprise binding for Microsoft Intune. This is done from the MS Endpoint Manager (https://endpoint.microsoft.com/).
Log into the
Endpoint Manager admin center
, go to
Devices
>
Android
and select
Android Enrollment
.
Click
Managed Google Play
.
Select the
I agree
checkbox and click the
Launch Google to Connect now
button. In the Google Play pop-up window, complete the business registration steps.
After registration is complete, go to MS Endpoint Manager admin center, click
Devices
>
Android
>
Android Enrollment
>
Managed Google Play
to verify the registration process. If successful, the Status label will display Setup with a green tick.
In the
Android Enrollment
page, select the
Enrollment Profile
to get the token that you can share with users for enrollment.
Approve Netskope Client
Log in to your
Google Play Store
account and search for Netskope Client.
Click
Approve
send authorization to MS Endpoint Manager.
Setting up Apps in MS Endpoint Manager
In the
MS Endpoint Manager admin center
, go to
Tenant Administration
>
Connectors and Token
page.
Select
Managed Google Play
and click
Sync
to get all approved apps listed in Intune
Apps
>
All Apps
.
Deploy Netskope Client
Netskope Client can be deployed to users or user groups as an optional or mandatory deployment action.
In the
MS Endpoint Manager admin
console, go to
Apps
>
All Apps
and select
Netskope Client
.
Click
Properties
and then click
Assignments
.
Select the user groups or users to which the app is to be deployed in the
Required
section (options
+Add group
, +Add all users,
+Add all devices
) and click
Review+Save
, and then click
Save
.
Select the appropriate deployment action and click
Save
.
Create App Configuration and Deploy
In the following sections, create app configuration policies using UPN and IDP modes:
UPN – All enrollment data is supplied by Intune. No action is required from the user since they are enrolled using zero touch enrollment.
IDP – The user needs to click on the Netskope Client to authenticate.
Perform the following instructions to create an app configuration policy using:
UPN
To create app configuration policy:
In the MS Endpoint Manager admin center, go to
Apps
>
App Configuration Policy
and click
+ Add
and select
Managed Devices
.
In the
Basics
section of the
Create app configuration policy
page, enter the following details and click
Next
.
Name:
Give a name to the policy.
Platform:
Android Enterprise
Associated App:
Select Netskope Client
In the
Settings
section of the
Create app configuration policy
page, locate
Configuration Settings
and select the
Use configuration designer
option from the
Configuration settings
format dropdown list.
Click Add and select the following mandatory values and click OK.
User Email Address: {{mail}}
If UPN is being synced to  Netskope from AD, use the key:value pair –
User Email Address: {{userPrincipalName}}
.
For environments where user context is not available (i.e. shared devices, kiosks) static email addresses should be used. This email should match provisioned user account email in Netskope tenant
Host: <addon-
<tenant-URL>
Token:
<Organization Key>
enrollauthtoken: <Secure Enrolment Authentication Token>
enrollencryptiontoken: <Secure Enrolment Encryption Token>
– The Organization ID is case-sensitive.
– ns_mdm_check is an optional value that is used for Android device classification purposes. If you are not doing device classification for Android, you can safely ignore this field.
In the
Assignments
section of the
Create app configuration policy
page, select groups from the
Assign to
dropdown menu to which the policy is applied. Assuming the option selected was Selected Groups, select include the Microsoft Entra ID groups that this policy will apply to and click
Next
.
You can also select groups that can be excluded from this configuration policy.
In the
Review + create
section of the
Create app configuration policy
page, review the configuration and click
Create
.
Enroll the Android devices to the Intune Company Portal application available on Google Play.
IDP
To create app configuration policy:
In the MS Endpoint Manager admin center, go to
Apps
>
App Configuration Policy
and click
+ Add
and select
Managed Devices
.
In the
Basics
section of the
Create app configuration policy
page, enter the following details and click
Next
.
Name: Give a name to the policy.
Platform: Android Enterprise
Associated App: Select Netskope Client
In the
Settings
section of the
Create app configuration policy
page, locate
Configuration Settings
and select the
Use configuration designer
option from the
Configuration settings format
dropdown list.
Click
Add
and select the following mandatory values and click OK.
Tenant:
<tenant-name>
In the
Assignments
section of the
Create app configuration policy
page, select groups from the
Assign to
dropdown menu to which the policy is applied. Assuming the option selected was
Selected Groups
, select include the Microsoft Entra ID groups that this policy will apply to and click
Next
.
You can also select groups that can be excluded from this configuration policy.
In the
Review + create
section of the Create app configuration policy page, review the configuration and click Create.
Enroll the Android devices to the Intune Company Portal application available on Google Play.
Enable Zero-touch Enrollment
The following steps enable zero-touch enrollment of Android devices with Microsoft Intune after the deployment of Netskope Client. This also enables SSL inspection with the presence of the trusted CA certificates in the user store.
Create Trusted Netskope Root Certificate Profile
Create Device Restrictions Profile
Create a Trusted Netskope Root Certificate Profile
Download the Netskope Root and Intermediate certificates from the Netskope UI to complete these steps. To get the certificate, go to
Settings
>
Manage
>
Certificates > Signing CA
.
The Netskope Root certificate is in .pem format. You will need to convert it to .cer or .crt format before importing it. Rename the file to convert from .pem to .cer format.
To create a trusted Netskope certificate profile:
In Intune UI proceed to
Devices
>
Android
>
Configuration profiles
.
Click
Profile
>
Create Profile
. Enter and select these parameters:
Name:
Enter a unique name.
Platform:
Android Enterprise
Profile type:
Trusted certificate
In the
Trusted Certificate
panel, provide a name in the
Basics
tab and click
Next
.
In the
Configurations settings
tab, upload the Netskope Root certificate.
Review your settings, and click
Create
.
Create Device Restriction Profile
Adding a device restriction profile helps administrators to set policies to control and manage Android devices in their organization. To learn more, view
Device Restriction
.
To add a device restriction profile:
Go to
Devices
>
Android
>
Configuration Profiles
>
Create Profile
.
In Create a Profile, select the following:
Platform:
Android Enterprise
Profile Type
: Device Restrictions
Click
Create
.
In
Basics
, enter a descriptive name for the profile and click
Next
.
In
Configuration settings
, expand Connectivity and enter the following:
Always-On VPN: Toggle
Enable
to select this option.
VPN Client: Select Custom.
Package ID: com.netskope.netskopeclient
Lockdown mode: Toggle Not configured to select this option.
Click
Next
.
Add the appropriate profile assignments  and click
Next
.
Review the configuration and click
Create
.
Enrollment Workflow
After the deployment is complete, Netskpe Client can enroll silently(assuming the enrollment data is correct and is matching the user information provisioned in the tenant). The VPN profile serves as the binding mechanism between source mobile applications and Netskope Client as secure connectivity provider.
Uninstall Netskope Client
This section describes the steps to uninstall Netskope Client from your Android devices.
Create a Security Group
Netskope recommends creating a security group adding the desired devices or users before you uninstall Netskope Client.
To create a security group:
Go to
Groups
>
All Groups
.
Click
New Group
.
Enter the following information:
Group Type: Security
Group Name: For example, Android Uninstall
Membership Type: Assigned
Add members by clicking
No members selected
.
Another window
Add Members
appears.
Add the desired users or groups or devices here.
Click
Select
to close this window.
The
New Group
screen displays the selected members.
Click
Create
.
Uninstall Managed App
After you create the security group, navigate to the uninstall section of the managed app that you wish to remove.
To uninstall:
Go to
Apps
>
Android
.
Select the already installed app. Select Netskope Client.
Click
Properties
.
Click
Edit
in the
Assignments
section.
From
Uninstall
, click +
Add Group
and include the security group that you created earlier.
Click
Review+Save
.
Wait for the device to sync and verify that the app is uninstalled.
In this Topic
Deploy Client On Android Using Intune

---
## Deploy Client on Android Using Omnissa Workspace ONE
**URL:** https://docs.netskope.com/en/deploy-client-on-android-using-vmware-workspace-one/
**Last Modified:** 2026-06-10T06:09:55+00:00
**Scraped:** 2026-06-26T09:35:02.864025+00:00

Deploy Client on Android Using Omnissa Workspace ONE - Netskope Knowledge Portal
Deploy Client on Android Using Omnissa Workspace ONE
This article describes how to deploy Netskope Client on Android devices using Omnissa Workspace ONE.
Prerequisites
Administrators must possess proficient working knowledge of Omnissa Workspace ONE UEM.
Administrators must review
Netskope Client Client Enrollment Methods
to understand the Client User Enrollment methods available for their environment.
Import users into the Netskope tenant – see
Provisioning Users for Netskope Client
.
Download
Netskope Root and Tenant Certificates
and ensure the certificates are available when needed.
See
Deploy Netskope Client via IdP
when using IDP as the method of user enrollment.
Login to Workspace ONE UEM console and register your Android enterprise through Managed Google Play Accounts. To learn more, view
Registering your Android device
.
Supported Platforms
This article outlines the Netskope Client deployment instructions for the following user enrollment methods and supported platforms. User enrollment methods not documented here are not supported at this time.
Workspace ONE UE Version: Workspace ONE UEM version 9.4 and later.
Netskope Client Playstore Version: 96.0.0.1009
Configure Omnissa Workspace One for Android Enterprises
To use Android Enterprise devices in Omnissa Workspace One, set up a Managed Google Play account.
Android Enterprise Modes
Netskope supports the following Android device modes:
Android Managed
Android BYOD
Android COPE
To learn more about different Android device modes, view
Device Modes
.
Deploying Android Applications
Perform the following steps to deploy your Android applications:
Go to
Resources
>
Apps
>
Native
>
Public
>
+Add Application
.
Provide the mandatory fields and click
Next
.
Select
Netskope Client
.
Click
Approve
.
In the
Edit Application – Netskope Client
, check the existing details.
Click
Save and Assign
.
In the
Netskope Client – Assignment
page, assign your Netskope Client to a device mode.
Click
Create
.
Click
Save and Publish
the Netskope Client to the web.
Click
Deployment
to configure the application and control availability.
Enter these parameters:
Push Mode: Set the application to install automatically (auto) or manually (on demand) when needed.
Send Application Configuration: Enable this checkbox.
Application Configuration: Enter the Configuration key/value information for these fields:
Email Address: {EmailAddress}
For environments where user context is not available(such as shared devices, kiosks), use static email addresses. This email must match provisioned user account email in Netskope tenant.
token: <Orgkey> (Organization ID in the Netskope UI)
host: addon-<tenant hostname>.goskope.com
enrollauthtoken: ​​ Enter the Authentication Token.
​​enrollencryptiontoken:​​ Enter the Encryption token.
Zero Touch Enrollment using VPN Profile
The custom VPN profile is a list of key-value pairs that you can add in the configuration to enable the silent enrollment for your Android devices. Creating a VPN profile from Omnissa Workspace ONE address the following challenges:
After you deploy Client for Android devices and complete the enrollment process, you need to accept Notification and Permission prompts to create the VPN profile.
Preventing users from disabling the connectivity through Netskope.
Create a VPN profile irrespective of the approach that you take to deploy Client in Android devices.
To create a VPN profile:
In Workspace One UEM console, click
Resources
>
Profiles
>
Add
>
Add Profile
.
Click
Android
.
Provide a name for the profile. For example, Netskope Android VPN.
Expand the
Custom Settings
option and click
Add
.
Copy-paste the following code snippet in the text field.
<characteristic uuid="00000000-0000-0000-0000-000000000000" type="com.airwatch.android.androidwork.app:com.netskope.netskopeclient">
<parm name="profileName" value="VPN" type="string" />
<parm name="action" value="0" type="string" />
<parm name="EnableAlwaysOnVPN" value="True" type="boolean" />
<parm name="LockDown" value="false" type="boolean" />
<parm name="EnableLockDownWhitelist" value="True" type="boolean" />
<parm name="LockdownWhitelistedPackageIds" value="com.netskope.netskopeclient" type="string" />
<parm name="authentication_type" value="2" type="string" />
</characteristic>
Include
com.netskope.netskopeclient
in the
LockdownWhitelistedPackageIds
for the
LockDown
mode. Append the certificate pinned applications configured in your steering configuration to this list. For example, if you want to bypass traffic for Example App1 with package ID: com.example.app1 and Example App2 with package ID com.example.app2, then append the package IDs for these two apps to the list by using a “;” separator (no space required between package IDs).
<parm name="LockdownWhitelistedPackageIds"value="com.netskope.netskopeclient;com.example.app1;com.example.app2"type="string"/>
Expand
Credentials
and click
ADD
.
Upload the root certificate details required for successful SSL interception.
Click
Next
.
In the
Assignment
section, assign the profile to a smart group from the list of options given in the
Smart Group
drop-down menu.
Click
Save and Publish
.
In this Topic
Deploy Client on Android Using Omnissa Workspace ONE

---
## Deploy Client on Windows Using Omnissa Workspace ONE
**URL:** https://docs.netskope.com/en/deploy-client-on-windows-using-omnissa-workspace-one/
**Last Modified:** 2026-02-15T13:48:33+00:00
**Scraped:** 2026-06-26T09:35:03.964911+00:00

Deploy Client on Windows Using Omnissa Workspace ONE - Netskope Knowledge Portal
Deploy Client on Windows Using Omnissa Workspace ONE
This article describes how to deploy Netskope Client on Windows devices using Omnissa Workspace ONE.
Prerequisites
Administrators must possess proficient working knowledge of Omnissa Workspace ONE UEM.
Administrators must review
Netskope Client Client Enrollment Methods
to understand the Client User Enrollment methods available for their environment.
Import users into the Netskope tenant – see
Provisioning Users for Netskope Client
.
Download
Netskope Root and Tenant Certificates
and ensure the certificates are available when needed.
See
Deploy Netskope Client via IdP
when using IDP as the method of user enrollment.
Supported Platforms and Enrollment Methods
This article outlines the Netskope Client deployment instructions for the following user enrollment methods and supported platforms. User enrollment methods not documented here are not supported at this time.
Enrollment Method
Single-User
Multi-User
IDP
Y
Y
UPN
Y
Y
Client Deployment
This section describes the instruction to upload the .msi file and add the install command to deploy Netskope Client.
To upload the Client installer file:
Navigate to
Resources
>
Apps
>
Native Apps
.
In the
Internal
tab, click
Add
>
Application File
.
In the
Add Application
pop-up:
In
Application File
, click
Upload
and choose the Netskope Client installation file (with the msi extension). Download the latest installation files from
Netskope Support
.
After selecting the file, click
Save
to continue.
Select
No
in
Is this a dependency app?
.
Click
Continue
.
The system displays the details of the uploaded installer file.
In the
Details
tab, leave the form data with the default values.
In the
Deployment Options
tab, scroll down to the
Install Command
field under How To Install and enter the MSIEXEC command in the following format:
msiexec /I NSClient.msi tenant=<tenant-name> domain=[region.]<tenant-domain> enrollencryptiontoken=<Encryption Token> /qn
For example,
msiexec /I NSClient.msi tenant=corp domain=goskope.com installmode=IDP enrollencryptiontoken=XXX /qn
To learn more about MSIEXEC configuration options, view
Netskope Client for Windows
.
Ensure that you end the command with the
/qn
parameter for silent and uninterrupted installation. Leave all other options with default values.
Click
Save
and Assign
.
From the
Assignment
page, enter the following details:
Name:
Specify a name for this delivery or deployment.
Description:
Optional parameter to add more information about the deployment.
Assignment Groups:
Select the groups in your organization to deploy the Client.
Deployment Begins:
Time to start the deployment. Leave the default options as is.
App Delivery Method:
Select Auto or On-Demand. Auto option will auto deploy client at the configured time. On-Demand can be used to deploy only when required for specific devices or groups.
Click
Create
.
From the
Assignment
details page, click
Save
.
From
Preview
of the Assigned Devices, click
Publish
.
After completing the deployment, go to
Resources
>
Native.
Click the uploaded client.
The system displays a pop-up window with the deployment status.
In this Topic
Deploy Client on Windows Using Omnissa Workspace ONE

---
## Netskope Client Command Reference
**URL:** https://docs.netskope.com/en/netskope-client-command-reference/
**Last Modified:** 2026-02-19T16:34:49+00:00
**Scraped:** 2026-06-26T09:35:05.116478+00:00

Netskope Client Command Reference
The Netskope Client
nsdiag
utility is a diagnostic and troubleshooting tool installed on end-user devices alongside Netskope Client.  This section lists the available
nsdiag
commands.
Diagnostics Commands (Windows, macOS, and Linux)
The diagnostics command is available using the
nsdiag
command in Microsoft Windows, macOS, and Linux devices. The command is located in the Client installation directory:
Operating System
Location
Example
Windows
32-bit: C:\Program Files (x86)\Netskope\stagent
64-bit: C:\Program Files\Netskope\stagent
C:\Program Files (x86)\netskope\stagent\nsdiag -n
macOS
/Library/Application Support/Netskope/STAgent/
$ /Library/Application\ Support/Netskope/STAgent/nsdiag -n
Linux
/opt/netskope/stagent/
/opt/netskope/stagent/nsdiag -n
Command example:
nsdiag [options]
Command options are case-sensitive.
nsdiag -o <file>.zip
       nsdiag -c start [-o <filename>.pcap] [-f <total packet size>] [-s <snap length>]
       nsdiag -c stop
       nsdiag -p start [-o <filename>.pcap] [-f <total packet size>] [-s <file size>]
       nsdiag -p stop
       nsdiag -d start [-o <filename>.log]
       nsdiag -d stop
       nsdiag -u 
       nsdiag -g upload -s [1mb | 10mb | 100mb]
       nsdiag -r <URL> 
       nsdiag -g download -s [1mb | 10mb | 100mb]
       nsdiag -l [dump | debug | info | warning | error | critical]
       nsdiag -m 
       nsdiag -n 
       nsdiag -t enable  
       nsdiag -t disable [--password <password>]  
       nsdiag -x <regular expression> <string to match>
       nsdiag -b [start | stop | status | cleanup] -l [ dump | debug | info | warning | error | critical] -s <snap length> -m <max debug log files> -i [disable | maxInnerPcapTotalSize in MB] -e [disable | maxOuterPcapTotalSize in MB] -c [disable | CPU sample interval in second] -d [enable | disable sysdiagnose log] -t [duration of time in minutes] -o <output archive path>
       nsdiag [-h | -v]
       nsdiag --pin [country=US|IN|...] [pop=xyz]
       nsdiag --unpin
       nsdiag --check-dc
There are minor differences in the commands displayed for Mac and Linux. For example,
The command to capture the outer packet: nsdiag
-p start [-o <filename>.pcap] [-s <file size>]
The command to start capturing driver logs:
nsdiag -d start [-o <filename>.log]
Command Option
Description
-o <file>.zip
Save logs and diagnostics to output <file>.zip.
-c start [-o <filename>.pcap] [-s
]
Start capturing inner packet dump to <filename>.pcap.
-p start [-o <filename>.etl] [-s <file size>]
Start capturing outer packet dump to <filename>.etl.
-d start  [-o <filename>.etl]
Start capturing driver logs in <filename>.etl.
-o <filename>.<extension>
In Windows
Output will be created in default directory "C:/ProgramData/Netskope/stagent/Logs"
If filename is not specified then default filename will be used
Filename should NOT be a path as output will always be created in default directory
In macOS
Output will be created in default directory "/Library/Logs/Netskope"
If filename is not specified then default filename will be used
Filename should NOT be a path as output will always be created in default directory
In Linux
Output will be created in default directory "/opt/netskope/stagent/logs"
If filename is not specified then default filename will be used
Filename should NOT be a path as output will always be created in default directory
-s <snap length>
If snap length is not specified, entire packet will be captured.
-m <file size>
Set the maximum file size number. The file size (in MB) must be less than 1024 MB and a non-zero number.
Usage:
nsdiag -m <filesize>
Example:
nsdiag -m 100
This modifies  the nsdebug.log file size to 100 MB.
-c stop
Stop capturing inner packet dump.
-p stop
Stop capturing outer packet dump.
-d stop
Stop capturing driver logs.
-u
Update configuration
-h
Show this help.
-v
Show Netskope Client version.
-r
Show time values of website access.
For example,
./nsdiag -r www.google.com
NameLookupTime: 0.1
ConnectTime: 0.2
AppConnectTime: 0.0
PretransferTime: 0.2
StarttransferTime: 0.7
TotalTime: 0.9
RedirectTime: 0.0
DownloadSpeed: 19669 bytes/sec
- t enable/disable
Enables or disables the Netskope Client.
--password
Enter the master password required to disable Netskope Client.
For example, nsdiag -t disable --password < master password in plain-text >
-g download -s [1mb | 10mb | 100mb]
Perform Speed Test operation, supports [upload | download] operation.
Supported file sizes are 1mb, 10mb, 100mb and should be provided by -s. File size is mandatory.
-g upload
Performs upload Speed Test for specified size.
Supported payload size are 1mb, 10mb, 100mb and to be used with the -s option. File size is mandatory.
Upload test example:
nsdiag -g upload -s 10mb.
-g download
Performs download Speed Test for specified size.
Download test example:
nsdiag -g download -s 10mb
-l [dump | debug | info | warning | error | critical]
Set the Netskope client log level.
-n
Get NPA status.
Example:
$/Library/Application\ Support/Netskope/STAgent/nsdiag -n
NPA status is Connected.
-x
Test if string will match regular expression.
-f
Use this command to display the client details such as client status, tunnel status, Gateway, On-PremStatus, Gateway IP, Tunnel Protocol, Explicit Proxy.
>.\nsdiag.exe -f
Orgname:: Netskope Corp.
Config:: Default tenant config.
Steering Config:: All Users.
Email:: xxxx@xxxxxx.com.
Peruser config:: FALSE.
Tunnel status:: NSTUNNEL_CONNECTED.
Client status:: enable.
Gateway:: gateway-maa1.goskope.com.
Dynamic Steering:: FALSE.
OnPremDetection:: Not Configured.
Explicit Proxy:: false.
Gateway IP:: 198.168.1.1
Tunnel Protocol:: DTLS.
SNI Enable:: FALSE.
Traffic Mode:: All Traffic.
-b
Set the Client debug mode
--check-dc
Check device classification and send current status immediately to the backend.
--pin
Pin Netskope Client to a desired POP for connectivity.
--unpin
Unpin Netskope Client and revert to automatic POP selection.
In this Topic
Netskope Client Command Reference

---
## Netskope Client Enrollment
**URL:** https://docs.netskope.com/en/netskope-client-enrollment-methods/
**Last Modified:** 2025-10-06T15:05:55+00:00
**Scraped:** 2026-06-26T09:35:08.472952+00:00

Netskope Client Enrollment
Secure Enrollment content is now moved to the Netskope Client Enrollment section. This approach is to consolidate all enrollment methods and deployment instructions in one place.
Netskope Client enrolment with the Netskope Cloud services is a mandatory step before steering the traffic and securing the end-user device.
The enrollment process includes three methods:
IDP
UPN
Email Invite
Netskope recommends enabling
Secure Enrollment Service
for all enrollment methods.
Enrollment Methods Comparison
Attributes
IDP
UPN
Email Invitation
User Identification
User Email address
UPN
Userkey
User Authentication
Through the configured IdP
Authentication Token part of Secure enrollment
User activation key (One-time token)
User Experience
Requires user interaction
No user interaction
User needs admin rights to deploy
Security
Supports the security levels setup for IdP such as MFA
Uses the same authentication and encryption token across organization
One time token distribution through Email
Lacks control on the distribution of the Email invitation
Domain-Joined
Not required
Requires to be domain-joined
Not required
Email invitation method does not require Secure enrollment token(s) for the enrollment.
Enrollment Token Management
Netskope Client Enrollment Using IDP
Netskope Client Enrollment Using UPN
Netskope Client Enrollment Using Email Invite
Secure Enrollment Frequently Asked Questions
Secure Configuration Services FAQ
In this Topic
Netskope Client Enrollment

---
## Netskope Client Enrollment Using IDP
**URL:** https://docs.netskope.com/en/netskope-client-enrollment-using-idp/
**Last Modified:** 2026-06-05T13:05:11+00:00
**Scraped:** 2026-06-26T09:35:09.596937+00:00

Netskope Client Enrollment Using IDP
The Netskope Client supports Single Sign-On (SSO) user enrollment when it integrates with a SAML 2.0 supported identity provider.
Supported Versions
IDP enrollment is available for user enrollment of the Netskope Client installed in the following  end-user environments:
Windows
macOS
Linux
Android and ChromeOS
iOS
Prerequisites
SAML Integration:
Configure your IdP in the
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
in your Netskope Tenant UI. For more details, view
SAML Forward Proxy
.
User Provisioning:
Provision all users into your Netskope admin console.The email address of the user in your Netskope Admin Console must match the email you find in the integrated IDP. For more details, view
SCIM Settings
.
Network Configuration:
Ensure that you can access the destinations mentioned in
Client Network Configuration
.
For Android and ChromeOS deployments, end user devices must support Android AppLink feature. If the end-user devices (older than 2018 models) do not support AppLink, then  user enrollment process requires additional manual user intervention user to select the
Open With…
dialog box. See
Enrollment on Devices without AppLink Support
section for illustration.
With release version 123.0.0, in a multi-user environment, Netskope introduces a feature flag to enable Netskope Client to perform only IDP-based user enrollment and not a UPN-based enrollment. The default value of this feature flag is set to false. Contact Netskope Support to enable this feature. Netskope recommends not to enable this feature flag if
FailClose
is enabled in a multi-user environment. Otherwise, the second user’s IDP enrollment fails since FailClose drops the IDP network traffic. Thus, for multi-user environments, add IDP URLs in Steering exception so that subsequent users can successfully perform IDP based enrollment.
Advantages
Requiring a user password during enrollment ensures that the actual user is completing the process and prevents potential impersonation attacks.
Leveraging the security features of IDP, such as strong authentication mechanisms and password policies, provides a higher level of trust for enrolled devices.
Enabling multi-factor authentication (MFA) during the enrollment phase adds a second layer of verification, offering protection even if the user credentials are compromised.
Disadvantages
Typically not a silent deployment. Requires integrated Windows authentication configured with IDP for silent deployment.
NPA Pre-logon requires users to be authenticated at least once.
In a non-SSO environment, before the user enrolls,
Fail Close
is not enforced.
Netskope Client Deployment with Enrollment Tokens
In this mode, the user’s email address is used as the user identity fetched from the idP authentication. To identify if this method is used, refer the installation commands or methods and check if that contains following parameter:
installmode=IDP
And does not contain:
token=” ”
host= “ “ (tenant name)
Before you begin to deploy Netskope Client using enrollment tokens, ensure to enable Secure Enrollment Services and add tokens  in
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distribution
.
Ensure to enforce tokens for successful enrollment.
IDP Enrollment With Encryption Tokens
As the IDP enrollment authenticates the user against the IDP method, authtoken need not be configured. Encryption token is optional.
Deployment Option
Installation Commands
Single-User Mode Installation for IDP-based Enrollment
< OS utility > < NSClient > installmode=IDP enrollencryptiontoken= < encryption token >
For example, MSIEXEC command in Windows:
msiexec /I NSClient.msi tenant=corp domain=goskope.com installmode=IDP enrollencryptiontoken=XXX /qn
Multi-User Mode Installation for IDP-based Enrollment
< OS utility > < NSClient > installmode=IDP tenant= < tenant-name > domain= < tenant-domain-name > enrollencryptiontoken= < encryption token > mode=peruserconfig
For example, MSIEXEC command in Windows:
msiexec /I NSClient.msi tenant=corp domain=goskope.com installmode=IDP mode=peruserconfig enrollencryptiontoken=XXX /qn
If
enrollencryptiontoken
is generated and enforced in the UI, it must be used in the installation command. However,
enrollauthtoken
is optional even if it is generated and enforced.
Prelogon Connectivity with Enrollment Tokens
To use
NPA Prelogon
, auth token must be present on the end-user machine even with IDP enrollments. Failing to do so results in the Prelogon user being unable to be provisioned.
Use the following commands with the flag prelogonuser=<user>@prelogon.netskope.com:
For single user mode ( with encryption token)
UPN:
msiexec /I NSClient.msi host=<addon URL> token=<orgID> enrollauthtoken=<auth token> enrollencryptiontoken=<encryption token> prelogonuser=<user>@prelogon.netskope.com
IDP:
msiexec /I NSClient.msi host=<addon URL> token=<orgID> installmode=IDP enrollauthtoken=<auth token> enrollencryptiontoken=<encryption token> prelogonuser=<user>@prelogon.netskope.com
For per-user mode
UPN:
msiexec /I NSClient.msi host=<addon URL> token=<orgID> mode=peruserconfig enrollauthtoken=<auth token> enrollencryptiontoken=<encryption token> prelogonuser=<user>@prelogon.netskope.com
IDP:
msiexec /I NSClient.msi host=<addon URL> token=<orgID> installmode=IDP mode=peruserconfig enrollauthtoken=<auth token> enrollencryptiontoken=<encryption token> prelogonuser=<user>@prelogon.netskope.com
To learn more, view
Configure Client Prelogon Connectivity
.
User Impact
Client Version 116.0.0 or earlier (includes any upgrades to these versions).
Device
Existing User
New User Enrollments
Existing Enrolled User Requiring Re-enrollment
Client Version 116.0.0 or earlier (includes any upgrades to these versions)
Client version 116.1.0 or later (includes during the upgrades)
Client Version 116.0.0 or earlier (includes any upgrades to these versions)
Client version 116.1.0 or later (includes during the upgrades)
Personal Corporate Machine
No change
Netskope Client package with token
Netskope Client package with token
Uninstall the client
Reinstall Client package with token
Install Client package with token, Or
Apply token using nsdiag on Windows and macOS
Shared Desktop/VDIs and so on
No change
Uninstall the Client
Reinstall Client package with token
Install Client package with token, Or
Apply token using nsdiag on Windows
Uninstall the client
Reinstall Client package with token
Install Client package with token, Or
Apply token using nsdiag on Windows
– For Client Version 116.0.0 or earlier:
– These changes are required only if Create encryption of initial configuration of Netskope client is enabled.
– All operating systems other than Windows, do not require uninstallation and reinstallation before version 116.1.0.
– For Client version 116.1.0 or later, these changes are required only if Create encryption of initial configuration of Netskope client is enabled.
Example commands:
Re-run the MSIEXEC command with the new tokens.
This flexibility is available only for Windows devices and the MSI rerun is not supported if the
Protect Client configuration and resources option
is selected in the Client Configuration webUI.
Use the following
nsdiag
command to update the tokens:
nsdiag -e enrollauthtoken=<token> enrollencryptiontoken=<token>
The preceding
nsdiag
command is supported only on Windows and macOS platforms. You can run
nsdiag
command using the path:
C:\Program Files (x86)\Netskope\STAgent
.
Run this command in admin mode in Windows.
In Windows and macOS, if
nsdiag -e
command fails then an error message is displayed in the command prompt.
Enrollment Workflow
The following sections describe the enrollment workflow for the following operating systems:
Windows
macOS
Linux
Android and Chrome OS
iOS
The following section describes the enrollment workflow for Windows:
Windows AD or Hybrid AD Joined – Integrated Windows Authentication (IWA)
Integrated Windows Authentication capabilities enable Single Sign On (SSO) if the user has logged into a corporate domain-joined device.
For example, if you run the following command:
msiexec /I NSClient.msi installmode=IDP tenant=acme domain=goskope.com
in your terminal, Netskope Client can seamlessly enroll the user through SSO. The following screenshots describe the end-user experience:
The user automatically enrolls to your IDP. The following images are generated from an environment where the IDP is Microsoft Entra ID.
Once the installation and user enrollment and installation are complete, validate the User Email through the Configuration option of the Client’s system tray icon.
Microsoft Entra ID With Integrated Windows Authentication (IWA)
Microsoft Entra allows users to perform seamless Single Sign on (SSO) when the user’s machine connects to your corporate network. To learn more, view
Quickstart: Microsoft Entra seamless single sign-on – Microsoft Entra ID
.
Windows Devices Registered With Entra ID
You can also achieve a Single Sign-On (SSO) experience on Windows devices using
Primary Refresh Token
from Entra ID. Even though it does not require an Active Directory environment, you can still utilize this capability alongside Active Directory and Azure Active Directory (AAD). However, the device must be registered with Entra ID.
Okta With Agentless Desktop Single Sign-on (ADSSO)
Okta provides Agentless Desktop Single Sign On (ADSSO) capability. To learn more, view
Install and configure the Okta IWA Web agent for Desktop Single Sign-on | Okta
.
Non-Domain Joined Devices
If you install Client in IdP mode with tenant and domain suffix, the corporate IDP login page appears and the user needs to enter login credentials.
If you install Client without the tenant details, the user must enter the following details in the enroll window before getting the IdP login page:
–
Tenant Name:
If you are accessing tenant URL acme.goskope.com, then tenant name = acme.
–
Domain Name:
If you are accessing tenant URL acme.goskope.com, then domain name = goskope.com.
The user can contact their Tenant admin for the Tenant Name and Domain Name.
On successful IdP authentication, Netskope enrolls the user.
The following sections describe the enrollment workflow for macOS devices:
Entra ID – Platform SSO
The concept of Primary Refresh Token holds particular significance for macOS devices when Entra ID serves as the Identity Provider. To learn more, view
macOS Platform Single Sign-on (PSSO) overview – Microsoft Entra ID
. Once a device registers with Entra ID,  you can extend Single Sign-On (SSO) capabilities to the Netskope Client for browser-based authentication challenges. The installation parameters required are similar to the following example:
set -- 0 0 0 IDP goskope.com acme 0 mode=scheme preferephemeral=false httpmethod=get
Browser-Based authentication
Netskope Client supports FIDO authentication with our SAML forward proxy for macOS devices through external browser support. To learn more, view
Jamf Pro
.
Non-Domain Joined Devices
The following procedure illustrates the typical enrollment workflow:
If you install the Client in IdP mode with tenant and domain suffix, the corporate IDP login page appears and the user needs to enter login credentials.
If you install Client without the tenant details, the user must enter the following details in the enroll window before getting the IdP login page:
–
Tenant Name:
If you are accessing tenant URL acme.goskope.com, then tenant name = acme.
–
Domain Name:
If you are accessing tenant URL acme.goskope.com, then domain name = goskope.com.
The Netskope Client redirects the user to the IDP authentication process.
On successful IDP authentication, Netskope enrolls the user.
The following procedure illustrates the typical enrollment workflow:
If you install the Client in IdP mode with tenant and domain suffix, the corporate IDP login page appears and the user needs to enter login credentials.
If you install Client without the tenant details, the user must enter the following details in the enroll window before getting the IdP login page:
– Tenant Name: If you are accessing tenant URL acme.goskope.com, then tenant name = acme.
– Domain Name:  If you are accessing tenant URL acme.goskope.com, then Domain name = goskope.com.
The Netskope Client redirects the user to the IdP authentication process.
On successful IDP authentication, Netskope enrolls the user.
To learn more, view
Netskope Client for Linux
.
Refer to
Netskope Client for Android and ChromesOS
to learn more about the enrollment process.
Enrollment on Devices without AppLink Support
If you have a ChromeOS device that does not support the Android AppLink feature, then you must manually select the Client app for the enrollment process.
After the Client (
Netskope Client
app) is successfully installed and the dP authentication is successful, the user must manually open the Client app to receive the Netskope tenant authentication token to continue with the enrollment process. In the popup (see the following screenshot), click the
Open
button and also ensure that you select the
Remember my choice
option.
Refer to
Netskope Client for iOS
to learn more about the enrollment process.
Enforce Enrollment
Administrators can mandate enrollment for IDP enrollment method where it enforces the end-users to enroll with their login credentials. To learn more, view
Enforce Enrollment for Netskope Client
.
Unenrollment
A user can unenroll by selecting Allow users to unenroll from
Settings
>
Security Cloud Platform
>
Netskope Client
>
Client
Configuration
. To learn more, view
Netskope Client Configuration
.
For ChromeOS users, uninstall the app to Unenroll.
IdP Enrollment Using Webview2
The Microsoft Edge WebView2 enables you to include web technologies such as HTML and javascript into your native applications. Netskope Client supports user IdP enrollment using WebView2. The following lists the requirements:
Supported OS: Windows 10 or above.
Webview2 version (Minimum): 106.0.1370.52.
Set the Windows Registry feature flag to HKCU\software\Netskope key: webview2 value DWORD 0 to disable the feature.
To check the version of the WebView2 installed in your machine, you can use one of the following methods:
Method 1
Go to
Start
>
Add or Remove Programs
.
Search for WebView2.
Method 2
Go to
Start
>
Settings
>
Apps
>
Apps & Features
.
Search for WebView2. You can find the version of the installed WebView2.
In this Topic
Netskope Client Enrollment Using IDP

---
## Netskope Client Enrollment Using UPN
**URL:** https://docs.netskope.com/en/netskope-client-enrollment-using-upn/
**Last Modified:** 2026-06-01T15:59:55+00:00
**Scraped:** 2026-06-26T09:35:10.716197+00:00

Netskope Client Enrollment Using UPN
Using this method, the user machine is joined to Active Directory or LDAP directory integration. The Netskope Client monitors the Directory Service to identify the user by their User Principal Name.
Prerequisites
For user authentication and successful enrollment, add enrollment token(s) in the MDM configurations. To learn more on tokens:
Enrollment Token Management
.
User Provisioning: Provision all users into your Netskope admin console. The domain UPN ((User Principal Name)  of the user in the Netskope Admin Console must match the UPN value at the user’s device.
Requires the user’s device to be domain-joined to Active Directory or LDAP directory integration.
Advantages
Organizations can easily adopt as user enrollment is transparent to the end user.
Works seamlessly with the AD environment.
Disadvantages
Requires an authentication token deployment that administrators ensure are distributed properly and prevent any token compromises.
Requires periodic token maintenance by the admin.
Netskope Client Deployment with Enrollment Tokens
In this mode, the user’s UPN (User Principal Name) is used as user identity from the logged in domain-joined system. To identify if this method is used, refer the installation commands or methods and check for the following parameters:
token=” ”
host= “ “ (tenant name)
And does not contain
installmode=IDP
Before you begin to deploy Netskope Client using enrollment tokens, ensure to enable Secure Enrollment Services and add tokens  in
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distribution
.
Ensure to enforce tokens for successful enrollment.
Deployment Option
Installation Commands
Single-User Mode Installation for UPN-based Enrollment
With authentication token
< OS utility > < NSClient > host= < addon URL > token= < orgID > enrollauthtoken= < auth token >
For example, MSIEXEC command in Windows:
msiexec /I NSClient.msi host=addon-corp.eu.goskope.com token=XXX enrollauthtoken=XXX /qn
With authentication and encryption tokens
< OS utility > < NSClient > host= < addon URL > token= < orgID > enrollauthtoken= < auth token > enrollencryptiontoken= < encryption token >
For example, MSIEXEC command in Windows:
msiexec /I NSClient.msi host=addon-corp.goskope.com token=XXX enrollauthtoken=XXX enrollencryptiontoken=XXX /qn
Multi-User Mode Installation for UPN-based Enrollment
With authentication token
< OS utility > < NSClient > host= < addon URL > token= < orgID > mode=peruserconfig enrollauthtoken= < auth token >
For example, MSIEXEC command in Windows:
msiexec /I NSClient.msi host=addon-corp.goskope.com token=XXX enrollauthtoken=XXX mode=peruserconfig /qn
With authentication and encryption tokens
< OS utility > < NSClient > host= < addon URL > token= < orgID > mode=peruserconfig enrollauthtoken= < auth token > enrollencryptiontoken= < encryption token >
For example, MSIEXEC command in Windows:
msiexec /I NSClient.msi host=addon-corp.goskope.com token=XXX enrollauthtoken=XXX enrollencryptiontoken=XXX mode=peruserconfig /qn
User Impact
Client version 116.0.0 or earlier (includes any upgrades to these versions)
Device
Existing User
New User Enrollments
Existing Enrolled User Requiring Re-enrollment
Client version 116.0.0 or earlier (includes any upgrades to these versions)
Client Version 116.1.0 or later (includes during upgrades)
Client version 116.0.0 or earlier (includes any upgrades to these versions)
Client Version 116.1.0 or later (includes during upgrades)
Personal Corporate Machine
No change
Netskope Client package with enrollment tokens
Netskope Client package with enrollment tokens
Uninstall the Client
Reinstall Client package with Secure enrollment tokens
Client package with Secure enrollment tokens, Or
Apply tokens using nsdiag on Windows and macOS
Shared Desktop/VDIs and so on
No change
Uninstall the Client
Reinstall Client package with enrollment tokens
Client package with the enrollment tokens, Or
Apply tokens using nsdiag on Windows
Uninstall the Client
Reinstall Client package with Secure enrollment tokens
Client package with Secure enrollment tokens, Or
Apply tokens using nsdiag on Windows
All operating systems other than Windows, do not require uninstallation and reinstallation before version 116.1.0.
Example commands:
Re-run the MSIEXEC command with the new tokens.
This flexibility is available only for Windows devices and the MSI rerun is not supported if the
Protect Client configuration and resources
option is selected in the Client Configuration webUI
Use the following
nsdiag
command to update the tokens:
nsdiag -e enrollauthtoken=<token> enrollencryptiontoken=<token>
The preceding
nsdiag
command is supported only on Windows and macOS platforms. You can run
nsdiag
command using the path:
C:\Program Files (x86)\Netskope\STAgent
.
Run this command in admin mode in Windows.
In Windows and macOS, if
nsdiag -e
command fails then an error message is displayed in the command prompt.
In this Topic
Netskope Client Enrollment Using UPN

---
## Netskope Client Enrollment Using Email Invite
**URL:** https://docs.netskope.com/en/netskope-client-enrollment-using-email-invite/
**Last Modified:** 2026-06-01T12:46:10+00:00
**Scraped:** 2026-06-26T09:35:11.838877+00:00

Netskope Client Enrollment Using Email Invite
The admin console sends email invitations to install the Netskope Client. The user can click the link in the email they received to download and install the Client (or the mobile profile) on their device.
If you use the email invite option for iOS devices, ensure you follow the steps defined
here
to trust manually installed certificates. Email invites are time-bound and the intended user can use them.
Supported OS
Email enrollment is available for user enrollment of the Netskope Client installed in the following  end-user environments:
Windows
macOS
Linux
Android
iOS
For iOS devices running versions after 12.1.3, Apple has changed how profile installations work. Apple has restricted automatic installation of profiles, that now requires additional steps. In such cases, for a new profile, end users must manually navigate to device settings to install the profile after clicking on the link in the email and downloading the profile. Netskope recommends updating the email invitation template to call the users’ attention to this important step. This change does not impact MDM-based configuration profile installation.
– Reference:
https://support.apple.com/en-us/HT209435
– To enroll in the iOS beta program and try this experience, view
https://appleseed.apple.com/
Prerequisites
Import a user with a valid and accessible email into the tenant. To learn more, view
Prerequisites to deploy Client through Email Invite
.
Set up the user  account on the tenant before sending out the email invite. To learn more, view
Provisioning Users for Netskope Client
.
Installation of client requires administrator rights on the end-user devices.
Advantages
The admin need not share any user authentication parameters for enrollment.
Send Email Invites for corporate and personal Email IDs.
Quick way to deploy for BYOD users.
Disadvantages
The user requires admin rights to install the Client software.
Misuse of the Email by forwarding it to the unintended recipients.
Download installation package name contains the org key and the activation key (not secure).
Netskope Client Deployment Using Email Invite
The following sections describe how to deploy Netskope Client using email invite in different operating systems:
Windows
macOS
Linux
iOS
Android and Chrome OS
Create Email Invite for New Users
Perform the following instructions in your (administrator account required) Netskope admin console to create the email invite:
An email invite is single use and the invite is valid for seven days only, whichever happens first.
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Users
.
Click
New Users.
Enter the following in the
New Users
pop-up window:
In User email address, enter comma separated email address if adding more than one user.
In addition, to add bulk users you can upload a CSV file with the email address of all users. The CSV file entries must have this format: email, lastname, firstname.  Last name and First name are optional.
Select the
Send email invite
checkbox.
Select one of the following in
Client Version Options (Windows)
:
64 bit
32 bit
Click
Add
.
Create Email Invite for Existing Users
Perform the following instructions in your (administrator account required) Netskope admin console to send email invite to an existing user:
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Users
.
Select the user (s) on the
Users
webUI.
Click
Send Invitation
.
In
Send Client Invites
, if you are using Windows OS, select one of the following in Client Version options (Windows):
64 bit version
32 bit version
Click
Send
.
The webUI displays Invite Successfully Sent confirmation box.
Install Netskope Client Through Email Invite
You can install Netskope Client using an email invitation sent from the Netskope Admin console.
Email invites are time-bound and only the intended user can use them.
After you receive the email:
Check your email from Netskope Onboarding and click the link for Windows.
If you selected 64 bit Windows Client version in the Netskope tenant webUI, select
Windows Client (64-bit)
in the email. The email that you receive can contain a similar format as shown in the following screenshot.
If you selected 32 bit Windows Client version in the Netskope tenant webUI, select
Windows Client
in the email. The email that you receive can contain a similar format as shown in the following screenshot.
Click
Download
.
This downloads to your default location.
Click the installer file.
Follow the steps as displayed in the
Install Netskope Client
window.
Once the installation is complete, you can see the Netskope Client running on your taskbar.
All new installations that use the email invitation feature require the end user to approve the kernel extension. Users will see a message that guides them through the steps to grant approval.
Note
The system behavior presents the approval dialog in the Security > Privacy preferences pane for 30 minutes after the above alert is generated. No traffic is tunneled to Netskope unless this approval is granted if the client is installed manually via the email invitation method.
Before you do a fresh installation of Netskope Client on macOS, do the following:
Install Netskope Client as an admin user (A non-admin cannot approve KEXT).
When the system blocks  KEXT during installation, users must approve the KEXT from
System Preferences
>
Security
>
Privacy
. In a few minutes, the Client will detect the approved KEXT.
Create Email Invite For New Users
Perform the following instructions in your (administrator account required) Netskope admin console to create the email invite:
An email invite is single use and the invite is valid for 7 days only, whichever happens first.
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Users
.
Click
New Users
and enter the following in the
New Users
pop-up window:
User email address. Enter comma separated email address if adding more than one user.
In addition, to add bulk users you can upload a CSV file with the email address of all users. The CSV file entries must have this format: email, lastname, firstname. Last name and First name are optional.
Select the
Send email invite
checkbox.
Click
Add
.
Create Email Invite For Existing Users
Perform the following instructions in your (administrator account required) Netskope admin console to send email invite to an existing user:
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Users.
Select the user (s) on the Users webUI.
Click
Send Invitation
.
The webUI displays a Send Client Invite confirmation box.
Click
Send
.
Install Netskope Client Through Email Invite
You can install Netskope Client using an email invitation sent from the Netskope Admin console.
Email invites are time-bound and only the intended user can use them.
After you receive the email:
Check your email from Netskope Onboarding and click the link for
Mac Client
.
Click
Download
. This downloads to your default location.
Click the installer file.
Follow the steps as displayed in the
Install Netskope Client
window.
Once the installation is complete, you can see the Netskope Client running on your taskbar.
To learn more about the installation process for Netskope Client for Linux using Email ID, view
Install and Enroll by Email ID
.
Deployments through an email invite is a two step process:
iOS Profile link:
This installs tenant certificates on the device. They are necessary for SSL Decrypt related functionality. This profile contains only certificates.
iOS Client link:
Helps to find the Client in the App Store and enroll it after installation.
– iOS Client in the email is a one time installation only link. You will receive an error message
Email Invitation Expired
the second time you attempt to use the link after installing Netskope Client.
– If you are unable to see the link to download Netskope Client for iOS in the email invite, use the default email template that includes the link to download Netskope Client for iOS.
After you receive the email:
Check your email from Netskope Onboarding and click
iOS Profile
to install the profile with certificates to your iOS device.
Click
Allow
for the pop-up
This website is trying to download a configuration profile. Do you want to allow this?
Close the pop-up after the profile is downloaded.
In your iOS device, go to
Settings
app >
General
and tap
Profile Downloaded
. The profile consists of the root and tenant certificates.
Tap
Install
in the upper-right corner. Follow the installation instructions displayed on the screen.
Go to
Settings
>
General
>
About
>
Certificate Trust Settings
.
Tap to enable the option
Enable Full Trust to Root Certificates
.
Click
Continue
to close the warning.
Click the
iOS Client
link in the email invite.
This opens a page with two links and perform the following steps:
Click
Install
to download Netskope Client from Apple Store to iOS devices. Perform the following instructions:
Click
Allow
to add VPN configurations.
Wait for the Client enrollment.
Click
Download iOS configurations
to complete the enrollment process.
Follow the enrollment steps as displayed on your screen.
After completing the enrollment steps, go to
VPN & Device Management
.
Check whether VPN displays the Connected status to ensure the successful installation of the iOS configuration profile.
You can install Netskope Client using the email invitation sent from the admin console.
After you receive the email:
Check your email from Netskope Onboarding and click Android Client.
Follow the instructions on your screens to install Netskope Client from Google Play Store.
Click
Install
.
After you install, Click
Open
.
Click
Allow
for notifications.
The app opens after it completes downloading the configurations.
Support for Chromebook
To install Netskope client in Chromebook, use the following procedure to install the Netskope root CA cert in Chrome OS cert store.
Ensure that you have purchased additional Chromebook management licence for the Google admin account.
Cert pinned app domains are bypassed in Netskope Android App
Enroll Chromebook to Google Managed Account
Power on the Chromebook and follow the on-screen instructions until you see the sign-in screen. Don’t sign in yet. If you see the enrollment screen instead of the sign-in screen, go to
step 4
.
If you’re enrolling a Chromebook tablet, tap Email or phone. Then, tap the
More
option (
three vertical dots
).
Switch to full layout to open the on-screen keyboard.
Choose an option to get to the enrollment screen:
Press
Ctrl+Alt+E
.
Click
More options
>
Enterprise enrollment
Note
This option is not available on Chromebook tablets.
Enter the username and password from your Google admin welcome letter or for a Google Account that has the permissions to enroll. If prompted, enter the asset ID and location and click
Next
.
When you get a confirmation message that the device is successfully enrolled, click
Done
.
Configure Google Admin Account
Sign in to your Google admin account console.
Click
Device Management
.
On the left, click
Network
and click
Certificates
.
[
Optional
] On the left, choose the organizational unit to add the certificate.
Note
The top-level organization is selected by default to give all users (including those in sub-organizations) access to any added certificates.
Click
Add Certificate
. Choose the certificate file to upload and click
Open
.
[
Optional
] If the certificate is used as a root CA for an SSL-inspecting web filter or to allow the browser to validate the full digital certificate chain of servers, check the Use this certificate as an HTTPS certificate authority box.
Click
Save
and then
Done
to confirm.
Deploy the Certificate to Chrome Devices
Enroll the Chromebook to the organization’s Google account. Chrome devices will authenticate to Google and receive the SSL certificate. The pushed certificate applies to all enrolled Chrome devices.
The admin sends an invitation email to the Chromebook user and the user must click the
Android app
link to install the Android app in Chromebook.
ChromeOS devices use the same Netskope Client app as Android devices.
In this Topic
Netskope Client Enrollment Using Email Invite

---
## Explicit Proxy Over Client (EPoC)
**URL:** https://docs.netskope.com/en/explicit-proxy-over-client-epoc/
**Last Modified:** 2026-06-24T20:23:53+00:00
**Scraped:** 2026-06-26T09:35:21.316483+00:00

Explicit Proxy Over Client (EPoC) - Netskope Knowledge Portal
Explicit Proxy Over Client (EPoC)
This document provides guidance on using Netskope Client in a network environment with no default route and no DNS resolution for public domains.
Overview
Here, the users cannot resolve and access public Internet resources. This is an approach similar to legacy explicit proxy, with the additional benefit of advanced controls and user coaching capabilities brought by the Netskope Client.
Supported Traffic Types
Next-Gen Secure Web Gateway (NG-SWG) – All Web Traffic
Prerequisites
Install Netskope Client on the endpoint.
goskope.com DNS zone is forwarded to a recursive DNS resolver.
Netskope Client can establish a direct DTLS/TLS tunnel to the Data Plane.
The local network has routes for 163.116.128.0/17 and 162.10.0.0/17.
Firewall is configured to allow TCP/UDP 443 to 163.116.128.0/17 and 162.10.0.0/17.
Add Exclusions in both the explicit proxy configuration (most likely in the PAC file) and the steering policy. The PAC file must have a statement for *.goskope.com to go direct.
A web server is required to host the EPoC PAC file. Use 163.116.128.80 or 163.116.128.81 on port 80 as the proxy destination in the PAC file.
– Port 8080 or 8081 can also be used as the proxy port; must be configured as a non-standard port for intercept in the steering configuration.
– EPoC must use a EPoC – PAC File. Do not use the operating system static proxy configuration, otherwise the Netskope Client mode changes to Proxy Interoperability Mode.
Recommendation
Netskope recommends using explicit proxy over Client because without a default route to the internet you must have a static route to a proxy in order to egress from the local network, and the same goes for public DNS resolutions.
In this approach, the Netskope Client installed in the endpoint is connected to the nearest Netskope NewEdge Data Plane. Netskope Client must be configured to intercept the proxy request in the configuration. Due to its operation mode (monitor network sessions at the OS level) an actual proxy is not required; the Netskope Client knows which IP is used so that it can intercept the traffic and send it through its tunnel.
Netskope NewEdge Data Plane steers all internet traffic sent from the endpoint to its configured explicit proxy and not explicitly bypassed. On the NewEdge Data Plane, the system inspects the traffic based on the real-time security policies defined and the corresponding action is taken.
Advantages of Using EPoC
Consistent security posture
regardless of the user location.
Comprehensive traffic inspection
, encompassing both web and non-web, directed towards both Internet and Private Applications, originating from the endpoint.
Optimal Performance
facilitated by the Netskope Client’s connection to the nearest Netskope NewEdge Data Plane.
Visibility
into web traffic directed to the Internet.
In this Topic
Explicit Proxy Over Client (EPoC)

---
## Netskope Client for Virtual Desktop Infrastructure (VDI)
**URL:** https://docs.netskope.com/en/netskope-client-for-virtual-desktop-infrastructure-vdi/
**Last Modified:** 2026-04-29T04:06:29+00:00
**Scraped:** 2026-06-26T09:35:42.715203+00:00

Netskope Client for Virtual Desktop Infrastructure (VDI)
This document mainly describes the instructions to deploy Netskope Client in a VDI environment. It also covers the configurations, limitations, and best practices that apply to the different types of VDI deployments used in your organization.
Supported VDI Environments
Microsoft Azure Virtual Desktop
Citrix DaaS Integration with Azure Virtual Desktop
Citrix Apps and Desktop
Amazon Workspace
Omnissa Horizon
Persistent vs Non-Persistent VDI
Persistent and Non-persistent VDIs offer primarily two types of VDI solutions that provide various advantages and use-cases for organizations.
Persistent VDI
A persistent VDI, commonly referred to as Stateful VDI, is an approach where each user is assigned a dedicated virtual machine. It saves all configurations, and other settings that the user updates, and persists from one session, thereby providing the same experience as a physical desktop.
The following section describes the different methods in which Netskope Client is deployed in a persistent VDI environment:
MDM Deployment Method
In Persistent VDI, there is no need to install Netskope Client in advance on the master image (golden image). MDM can instrument the deployment of Netskope Client and manage the VDI machine.
Administrators can deploy Netskope Client through MDMs in two ways depending on the chosen Client enrollment method described
here
.
Master Image (Golden Image) Pre-installation
Regardless of the VDI solutions, the administrator must install Netskope Client on the master image before creating the snapshot used in the VDI environment.
To deploy Netskope Client using a master image in a persistent VDI environment:
Download Netskope Client MSI from
Netskope Support
.
Copy MSI to the master or golden image.
Refer
Microsoft Azure
and
Citrix Virtual Apps
documentation to create a golden image.
The administrator can now install Netskope Client using CLI (cmd or Powershell).
Administrators can deploy Netskope Client through golden image in two ways, depending on the chosen Client enrollment method described
here
.
Non-Persistent VDI
Administrators manage virtual desktops by allowing users to share a single desktop, and the system removes all installed applications and settings after the user closes the VDI session.
Master Image (Golden Image)
Administrators cannot use MDM method to deploy Netskope Client in a non-persistent VDI. The only deployment method to install the Netskope Client is using the Golden Image.
To deploy Netskope Client using a master image in a non-persistent VDI environment:
Download Netskope Client MSI from
Netskope Support
.
Copy MSI  to the master or golden image.
Refer
Microsoft Azure
and
Citrix Virtual Apps
documentation to create a golden image.
The administrator can now install Netskope Client using CLI (cmd or Powershell).
Administrators can deploy Netskope Client through golden image in two ways, depending on the chosen Client enrollment method described
here
.
Netskope Client Enrollment Method
UPN
IDP
Choose UPN enrollment method if the VDI machines are domain-joined (either AD or Entra)
Use the following parameters to deploy Netskope Client in a multi-user environment using UPN:
msiexec /I NSClient.msi host=addon-<tenant-FQDN> token=<OrgID> mode=peruserconfig [enrollauthtoken=<enrollment-token> enrollencryptiontoken=<encryption-token> prelogonuser=<prelogon-user> npavdimode=on userconfiglocation=<path> fail-close=<disable|no-npa> autoupdate=<on|off> /l*v <path>] /qn
IDP is another user enrollment method where a user needs to authenticate against the configured IDP each time a user logs into the machine. To learn more, view
User Authentication and Provisioning
.
After the user authenticates, the Netskope Client in a persistent VDI enrolls using the authenticated user credentials. As long the user profile exists on the VDI machine, the system does not prompt the user to enroll again.
In a non-persistent environment, the administrator must ensure that the profile is non-persistent; otherwise the system always prompts the user for authentication at every session.
For subsequent users to log in using the IDP method after the first user logs into the VDI using the IDP enrollment method, contact Netskope Support to enable the necessary feature flag.
Use the following parameters to deploy Netskope Client in a multi-user environment using IDP:
msiexec /I NSClient.msi installmode=idp tenant=<tenant-name> domain=<tenant-domain> mode=peruserconfig [enrollauthtoken=<enrollment-token> enrollencryptiontoken=<encryption-token> prelogonuser=<prelogon-user> npavdimode=on userconfiglocation=<path> fail-close=<disable|no-npa> autoupdate=<on|off> /l*v <path>] /qn
Client Deployment Parameters
Parameter
Description
host=addon-<tenant-name>.[region.]<tenant-domain>
(Mandatory parameter)
Required when enrolling users using UPN. Do not use it when enrolling users using IDP. This is the addon hostname of your tenant. For example,
If your tenant hostname is corp.goskope.com use host=addon-corp.goskope.com
If your tenant hostname is corp.eu.goskope.com use host=addon-corp.eu.goskope.com
token=<Organization ID>
(Mandatory parameter)
Required when enrolling users using UPN. Do not use it when enrolling users using IdP. To find your organization ID:
Login to your Netskope Admin Console with admin credentials.
Go to Settings > Security Cloud Platform > MDM Distribution.
Locate your Organization ID under the Create VPN Configuration section. The organization ID is case-sensitive.
enrollauthtoken=<Authentication Token>
Required when enrolling users using UPN with Secure Enrollment Authentication Token that is enabled and enforced.
Required when using Private Access Prelogon (UPN and IdP enrollment) with Secure Enrollment Authentication Token that is enabled and enforced.
enrollencryptiontoken=<Encryption Token>
Required when enrolling users using UPN or IdP with Secure Enrollment Encryption token enabled and enforced.
mode=peruserconfig
(Mandatory parameter)
Use when installing on a multi-user system. With this parameter set, each user needs to enroll Netskope Client independently.
With this parameter set, each user needs to enroll Netskope Client independently and same steering configuration is applied for all users. The Client Configuration is applied based on the priorities.
This parameter is mandatory for VDI environments (if different users login concurrently or separately into the same VDI machine, they are identified correctly by their UPN).
npavdimode=on
Use when installing on a multi-user Windows desktop with concurrent users logged on at the same time, such as some Citrix VDI or Azure Virtual Desktop Environments.
This parameter is applicable only Netskope Private Access (NPA).
userconfiglocation=<path>
Overrides the default path for storing the user configuration. It is recommended to leave this parameter out (allow the default path) unless users' home directories are hosted on external file servers or network shares. And this parameter is recommended to be used only for multi-user systems (when mode=peruserconfig is included in the parameters).
The default path: %AppData%\Netskope\STAgent
The custom path could be an absolute path, a network share, or a path having environment variables. Environment variables need to be properly escaped depending on how the MSIEXEC command is run:
If running from a command prompt, append ^ before each %
Example:
>msiexec /I NSClient.msi mode=peruserconfig userconfiglocation=C:\Users\^%USERNAME^%\Netskope
If running from a batch script, append % before each %
Example:
>msiexec /I NSClient.msi mode=peruserconfig userconfiglocation=C:\Users\%%USERNAME%%\Netskope
If running from SCCM (or other mass deployment tool), append ^ before each % and prefix with cmd /c
Example:
>>cmd /c msiexec /I NSClient.msi mode=peruserconfig userconfiglocation=C:\Users\^%USERNAME^%\Netskope
fail-close=disable|no-npa
This overrides the Fail Close settings in the Client Configuration.
disable: Explicitly disable fail-close on this device.
no-npa: Allow Private Access (NPA) traffic even if the Internet Security tunnel cannot be established and Fail Close is blocking Internet traffic.
prelogonuser=<prelogon username>@prelogon.netskope.com
Use when deploying Private Access Prelogon. For more information, view
Prelogon
.
autoupdate=on|off
on: Default value which allows auto updating of Netskope Client based on the Client Configuration. If Client Configuration has auto update disabled then Netskope Client will not auto update on this system.
off: Disable auto updating of Netskope Client. This overrides the Client Configuration and will prevent any Netskope Client auto updates on this system.
/l*v
Sets the MSIEXEC installation log file path. For Example:
/l*v %PUBLIC%nscinstall.log
/qn
Use this option for silent installation.
Support for Multi-User Environment in VDI
The following sections describe the best practices that you can consider in a multi-user VDI environment.
Persistent vs Non-Persistent Comparison In a Multi-User Environment
Refer to the following table to understand the considerations taken for Steering Configuration, Client Configuration, OTP, and Master Password:
Configuration Type
Persistent VDI
Non-Persistent VDI
Additional information
Client Configuration
Client Configurations with highest priority* takes precedence
Client Configurations with highest priority takes precedence
-
Steering Configuration
Applies the first logged in user Steering Configuration downloaded by the Netskope Client.
Applies the first logged in user Steering Configuration downloaded by the Netskope Client.
For consistent behavior in a multi-user environment, ensure every user shares the same Steering Configuration.
One-Time Disablement Password
Applies to the Client Configuration with the highest priority.
Applies to the Client Configuration with the highest priority.
User A disabling Internet Security using OTP does not disable the Client services of User B.
Master Password
Applies to the Client Configuration with the highest priority.
Applies to the Client Configuration with the highest priority
User A disabling Clients services using Master Password does not disable the Client services of User B.
*
Priority
is the order of configuration. The higher the profile in the list, the higher the priority.
Whenever the administrator does a fresh installation or upgrades the Netskope Client, Netskope recommends deleting the registry keys:
nsdeviceuid
and
nsdeviceuidnew
from the master image to avoid any duplicate unique device IDs of the cloned VMs.
Additional Info
Delete
nsdeviceuid
and
nsdeviceuidnew
keys to avoid duplicate unique ID between master image and cloned VM. If multiple VMs are cloned from the same infrastructure (for example, VMware EXSi), they get the same unique device ID for the Cloned VMs.
If the administrator does not delete registry keys of the device UID, the master image and cloned image will use the same unique device ID.
The following folders are created after the Netskope Client installation and the administrator can check if the master image includes the following folders:
C:\Program Files (x86)\Netskope
C:\Program Files\Netskope
C:\ProgramData\netskope
Limitation
The Netskope Client in a multi-session environment exhibits the following limitations:
NPA Policies for applications that use “session 0” to communicate (like AD or SMB) must be assigned to the “session 0” VDI user specified on the Client Configuration, and all the traffic for those applications, no matter the actual user initiating it, will be identified and managed by the “session 0” VDI user policy.
eDLP (Endpoint DLP) is not supported in multi-session environments running a Windows Desktop OS. Adminstrators must consider disabling eDLP in those environments.
eDLP (Endpoint DLP) is not enabled in multi-session environments running a Windows Server OS.
When the Netskope Client is deployed/upgraded/reconfigured from single user mode to multi-user mode using IdP enrollment on a Windows device, the stAgent process fails to initialize for users who transition from an inactive or locked state back to an active session.
For example, Two users User A, and User B use a Windows system.
User B is active on the system and User A who is logged in but inactive.
Netskope Client gets installed/upgraded/reconfigured from single user mode to multi user mode and the session for User B is created successfully.
User B locks the screen, which moves the session into an inactive state.
User A unlocks the screen but the Netskope Client doesn’t initialize for User A and there is no stAgentUI process for User A. This disrupts the traffic steering for User A and keeps the Client inactive.
To restore stAgentUI process and ensure proper traffic steering for User A, Netskope recommends performing log off and login for user A to eliminate any inactive Netskope Client issue.
Define Client Configuration
In a multi-user environment, each Client Configuration includes a priority value. The configuration with the highest priority remains active up to 24 hours after it is downloaded. If another user logs in with a configuration of equal or higher priority, then the latter configuration is applied immediately. However, if the priority for the new configuration is lower, it will not be applied while the current configuration is still within its 24-hour window. For example, consider the following scenarios:
Scenario 1:
User A is part of the Client Configuration A (with higher priority), while User B is part of Client Configuration B (with lower priority). The Client Configuration with the highest priority is always applied during both user session logins.
Scenario 2:
If User B logs in first and applies Client Configuration B (with lower priority). When User A (with higher priority) subsequently logs into the multi-session, both users receive Client Configuration A due to its higher priority.
Scenario 3:
Consider User A logs in and logs out in a span of a few minutes. User B logs in after 24 Hours of User A logging out. User B uses the lower priority Client Configuration B due to the higher priority of the User A configuration expired after 24 hours.User B receives the lowest priority Client Configuration and it remains as it is even when there are any Client configuration updates.
Scenario 4:
Consider Client Configuration A (higher priority) is applied to User A and User B. The tenant administrator modifies the Client Configuration B. This does not change the Client Configuration applied from A to B due to the higher priority of Configuration A. However, if the tenant administrator modifies the Client Configuration A; the new modifications are applied to User A and User B.
Scenario 5:
If User B, belonging to Client Configuration Group B, logs into the VDI first, with no other users currently logged into the VDI session. In this case, the Netskope Client will apply the settings from Client Configuration Group B to User B. Any edits or modifications made to other client configuration groups will not affect User B’s session. Changes will only take effect if an administrator updates the settings for Client Configuration Group B.
Define Steering Configuration
In a multi-user VDI environment, it applies the first logged in user steering configuration that the Netskope Client downloads. Traffic from session 0 (the service session) is steered through the logged-in user’s tunnel that contains the smallest session ID. For example, consider the following scenarios:
For consistent behavior in a multi-user environment, ensure every user shares the same steering configuration.
Scenario 1:
User A (with Steering Configuration A) logs into the session, followed by User B a few minutes later. User A and User B receive the same steering configuration profile (Steering Configuration A). Now, if User C (with Steering Configuration C) logs in, User C also receives the same Steering Configuration of User A.
Scenario 2:
User A logs in followed by User B. Steering configuration A is applied to both users. Now, if the If the tenant admin modifies the settings in Steering Configuration B and updates the Client Configuration.The logged in users now contains the modified Steering Configuration B.
Scenario 3:
If only User B logs in and no other users have accessed the VDI session, the Steering configuration for User B will be applied to User B’s client UI. Any modifications made to other Steering configurations will not affect User B’s client UI. Changes to the Steering configuration will only take effect when the admin modifies User B’s specific steering settings. This behavior is similar to that of a single-user session.
Define One-Time Disablement Password
In a multi-user environment, Client Configuration with the highest priority takes precedence.
For example, consider the following scenario where User A logs in and performs the following:
Click the Disable
Internet Security
option in the Client UI.
This prompts a dialog box with the option to enter the one-time password.
Enter the password and verify if the Internet Security option is disabled.
Next, User B logs in and gets the same Client Configuration as User A. User B can verify if the
Internet Security
option is enabled in the Client UI.
If User B logs in first with Client Configuration B with lower priority, the administrator must configure the OTP in the Client Configuration for User B to disable Internet Security Services in the Client UI.
Define Master Password
In a multi-user environment, Client Configuration with the highest priority takes precedence.
For example, consider the following scenario, User A logs in and performs the following:
Click the DisableAll
Client Services
option in the Client UI.
This prompts a dialog box with the option to enter the master password.
Enter the password and verify if the All Client Services option is disabled.
Next, User B logs in and gets the same Client Configuration as User A. User B can verify if the
All Client Services
option is enabled in the Client UI.
If User B logs in first with Client Configuration B with lower priority, the administrator must configure the Master Password in the Client Configuration for User B to disable All Client Services in the Client UI.
Define Fail Close
In a multi-user environment, Client Configuration with the highest priority takes precedence.
Scenario 1:
When Netskope Client is not reachable, it goes into the Fail Close state for VDI sessions. If User A logs in and accesses the Steering app, the Client blocks access. If User A accesses the defined exception apps; the Client must bypass the app traffic.
Scenario 2:
When the device is in fail-close status, it should bypass the MP APIs (such as client config, auto-upgrade, client status, etc.).
Scenario 3:
When both User A and User B log in to the VDI session while the Client is in fail-close, both users are blocked from accessing the Steering app, and the defined exception apps are bypassed.
Scenario 4:
When User C, a non-provisioned user (not managed by the Netskope tenant/guest user), logs into the VDI session while other provisioned users are active, and the Netskope client is enabled, verify that User C’s Client status shows as fail-close. User C’s access to the steering apps is blocked, while the defined exception apps are bypassed.
Known Issue: User migration
If existing users are migrating from UPN enrollment to IDP enrollment or vice-versa in the master image for non-persistent VDI, they can encounter issues due to stale data in their user profile saved on the Fslogix/Shared network path. As a workaround, administrators must delete the user profile from the roaming profile path that includes FSLogix or home directories located on external file servers or network shares.
User Notification for the Published App
This section provides guidance about the user notification behavior for published apps through XenApp with Netskope Client.
User notification templates enable the administrator to block a user action and/or send an alert to the user. These templates can be customized to provide specific information and options in an alert or block notification. Administrators can provide a justification dropdown list for the users and also display a description box to provide a justification (Optional). To learn more, view
User Notification Template
.
Consider the following scenarios where the Netskope Client prevents application access by blocking or alerting users according to the real-time protection policies for data loss prevention (DLP) and threat protection. It enforces actions such as file upload or download and user login or logout to maintain robust security. For example,
If the user is logged into the Microsoft Teams application in XenApp and tries to sign out; Netskope Client blocks the user action and sends an alert to the user.
Netskope Client prevents file download or content posting in the published Cloud application. For example, if the user is logged into the Microsoft Teams application in XenApp and tries to download a confidential file from the Teams chat, Netskope Client blocks the user action and sends an alert to the user.
Netskope Client prevents web traffic activities such as Upload or Download through a browser. For example, if the user tries to download Notepad++ application through the Microsoft Edge or Google Chrome browser. Netskope Client blocks the user action and sends an alert to the user.
Netskope Client prevents web traffic activities such as accessing an unauthorized domains through a browser. For example, if the user tries to access a domain such www.gambling.com through the Microsoft Edge or Google Chrome browser. Block message is seen on the browser where the user enters the domain name on the browser URL.
In this Topic
Netskope Client for Virtual Desktop Infrastructure (VDI)

---
## Deploy Client on iOS Using Intune
**URL:** https://docs.netskope.com/en/deploy-client-on-ios-using-intune/
**Last Modified:** 2026-04-17T12:23:26+00:00
**Scraped:** 2026-06-26T09:35:47.300531+00:00

Deploy Client on iOS Using Intune - Netskope Knowledge Portal
Deploy Client on iOS Using Intune
Netskope supports Intune on-demand and per-app VPN for iOS devices. This can provide users with access to corporate applications, data, and resources while keeping your sensitive information secure.
– On-Demand VPN profile applies to the entire iOS device. iOS devices support only one active On-Demand VPN profile. If there are two or more On-Demand VPN profiles, only one remains active. To steer traffic to Netskope with On-Demand VPN profile, disable or remove all other On-Demand VPN profiles.
– Assign Per-App VPN  to individual iOS apps. A Per-App VPN profile can co-exist with an On-Demand VPN profile simultaneously. Applications you configure for the Per-App VPN profile takes precedence over the On-Demand VPN profile and steers the application traffic to Netskope.
Prerequisites
Before you configure Intune:
In the Netskope UI, go to
Settings
>
Manage
>
Certificates
>
Signing CA
. Download the Netskope Root certificate.
– This bundle includes three certificates: Regional, Intermediate, and nsrootCA. Since Intune can only ingest a single certificate per profile, these must be separated into three individual certificates, and then three corresponding certificate profiles must be created in Intune.
– The Netskope Root certificate is in .pem format. Convert it to .cer or .crt format before importing. To convert certificates from .pem to .cer, run the following command in a terminal:
openssl x509 -inform PEM -in <filename.pem> -outform DER -out <filename.cer>
Locate and save
Organization ID
token from
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distribution
.
Locate and save
Secure Enrollment
tokens from
Settings
>
Security Cloud Platform
>
Netskope Client
>
MDM Distribution
.
Ensure user accounts provisioned within the MDM/EMM platform match with those provisioned with the Netskope tenant.
Create a Trusted Netskope Root Certificate Profile
You need to download the Netskope Root certificate from the Netskope UI to complete these steps. To get the certificate, go to
S
ettings
>
Manage
>
Certificates
>
Signing
CA
.
To create a trusted Netskope certificate profile:
In the Intune UI proceed to
Devices
>
iOS/iPadOS
>
Configuration profiles
.
Click
Profile > Create Profile
. Enter and select these parameters:
Name:
Enter a unique name.
Platform:
iOS.
Profile type:
Trusted certificate.
In the
Trusted Certificate
panel, provide a name in the
Basics
tab and click
Next
.
In the
Configurations settings
tab, upload the Netskope Root certificate.
Review your settings, and click
Create
.
Create another configuration profile and repeat the same steps to upload Netskope intermediate certificate.
Deployment Procedure
Perform the instructions in the following sections to deploy Netskope Client using Intune.
Enroll Netskope iOS Client in MS Intune
Go to
Apps
>
iOS/iPadOS
apps
.
Click
+ Add
.
Select
iOS store app
from the
App type
drop-down menu.
Purchase Netskope Client through the respective tools if your organization is leveraging Apple Business Manager or Apple School Manager. The Netskope Client shows up in the list of applications available for deployment after the tokens are synchronized.
Click
Select
.
From
App Information
, click
Search the App Store
and select
Netskope Client
app to add the application.
Click
Select
. The
App Information
section displays more information on the UI. No additional configuration is required here.
Click
Next
.
Assign the application to devices or users. Click
Next
to continue.
Click
Create
to complete creating the application.
Zero Touch Enrollment with On-demand VPN Configuration
To configure:
Go to
Devices
>
iOS/iPadOS
>
Configuration
>
Create New Policy
.
Select
Profile Type
as Templates and
Template name
as Custom.
Click
Create
.
In
Basics
, enter a descriptive name for the profile. For example, iOS Zero Touch On-Demand.
Click
Next
.
In
Configuration settings
:
Enter a descriptive name in
Custom configuration profile name
.
Save the following XML content and make the  required changes.
After updating the XML file with your tenant specific details upload the file under the
Configuration profile file
.
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>PayloadContent</key>
   <array>
       <dict>
           <key>IPv4</key>
           <dict>
               <key>OverridePrimary</key>
               <integer>1</integer>
           </dict>
           <key>PayloadDescription</key>
           <string>Configures VPN settings</string>
           <key>PayloadDisplayName</key>
           <string>VPN</string>
           <key>PayloadIdentifier</key>
           <string>com.apple.vpn.managed.BB54E90D-B34E-4C96-97B3-EBC608E10C7C</string>
           <key>PayloadType</key>
           <string>com.apple.vpn.managed</string>
           <key>PayloadUUID</key>
           <string>BB54E90D-B34E-4C96-97B3-EBC608E10C7C</string>
           <key>PayloadVersion</key>
           <integer>1</integer>
           <key>Proxies</key>
           <dict>
               <key>HTTPEnable</key>
               <integer>0</integer>
               <key>HTTPSEnable</key>
               <integer>0</integer>
           </dict>
           <key>UserDefinedName</key>
           <string>Netskope VPN</string>
           <key>VPN</key>
           <dict>
               <key>AuthenticationMethod</key>
               <string>Password</string>
               <key>IncludeAllNetworks</key>
               <integer>0</integer>
                <key>OnDemandUserOverrideDisabled</key>
                <true/>
               <key>OnDemandEnabled</key>
               <integer>1</integer>
               <key>OnDemandRules</key>
               <array>
                 <dict>
                 <key>Action</key>
                 <string>Connect</string>
                 </dict>
               </array>
               <key>RemoteAddress</key>
               <string>gateway-<tenant-URL></string>
           </dict>
           <key>VPNSubType</key>
           <string>com.netskope.Netskope</string>
           <key>VPNType</key>
           <string>VPN</string>
           <key>VendorConfig</key>
           <dict>
               <key>AddonHost</key>
               <string>addon-<tenant-URL></string>
               <key>OrgKey</key>
               <string><your organization ID></string>
               <key>UserEmail</key>
               <string>{{mail}}</string>
               <key>enrollauthtoken</key>
               <string><Secure Enrollment Auth token></string>
  <key>enrollencryptiontoken</key>
               <string><Secure Enrollment Encryption token></string>
           </dict>
       </dict>
   </array>
   <key>PayloadDisplayName</key>
   <string>Netskope VPN</string>
   <key>PayloadIdentifier</key>
   <string>MacBook-Air</string>
   <key>PayloadRemovalDisallowed</key>
   <false/>
   <key>PayloadType</key>
   <string>Configuration</string>
   <key>PayloadUUID</key>
   <string>64A21995-FBDA-4824-8DA9-1789F40E4869</string>
   <key>PayloadVersion</key>
   <integer>1</integer>
</dict>
</plist>
You can also add {{userprincipalname}} as the string value instead of {{mail}}.
Replace the following parameters with values according to your tenant:
–
Line #
52
:  gateway-<tenant-URL>
–
Line #
61
: addon-<tenant-URL>
– Line #63: <organization ID>
–
Line #6
7
: <Secure Enrollment Auth token>
–
Line #6
9
: <Secure Enrollment Encryption token>
Assign the appropriate user/device groups.
Click
Next
.
Review the configuration.
Click
Create
.
Netskope client is capable of enrolling silently without any user action when enrollment data is supplied through XML using a Configuration Profile. Currently Intune does not support variables such as {{mail}} in key:value pairs of VPN profiles. Hence App Configuration is used as a primary enrollment data.
Setup for Per-App VPN Configuration
The following instructions do not include Zero Touch Enrollment for Per-App VPN.
Go to
Apps
>
App Configuration Policies
to add the required policies to Unified Netskope Client.
Click
+Add
and select
Managed Devices
.
In the
Basics
section of the
Create app configuration policy
page, enter the following details and click
Next
:
Name:
Give a name to the policy.
Platform:
Select iOS/iPadOS.
Targeted App:
Select Netskope Client.
In the
Settings
section of the
Create app configuration policy
page, select the Use configuration designer option from the Configuration settings format dropdown menu.
Provide the required Key-Value pairs to complete the Netskope Client enrollment process:
UserEmail:
{{mail}}
If UPN is being synced to Netskope from AD, use the key:value pair –
UserEmail: {{userPrincipalName}}
.
AddonHost
: <addon-hostname>.
For example, addon-
<tenant-URL>
.
OrgKey:
<Organization Key>
enrollauthtoken:
< Authentication Token>
enrollencryptiontoken:
<Encryption Token>
Use keys <enrollauthtoken> and <enrollencryptiontoken> only if you have enabled
Secure Enrollment
in your tenant.
–
enrollauthtoken
specifies the
Enforce authentication of Netskope Client Enrollment
token (mandatory).
–
enrollencryptiontoken
specifies the
Enforce encryption of initial configuration of Netskope client
token(optional).
In the
Assignments
section of the Create app configuration policy page, select groups from the Assign to dropdown menu to which the policy is applied and click
Next
.
In the
Review + create
section of the Create app configuration policy page, review the configuration and click
Create
.
Create VPN Profile
Once the Netskope Client is installed, it attempts to create an On-Demand VPN profile on the mobile device that results in the additional user prompt. In order to suppress user prompts as well as customize VPN profile settings (such as create Per-App instead of On-Demand), it is recommended to create and push VPN profile with Intune. To learn more, view
Create Profile
.
Go to
Devices
>
iOS/iPadOS  policies
>
Configuration Profiles
>
Create Profile
.
Select
Profile Type
as Templates and Template name as
VPN
.
Click
Create
.
In
Basics
, enter a descriptive name for the profile and click
Next
.
In
Configuration
settings
, choose the
Connection Type
as
Custom VPN
.
Once you select the connection type, do the following:
Under
Base VPN
and provide the following:
Connection name
VPN server address:
gateway-
<tenant-URL>
Authentication method:
Username and Password
VPN identifier:
com.netskope.Netskope
Enter the following in the key-value pair section according to your requirement:
Key
Value
Description
SingleSignOn
True
-
TerminateOnSleepThreshold
Recommended value range: 20-75 seconds.
Value: 0 (default) means existing legacy behavior (no sleep/wake handling).
Netskope Client to check the sleep time after it wakes up from the sleep mode without any network activity. If the value is above the specified value in seconds, it gets terminated immediately.
ForceDisabledSteering
True
If deployment requires NPA only traffic steering.
OnDemandConnectionsHoldTimeout
Numeric value in seconds. For example, 20
To define timeout to control the iOS On-demand connections hold feature. This numeric value in the VPN profile can hold the connection for a longer time until it establishes the tunnel successfully and handles traffic. Netskope recommends using values that are large enough to cover normal connection time.
Key-value pairs for Netskope Client enrollment using IDP in iOS devices (Optional)
The following four key-value pairs are optional and you can use them only if you need to perform user enrollment using IDP.
Key
Value
Description
IDPMode
Embedded, or
Scheme
Enter the mode to specify the browser support to be enabled during Client installation. Mode is a string with values and you can add one of the following values in the script.
Embedded: Default value and opens the existing mini-browser (Applies only for NPA reauthentication).
Scheme:  Uses default browser.
IDPpreferEphemeral
True, or
False
If you set the value to:
True: It means it requests an ephemeral (private) browser window from the default browser.
False: It means it requests a regular (non-private) browser window from the default browser.
IDPTenant
<tenant-name>
If the tenant URL is acme.eu.goskope.com, tenant value is acme.
IDPDomain
<domain-name>
If the tenant URL is acme.eu.goskope.com, then domain is eu.goskope.com.
IDPScope
all
This string applies only to Netskope Private Access (NPA) re-authentication. Set the value of IDScope to NPA to use an external browser for NPA re-auth only. This is useful while using a non-IDP enrollment method.
Note:
Use this option for the enablement of default browser for NPA re-authentication
Custom Device Identity Key-Value Pairs for iOS
Netskope Client for iOS previously generated its own opaque UUID as a device identifier and hostname; always reported serial number as “N/A” (Apple platform limitation). This resulted in a challenge for  the IT and security administrators to match a device in the Netskope Web UI to a known asset in their MDM or help desk system thereby slowing down incident response and device auditing. Use the following optional VPN profile keys that MDM can populate at profile-push time:
Key
Value
Description
CustomDeviceSerialNumber
Provide an asset serial number. If not defined, the system displays it as “"N/A" in the webUI.
Use this variable to send serial number of the device:
{{SerialNumber}}
CustomDeviceSerialNumber is a dynamic value. It takes the current value in the MDM VPN profile on each connection.
CustomDeviceName
Provide a human-readable device name.
Use this variable to send device name:
{{DeviceName}}
CustomDeviceName is a dynamic value. It takes the current value in the MDM VPN profile on each connection.
For example, consider the following device key-value pairs added for iOS:
The Devices webUI displays the Device Name and Serial Number according to the values added in the MDM profile.
Under
Automatic VPN
, choose the following VPN type:
Per-App VPN
Specify Provider as Type packet-tunnel.
Specify associated domains, Safari URLs, and excluded domains if necessary.
Assign the appropriate user/device groups and click
Next
.
Review the configuration and click
Create
Associating the Per-App VPN profile with the Apps
Associate the Per-App VPN profile with the applications to steer through the VPN connection.
In the MEM admin console, go to
Apps > All apps
, select one of the apps listed there, and then click
Properties
.
In the app
Properties
page, click
Edit
for Assignments.
In the
Required
section, click
Add Group
. Search and choose one or more groups, and then click
Select
.
Click
VPN
and select appropriate Per-App VPN configuration from the dropdown menu.
In this Topic
Deploy Client on iOS Using Intune

---
## Netskope Client Debug Mode
**URL:** https://docs.netskope.com/en/netskope-client-debug-mode/
**Last Modified:** 2025-10-07T17:00:18+00:00
**Scraped:** 2026-06-26T09:36:32.817162+00:00

Netskope Client Debug Mode - Netskope Knowledge Portal
Netskope Client Debug Mode
The Netskope Client debug mode offers an easy and efficient way to consolidate all necessary information required for troubleshooting. In the event of any issues, activate debug mode and reproduce the issue. Once the issue occurs, stop the debug mode and share the generated archive file with Netskope.
When the Netskope Client debug mode is activated, it performs the following:
Inner packet capture with multiple file rotations.
Outer packet capture with multiple file rotations.
The Netskope Client service debug logs rotate across multiple files.
Start debug mode with administrative privileges to collect the following information:
Run the
nsdiag
command as an administrator on Windows and
sudo
on MacOS
On Mac, collect the
sysdiagnose
log (this process can take a few minutes).
On Windows,
Generate memory dumps for the Netskope Client service (stAgentSvc.exe) and the current tenant user UI (stAgentUI.exe).
If
Protect Client configuration and resources
is enabled, debug Mode does not collect memory dumps.
Collect Windows Application and System Event logs.
Disables
Save Logs
option on the Client UI.
Disables
Advanced Debugging
Client UI features such as
Set Log Level
,
Save Driver Logs
,
Inner Packet Capture
, and
Outer Packet Capture
.
Disables
nsdiag
command from setting log levels, initiating inner and outer packet captures from the Netskope Client UI, and increasing the log file size.
Debug Mode Command
Windows
nsdiag -b [start | stop | status | cleanup] -l [ dump | debug | info | error | critical] -s <snap length> -m <max debug log files> -i [disable | maxInnerPcapTotalSize in MB] -e [disable | maxOuterPcapTotalSize in MB] -c [disable | CPU sample interval in second] -r [enable | disable driver log] -t [duration of time in minutes] -o <output archive path>
macOS
nsdiag -b [start | stop | status | cleanup] -l [ dump | debug | info | error | critical] -s <snap length> -m <max debug log files> -i [disable | maxInnerPcapTotalSize in MB] -e [disable | maxOuterPcapTotalSize in MB] -c [disable | CPU sample interval in second] -d [enable | disable sysdiagnose log] -t [duration of time in minutes] -o <output archive path>
Linux
nsdiag -b [start | stop | status | cleanup] -l [ dump | debug | info | warning | error | critical] -s <snap length> -m <max debug log files> -i [disable | maxInnerPcapTotalSize in MB] -e [disable | maxOuterPcapTotalSize in MB]-t [duration of time in minutes] -o <output archive path>
Parameter
Description
-b [start | stop | status | cleanup]
start/stop/get status/cleanup debug mode
-l [ dump | debug | info | error | critical]
Set debug mode log level. Default value is debug.
-s <snap length>
Set the inner and outer packet capture snap length in debug mode. Default value is 0.
-m <max debug log files>
Set the maximum debug log file number in debug mode. Default value is 10.
-i [disable | maxInnerPcapTotalSize in MB]
Set inner packet capture total size in debug mode. Default value is 600MB.
-e [disable | maxOuterPcapTotalSize in MB]
Set outer packet capture total size in debug mode. Default value is 800MB.
-c [disable | CPU sample interval in second]
– Windows and Mac only.
– Snapshot all processes CPU usage in every (interval) seconds. The result will be in new nsDMCpuUsage.log in Netskope Client log folder.
-r [enable | disable driver log]
– Windows only.
– Enable/disable driver log in debug mode.
-d [enable | disable]
– macOS only.
– Enable/disable collecting sysdiagnose log.
Note: It takes a few minutes to collect sysdiagnose log details.
-t [duration of time in minutes]
Optional: Default is 2160 minutes or 36 hours
– Minimum value is 1 (minute).
– Maximum value is 86,400 minutes or 60 days
– Netskope Client automatically stops the debug mode and collects the required information after the duration.
-o <output archive full path>
Required: set output archive file (.zip) full path.
– Netskope Client automatically adds .zip extension if the specified file does not have it.
– If it is configured in -b start command, it is not required in -b stop command.
Stop Debug Command
The Netskope Client continues to collect information until the user executes the command
nsdiag
-b
stop to terminate debug Mode.
A device reboot would not stop debug Mode.
Debug Command Examples
Example 1
Users frequently encounter issues with Netskope Client. To troubleshoot this, initiate debug mode using the default parameters and then attempt to reproduce the issue as follows:
nsdiag -b start -o ~/debug/NSClientLogs.zip
When the issue occurs, stop the debug mode immediately. A file named NSClientLogs_timestamp.zip (for example, NSClientLogs_2025.04.03_16-16-35-0800.zip) is generated in the ~/debug folder. Share this file with Netskope Support.
nsdiag -b stop
Example 2
Users occasionally encounter issues that are not easily reproducible on demand; it might take several hours or even days for the problem to manifest. To troubleshoot, they can initiate debug mode as follows:
Before proceeding, ensure that there is sufficient disk space available and adjust the parameters as necessary.
nsdiag -b start -s 200 -i 1000 -e 1200 -m 50 -o ~/debug/NSClientLogs.zip
Set inner pcap total size to 1000M bytes.
Set outer pcap total size to 1200M bytes.
Set total 50 debug log files.
When the issue occurs after several hours or days, users can promptly disable the debug mode.
nsdiag -b stop
Example 3
Netskope Client experiences instability which may manifest as process hangs or crashes. As an admin run the following:
nsdiag -b start -o “c:\debug\NSClientLogs.zip“
When the issue occurs, stop the debug mode immediately. To stop the debug mode, run the following in the command prompt:
nsdiag -b stop
Example 4
If there is a performance issue due to tunnel loading, run the following in the command prompt:
nsdiag -b start -l info -s 200 -i 1200 -e disable -r disable -c 3 -o "c:\debug\loadtest.zip"
In the preceding command, set the following parameters:
Set log level to “info”
Set snaplen to 200
Set inner pcap total size to 1200M bytes
Disable outer pcap
Disable driver log
You can evaluate CPU usage every three seconds. Disable the debug mode after validation is complete.
Example 5
If the administrator wants to initiate the debug mode in a macOS device and gather all relevant information including sysdiagnose log, perform the following:
​​sudo nsdiag -b start -o ~/debug/1.zip
nsdiag -b stop
Example 6
If the administrator wants to initiate the debug mode on a macOS device without collecting the sysdiagnose log, perform one of the following:
nsdiag -b start -o ~/debug/1.zip
nsdiag -b stop
OR
sudo nsdiag -b start -o ~/debug/1.zip
nsdiag -b stop -d disable
Example 7
To clean up all debug mode files after stopping the debug mode:
nsdiag.exe -b cleanup
Example 8
The administrator wants to specify running the Debug Mode for only
60 minutes
with the default parameters.
-b start -t 60 -o outputFile(.zip)
After 60 minutes, the Debug mode stops automatically, and collects the required information to the output file in the format
outputFile_YYYY.MM.DD_HH-MM-SS-UTC.zip
file.
Restarting Netskope Client in between 60 minutes does not stop the debug mode.
Verify Debug Status
To verify the status of debug mode, you can use one of two methods:
Using command line:
nsdiag -b status
Using Netskope Client UI:
When debug mode is enabled, the
Save Logs
… menu appears greyed out.
Click
Advanced Debugging
.
The options for Set Log Level, Save Driver Logs, Inner Packet Capture, and Outer Packet Capture are also greyed out, and shows the current status (Start or Stop).
In this Topic
Netskope Client Debug Mode

---
## Service Account Migration and Netskope Client Auditing
**URL:** https://docs.netskope.com/en/service-account-migration-and-netskope-client-auditing/
**Last Modified:** 2025-10-14T18:56:46+00:00
**Scraped:** 2026-06-26T09:36:43.295904+00:00

Service Account Migration and Netskope Client Auditing
This article is a comprehensive guide for Netskope administrators migrating API integrations from the legacy REST API V2 token model to the secure, role-driven RBAC V3 Service Account framework.
This migration is a critical step, as the RBAC V3 framework represents a mandatory architectural shift to a decentralized,
“API First” architecture
, ensuring consistent authorization for both WebUI and REST API interactions.
REST API V2 Token Deprecation and Mandatory Service Account Workflow
The previous REST API V2 token provisioning workflow is deprecated and will become unavailable after RBAC V3 functionality is activated.
V2 Token Deprecation Status:
You can no longer provision new V2 tokens using the deprecated interface (Settings > Tools > Rest API V2) once RBAC V3 is enabled.
Existing V2 Tokens:
Any existing V2 tokens will continue to function until their specified expiration date. However, these tokens
cannot be extended
.
New Workflow Requirement:
All future token provisioning must be performed using the new Service Account creation process, which is fully integrated with the RBAC V3 role management framework.
Proactive API Client Auditing (Critical Pre-Enforcement Step)
Before enabling IP allowlists for any new RBAC V3 role or globally, administrators
must
conduct a proactive audit of all API client source IPs. This is the only way to prevent a catastrophic service outage.
The Critical Warning: Preventing Self-Inflicted Denial-of-Service (DoS)
Enabling a role-based or global IP allowlist without a complete inventory of existing API clients can result in a
“self-inflicted denial-of-service attack.”
Activating the allowlist will instantly block all API calls from unlisted IPs, halting critical security and operational integrations, including:
Security Information and Event Management (SIEM) platforms ingesting logs
Security Orchestration, Automation, and Response (SOAR) tools orchestrating responses
SCIM user provisioning flows
Custom scripts and automated reporting tools
Using the REST API for IP Inventory
The definitive method and the most reliable source of truth for administrative API activity is the Netskope REST API V2 itself, not the UI Audit Log.
Step 1: Identify Audit Scope
Recommended Audit Window:
Use a minimum of a
90-day audit window
. This period aligns with Netskope’s default log retention and ensures both frequent and infrequent API activities are captured.
Required Endpoints:
Query the REST API v2
datasearch
endpoints, which are designed for ad-hoc queries, focusing on events most likely to contain API activity:
◦
/api/v2/events/datasearch/alert
◦
/api/v2/events/datasearch/application
◦
/api/v2/events/datasearch/page
Key Data Point:
Extract the value of the
srcip
field from the returned log records, as this contains the source IP address of the API client.
Step 2: Extract Inventory Using a Script (Example)
To effectively handle pagination and process the large volume of data, programmatic querying is required.
The core task is to programmatically query these event logs, extract the
srcip
, and aggregate a final, unique list of all source IP addresses.
Example Implementation Logic:
The script should iterate through the defined
datasearch
endpoints for the 90-day period.
It must handle
pagination
by incrementing the
offset
parameter until no more records are returned.
It should parse the JSON response and extract unique
srcip
values, ultimately providing an exhaustive list of all client source IPs.
Step 3: Implement the Role-Based Allowlist
Review and Approve:
The aggregated list of unique IPs must be reviewed to correlate each IP with its owner and purpose (e.g., SIEM platform, custom tool).
Configure Role Allowlist:
Navigate to the role settings (Settings > Administration > Roles) and populate the
IP Allowlist
section with the approved IPv4 addresses.
◦ The IP addresses must be
space-delimited
and be valid
IPv4
addresses.
Critical Security Note:
The role-based IP allowlist
supersedes and overrides
any previously configured global IP allowlist settings. If enabled on the role, it becomes the sole source of truth for access control for that service account.
SCIM Integration Update: Step-by-Step Migration to Service Account V3
The migration from a legacy API token to a new RBAC V3 Service Account requires a sequential, three-part process: Role Creation, Service Account Creation, and Integration Update.
Step 1: Role Creation (Principle of Least Privilege)
Since RBAC V3 is role-driven, you must
create the role first
before creating the service account.
Navigate to Role Management:
Go to
Administration > Roles
and click
New
.
Define Permissions (PoLP):
Assign a descriptive name (e.g.,
scim_provisioner
). Apply the
Principle of Least Privilege (PoLP)
.
◦ For SCIM, select the
Administration
category.
◦ Explicitly
deselect permissions for UI functions
and any other non-essential operations, as service accounts are non-interactive.
◦ Set the permission level to
Manage
for the
Users
and
Group
APIs, as these are required for SCIM provisioning.
Apply IP Allowlist:
If you performed the audit (Section 2), navigate to the
IP Allowlist
tab and add the approved source IPv4 addresses of your Identity Provider (IdP).
Step 2: Service Account and Token Creation
Create Service Account:
Navigate to
Administration > Administrators & Roles
and click
Service Account
.
Configure Account:
Type the name of the service account and select the custom role created in Phase A (e.g.,
scim_provisioner
).
Set Expiration:
Specify the token’s expiration period (e.g., 12 months).
Generate and Store Token (Critical Step):
Click
Create
. The API token is displayed
only once
upon successful creation. It is
critical to copy and securely store this token immediately
as it cannot be retrieved later.
Step 3: SCIM Integration Update
Update API Token:
In your Identity Provider’s (IdP’s) SCIM provisioning settings (e.g., Okta or Entra ID), replace the old V2 API token with the
new V3 Service Account token
.
Update Base URL:
The older SCIM service URL is being deprecated and must be modified to point to the new RBAC V3-compliant endpoint.
◦
New Base URL Format:
https://<tenant-name>.goskope.com/api/v2/scim
.
Test Connection:
After updating both the token and the base URL,
test the connection
to ensure the integration is functioning correctly.
Troubleshooting Connection Errors
If the connection test fails, the most common reason is a conflict with the role-based IP allowlist.
Verify Source IPs:
Check the role’s IP allowlist configuration to ensure that the current source IP addresses used by your specific SCIM provider (e.g., Okta’s cell IPs or Microsoft Entra ID ranges) are accurately included in the role’s allowlist. Remember that
the role-based allowlist supersedes any global settings
.
In this Topic
Service Account Migration and Netskope Client Auditing

---
## Netskope Client For Linux
**URL:** https://docs.netskope.com/en/netskope-client-for-linux/
**Last Modified:** 2025-11-05T18:00:59+00:00
**Scraped:** 2026-06-26T09:37:15.918180+00:00

Netskope Client For Linux - Netskope Knowledge Portal
Netskope Client For Linux
This document describes the available deployment methods and user enrollment options when installing the Netskope Client on Linux devices.
Supported Versions
Refer to
Netskope Client Supported OS and Platform
for more details on the supported Linux versions.
Download Client Packages
You can download Netskope Client installers from
Download Netskope Client and Scripts
.
Prerequisites
Netskope Client for Linux relies on
iptables
for steering traffic and is a requirement for all Netskope Client for Linux deployments.
Netskope Client Installation Methods
The Netskope Client for Linux supports webUI and command-line installations enrolling users by email, UPN, or IDP.
Installation Using Command Line Interface (CLI)
Refer to the following instructions to complete the Netskope Client deployment once the Client package is downloaded onto the Linux device.
Netskope Client supports Windows Subsystem for Linux(WSL) version 2 that allows you to run  Linux on your Windows devices without the need of a separate virtual machine. Netskope Client extends command-line interface(CLI) only support for WSLv2.
To learn more, view
Windows Support for WSLv2
.
Install And Enroll by Email ID
Use the following command to install and enroll using email ID:
sudo ./STAgent.run -H <tenant hostname> -o <org key> -m <email address>
For example,
sudo ./STAgent.run -H abc.goskope.com -o abc123xyz -m user@example.org
STAgent.run {-H | --tenant-hostname tenant_hostname}            
             {-o | --orgkey orgKey}            
             {-m | --email email_address}             
             [-a | --enroll-auth-token enroll_authentication_token]          
             [-e | --enroll-encrypt-token enroll_encryption_token]            
             [-c | --cli]
Options:-H --tenant-hostname: Tenant hostname
        -o --orgkey: org key
        -m --email: User email
        -a --enroll-auth-token: enroll authentication token
        -e --enroll-encrypt-token: enroll encryption token
        -c --cli: This is a flag for CLI only mode and no value
                  When this argument is present, UI will not be installed
All arguments mentioned within {} are mandatory.
Install And Enroll By UPN
Use the following command to install and enroll by UPN:
sudo ./STAgent.run -H <tenant hostname> -o <org key>.
For example,
sudo ./STAgent.run -H abc.goskope.com -o abc123xyz
STAgent.run {-H | --tenant-hostname Tenant_hostname}             
             {-o | --orgkey orgKey}           
             [-u | --upn UPN]            
             [-a | --enroll-auth-token enroll_authentication_token]        
             [-e | --enroll-encrypt-token enroll_encryption_token]           
             [-c | --cli]
Options:-u --upn: User UPN
– All arguments mentioned within {} are mandatory.
– Requires a UPN value while performing user enrollment of non-domain joined devices by UPN. The installer fails and quits if the UPN value is missing.
Install And Enroll By IDP
Use the following command to install and enroll by IDP:
sudo ./STAgent.run -i
STAgent.run {-i | --idp} 
             [-t | --tenantname tenant_name]
             [-d | --domain tenant_domain]
             [-e | --enroll-encrypt-token enroll_encryption_token]     
Options:-i --idp: This is a flag with no value. 
                  When this argument is present,installer will enroll by IDP. All other options will be skipped in IDP mode.
        -t --tenantName: tenant name
        -d --domain: tenant domain
        -e --enroll-encrypt-token: enroll encryption token
– All arguments mentioned within {} are mandatory.
– Ensure that
STAgent.run
file must have executable permissions.
Installation Using WebUI
After you download the Netskope Client to the end-user device, perform the following steps to setup Client and connect to the Netskope Cloud:
From your terminal, run the following command:
sudo ./STAgent.run -e <encryption_token>
Ensure that you add the encryption token mapped to your tenant.
After the installation is complete, a pop-up is displayed to the user to enter the Netskope Tenant name and select the tenant domain. This information is shared with the user by their respective IT admin.
Click
Next
to continue with enrollment. The user is redirected to their IDP login screen. Authentication status message is displayed in the browser.
Once the user enrollment is complete, you can see the Client icon on the taskbar. Click the Client icon to view the configuration details.
Netskope Client Installation for Debian
Netskope Client for Linux relies on
iptables
for steering traffic and is a requirement for all Netskope Client deployments in Linux. However, the modern operating systems such as Debian 12 shifted from
iptables
to
nftables
, and therefore
iptables
components are not installed on Debian by default. To ensure a seamless installation of Netskope Client for Linux on Debian, the Netskope installer verifies the presence of
iptables
. If
iptables
are missing, the installer issues a warning and automatically installs the necessary libraries.
Press
y
to install the iptables package automatically.
Verify Enrollment After Installation
To verify successful token enrollment during installation, refer to following instructions, based on your chosen enrollment method:
Validation for IDP Enrollment
When enrolling with an Identity Provider, you can verify both the saved “keycard” and the final Netskope Client status using one of the following methods:
Verify the Encryption Token File (Your “Keycard”): Open a terminal and run the following command to see the saved token:
sudo cat /opt/netskope/stagent/.eetk
If the terminal displays a lengthy string of random characters, this confirms that your “keycard” is successfully saved to the device.
If it displays an error such as “No such file or directory,”, it indicates and issue with the token application.
In your terminal, run the following:
bash
# Step 1: Launch the client’s command-line interface
nsclient
# Step 2: At the Netskope > prompt, check the configuration
show-config
The command displays the Client Configuration details such as Gateway, Organization, User Email, and more. This confirms successful enrollment.
Validation for Email or UPN Enrollment
When you enroll with an Email or UPN, no token file is saved. In your terminal, run the following:
bash
# Step 1: Launch the client’s command-line interface
nsclient
# Step 2: At the Netskope > prompt, check the configuration
show-config
The command results display Client Configuration details such as Gateway, User Email, and so on. This confirms that the token-based enrollment was successful. The absence of the .eetk file is normal and expected in this mode.
Uninstall Client in Linux
Use the command
sudo /opt/netskope/stagent/uninstall.sh
to uninstall Netskope Client in Linux.
Additional CLI Commands
Use the ‘help’ command to understand the additional commands available for managing Netskope Client in a Linux device. For example:
To enable Netskope Client in CLI and then to quit:
~$ nsclient
start process....
===== Netskope Client CLI,  Version: 200.200.0.100 =====
Copyright(c) 2022 Netskope, Inc. All Rights Reserved.
Please enter <help> for available commands.
Netskope> enable
Enabling Netskope Client...
Netskope Client enable success.
Netskope> quit
To display Netskope Client Status
~$ nsclient
start process....
===== Netskope Client CLI,  Version: 99.0.0.1090 =====
Copyright(c) 2022 Netskope, Inc. All Rights Reserved.
Please enter <help> for available commands.
Netskope> show-status
Netskope Client enabled
To display Netskope Client Configuration
Netskope> show-config
Show configuration in progress...
Netskope Client Configuration
Gateway: gateway-qa.de.goskope.com
Organization: Netskope Inc
Gateway IP: 163.116.140.35, POP: US-SFO1
User Email: jjia@netskope.com
Client Configuration: client_config1
Steering Configuration: jjia-mygroup2
Device Classification: unmanaged
Tunnel Protocol: TLS
Private Access: Connected (User Tunnel)
Private Access Gateway IP: 163.116.138.23
On-Premises Check: Remote
Traffic Steering Type: All Web Traffic
Config Updated: 10:27:26,  1st Dec, 2022
configuration update avaliable.Pleasae use <update-config> command to update latest configuration
To display the blocked events
Netskope> show-blocked-event
Blocked Event:
App Name: [opera], Last Access Time: Thu Dec  1 21:01:20 2022
To update the Client Configuration
Netskope> update-config
Update configuration in progress...
startConfigUpdate->bNeedUpdate=1
configuration update avaliable.
Please use <update-config> command to update latest configuration
Command
Description
–help
Usage for Netskope Client CLI.
– enable
Netskope Client status.
– disable
Disable Netskope Client.
– show-status
Netskope Client status.
– show-config
Display Netskope Client configuration.
– update-config
Update Netskope Client configuration.
– show-blocked-event
Display Netskope Client blocked event(s).
– set-log-level
Reset Netskope Client log level, <debug|info|warning|error|critical>
– save-logs
Save Netskope Client diagnostic information.
– start-pkt
Start packet capture, <inner|outer> packet <inner len from 0 to 9999 byte|outer size from 0 to 99 MB> Please use the ‘stop-pkt’ command to exit.
– stop-pkt
Stop packet capture.
– start-speedtest
Start speed test, testing <download|upload> <1|10|100>MB file.
– show-pa
Show Private Access status.
Limitations
Netskope Client for Linux does not support docker configuration. Netskope Client cannot install certificates for web traffic initiated from Containers. The Netskope Client can only install certificates for the web traffic initiated from the apps running on Linux host devices.
The DNS tunneling feature available in Windows 11 is part of Windows Sub-System for Linux (WSL). This handles DNS requests directly within the WSL environment. The Linux instances running in WSL does not send DNS requests through Network Address Translation (NAT) to the host anymore. This causes the Netskope Client to not intercept the requests through routing. As a workaround,  disable the DNS tunneling in the .wslconfig file on your host, shutdown, and then restart the WSL instance.
To disable the tunneling feature:
Create the
.wslconfig
file using the following:
[wsl2]
dnsTunneling=false
Copy this file to your Windows user profile folder:
C:\Users\<YourUsername>\.wslconfig
Run the following command in
PowerShell or CMD
to shutdown the WSL:
wsl --shutdown
Launch Ubuntu in WSL again, and run the following command:
cat /etc/resolv.conf
You can now view the following:
nameserver 172.22.240.1
(or another 172.x.x.x address depending on your NAT gateway).
In this Topic
Netskope Client For Linux

---
## Deploy Netskope Client On Citrix DaaS With Azure Virtual Desktop
**URL:** https://docs.netskope.com/en/deploy-netskope-client-on-citrix-daas-with-azure-virtual-desktop/
**Last Modified:** 2025-11-05T18:00:24+00:00
**Scraped:** 2026-06-26T09:37:17.048801+00:00

Deploy Netskope Client On Citrix DaaS With Azure Virtual Desktop - Netskope Knowledge Portal
Deploy Netskope Client On Citrix DaaS With Azure Virtual Desktop
This document describes how to deploy Netskope Client on Citrix DaaS with Azure Virtual Desktop supporting multi-user environments.
Overview
This virtual environment consists of Windows 11 multi-user sessions in Azure Virtual Desktop and end-users with Citrix DaaS. To learn more, view
Citrix DaaS with Azure Virtual Desktop Hybrid
.
In this document, Netskope uses FSLogix for user profile management. To learn more, view
Configure Profile Containers Using FSLogix
.
Environment
Citrix Virtual apps and Desktops 7 2507 LTSR CU2 (2507.0.100.428)
FSLogix: 3.25.202.4223
Windows 11(22H2)
Netskope Client version: 132.0.0.
Prerequisites
Check the following prerequisites before deploying Netskope Client on your VDI:
Add Certificate Pinned Apps:
Create separate Certificate Pinned Applications for the following:
Go to
Settings
>
Security Cloud Platform
>
App Definitions
to create Certificate Pinned Apps. To learn more, view
Creating a Custom Certificate Pinned Application
.
FSLogix processes
Citrix DaaS processes
Refer to the following table to understand the process names that you need to add for each Citrix DaaS and FSLogix:
Certificate Pinned App
Process Names
Citrix DaaS
PicaSvc2.exe,brokeragent.exe,lsass.exe,cseengine.exe,wfica32.exe,concentr.exe,Receiver.exe,
SelfService.exe,wfcrun32.exe,CDViewer.exe,AuthManSvr.exe,UpdaterService.exe,redirector.exe,
SelfServicePlugin.exe,ssonsvr.exe,PrimaryAuthModule.exe,storebrowse.exe,CtxWebBrowser.exe,
Browser.exe,CitrixWorkspaceBrowser_proxy.exe,CitrixWorkspaceBrowser.exe,native_bridge.exe,
nmh_launcher.exe,cpviewer.exe,Ctx64Injector64.exe,CtxBrowserInt.exe,CtxCFRUI.exe,CtxTwnPA.exe,
HdxBrowser.exe,HdxRtcEngine.exe,icaconf.exe,migrateN.exe,NMHost.exe,pcl2bmp.exe,PdfPrintHelper.exe,
RawPrintHelper.exe,SetIntegrityLevel.exe,WebHelper.exe,wfcwow64.exe,XpsNativePrintHelper.exe,
XPSPrintHelper.exe,HdxBrowserCef.exe,WinDocker.exe,chrome_pwa_launcher.exe,notification_helper.exe,
chrmstp.exe,setup.exe,usbinst.exe,Ceip.exe,CitrixReceiverUpdater.exe,CitrixWorkspaceNotification.exe,
ConfigurationWizard.exe,PrefPanel.exe,SRProxy.exe,crashpad_handler.exe,CdfCollector.exe,
DiagnosticTool.exe,CWAFeatureFlagUpdater.exe,CemAutoEnrollHelper.exe,CleanUp.exe,NPSPrompt.exe,
SelfServiceUninstaller.exe
FSLogix
frxsvc.exe,fslogix.exe:,frxtray.exe,frxccds.exe,frxshell.exe
Create Network Location configuration for Azure Virtual Desktop:
Destination Location exception bypasses traffic sent to specific destinations as defined in the network location profile.
You can get the latest IP address from the Microsoft website in the JSON format. Refer
Adding Network Location
to learn more about how to extract the IP addresses from Microsoft using the Python script. After converting the .json file to a .csv file, you can configure the Network Location Object through
Policies
>
Network Location
.
Add Exceptions:
After you are ready with the custom Certificate Pinned Apps for Citrix DaaS, FSLogix, and Network Location configurations, proceed with adding exceptions in the selected steering configuration.
Add the custom certificate pinned applications in the certificate pinned exceptions. To add a Certificate Pinned Application, view
Certificate Pinned Exception
.
Add Destination Location exception to add exceptions for Azure Virtual Desktop network locations. To learn more, view
Destination Location Exception
.
Netskope Client Deployment Procedure
After completing the prerequisites, perform the following to set up Netskope Client in your Citrix Workspace:
Log into your Citrix Workspace console.
Launch your remote desktop in Citrix Workspace.
Install Netskope Client on your remote desktop using any method provided in the
deployment methods
or using the MSIEXEC commands.
Once the Netskope Client is installed, the provisioned user can see that the Netskope Client is  enabled and managed applications are steered through the Netskope tunnel. The bypassed application traffic is directed to the internet.
In this Topic
Deploy Netskope Client On Citrix DaaS With Azure Virtual Desktop

---
## Deploy Client on macOS Using Omnissa Workspace ONE
**URL:** https://docs.netskope.com/en/deploy-client-on-macos-using-omnissa-workspace-one/
**Last Modified:** 2026-04-02T12:24:59+00:00
**Scraped:** 2026-06-26T09:37:47.126669+00:00

Deploy Client on macOS Using Omnissa Workspace ONE - Netskope Knowledge Portal
Deploy Client on macOS Using Omnissa Workspace ONE
This article describes how to deploy Netskope Client on macOS devices using Omnissa Workspace ONE.
Prerequisites
Administrators must possess proficient working knowledge of Omnissa Workspace ONE UEM.
Administrators must review
Netskope Client Client Enrollment Methods
to understand the Client User Enrollment methods available for their environment.
Import users into the Netskope tenant – see
Provisioning Users for Netskope Client
.
Download
Netskope Root and Tenant Certificates
and ensure the certificates are available when needed.
See
Deploy Netskope Client via IdP
when using IDP as the method of user enrollment.
Supported Platforms and Enrollment Methods
This article outlines the Netskope Client deployment instructions for the following user enrollment methods and supported platforms. User enrollment methods not documented here are not supported at this time.
Enrollment Method
Single User
Multi-User
IDP
Y
Y
PLIST
Y
N
Configuration Profile Setup
Profiles manage the core configuration for Client installation. The following sections provide a detailed overview of how to configure these profiles effectively.
Note: The following can be added to a New or Existing Profile as it aligns with your environment.
Pre-Approve Network Extension
The Netskope Client installs a network extension on macOS that requires administrator approval to function. Configure the following to pre-approve the network extension and suppress end-user notifications requesting approval.
To configure:
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple macOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
System
in the search text box of the configuration profile.
Expand
System Extensions
and click
Add
.
Configure Allow Systems Extensions as follows:
Bundle Identifier:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Team Identifier:
24W52P9M7W
Click
Next
.
If the
Next
button is not available, remove empty configuration options from other headers. For example, Removable system extensions, Non Removable System extensions.
Add the assignment details.
Click
Save & Publish
.
Approve Full Disk Access Permission
The Netskope Client on macOS requires Full Disk Access permissions for various foundational functionalities. The following configuration approves these permissions and suppresses end-user notifications requesting approval.
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple macOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
Privacy
in the search text box of the configuration profile.
Expand
Privacy Preferences
and click
Add
.
Configure the following settings to allow access to a service or an app:
Bundle Identifier:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Team Identifier:
Select
Bundle ID
.
Code Requirement:
anchor apple generic and identifier "com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
Find
System Policy All Files
under
Services
section and select
Allow
.
Click
Next
.
Add the assignment details.
Click
Save & Publish
.
For Endpoint DLP, you can add the following Identifier and Code Requirement:
– Identifier: com.netskope.epdlp.client
– Code Requirement:
anchor apple generic and identifier "com.netskope.epdlp.client" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
To learn more:
Enabling Endpoint DLP on the Netskope Client for macOS
.
Pre-Approve VPN Popup for App Proxy
The Netskope Client installs a network extension on macOS that triggers updates to the device’s Network settings. The following configuration pre-approves these updates and suppresses end-user notifications requesting approval.
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple macOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
VPN
in the search text box of the configuration profile.
Expand
VPN
and click
Add
.
Configure the following settings to allow access to a service or an app:
Connection Name:
Enter a descriptive name for the Connection Name.
Connection Type:
Select Custom SSL.
Identifier:
com.netskope.client.Netskope-Client
Server:
Enter your VPN server name from the Netskope UI. For example, gateway-<tenant-URL>.
Click
Next
.
Add the assignment details.
Click
Save & Publish
.
Prevent Disabling of System Extensions in macOS 15 (Sequoia)
Netskope recommends adding two optional deployment parameters,
Prevent Disabling of System Extensions
and
Restrict App Proxy Removal
, to manage user permissions regarding System Extensions in macOS 15 (Sequoia) and above. These controls prevent the user from removing the specified system extension.
To configure:
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple macOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
System
in the search text box of the configuration profile.
Expand
System Extensions
and click
Add
.
Configure
Allow Systems Extensions
as follows:
Bundle Identifier:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Team Identifier:
24W52P9M7W
Configure
Non Removable From UI System Extensions
as follows:
Bundle Identifier:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Team Identifier:
24W52P9M7W
Click
Next
.
Add the assignment details.
Click
Save & Publish
.
Restrict App Proxy Removal
Netskope recommends adding two optional deployment parameters
Prevent Disabling of System Extensions
and
Restrict App Proxy Removal
to manage user permissions regarding System Extensions in macOS 15 (Sequoia) and above. These controls prevent the removal of the specified system extension by the user.
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple macOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
Restrictions
in the search text box of the configuration profile.
Expand
Restrictions
and click
Add
.
Toggle Restrict System Preferences to enabled under Preferences
Select
DISABLE SELECTED ITEMS
Find Network and select checkbox
Click
Next
.
Add the assignment details.
Click
Save & Publish
.
Push Netskope Root and Tenant Certificates
Provide additional trust to end users by pushing certificates during client installation. Before you can push the root and tenant certificates, ensure that you do the following:
Download root and tenant certificates from Netskope MDM distribution page.
Login to Netskope tenant admin console with admin credentials.
Go to
Settings
>
Security Cloud Platform
>
MDM Distribution
. The certificate download options are displayed in the Certificate Setup section.
Convert the downloaded certificates to
.cer
format by renaming the .pem files to .cer.
Perform the following steps to add certificates to Omnissa Workspace ONE:
Go to
Resources
>
Profiles & Baselines
>
Profiles
.
Click
Add Profile
from the
Add
dropdown options.
Select
Apple macOS
from the platform list.
Select
Device Profile
in
Select Context
and click
Next
.
Enter a unique
Profile
name. For example, Netskope Client Configuration Profile.
Start typing
Credentials
in the search text box of the configuration profile.
Expand
Credentials
and click
Add
.
Enter the following details:
Credential Source: Select
Upload
.
Credential Name: It auto-populates the name after uploading the certificate.
Certificate: Click
Choose File
> Browse for the rootcaCert.cer file you downloaded from the Netskope tenant.
Click
Attach Certificate
.
Once you click
Attach Certificate
, the webUI displays the uploaded certificate details such as validity, thumbprint, and so on.
Click
+Add
to add another certificate.
Click
Choose File
>
Browse
for the
caCert.cer file you downloaded from the Netskope tenant.
Click
Attach Certificate
.
The webUI now displays two Credentials tabs in your Credentials payload.
Click
Next
.
Add the assignment details.
Click
Save & Publish
.
Deploy Email from Workspace ONE User Profile to Device
For a PLIST user enrollment, you must deploy the Plist file to the endpoint in advance. This file must contain the user’s email attribute that must be sourced from an email variable within the Workspace Sensor.
Perform the following steps to add the Plist file:
Use this section only if you are using PLIST mode for user enrollment.
Log into your Workspace One admin console.
Go to
Resources
>
Sensors
.
Click
Add
>
macOS
.
On the
New Sensor
window, provide
Name
and
Description
in the
General
section.
Click
Next
.
In the
Details
section, select the following:
Language: Bash
Execution Context: System
Response Data Type: String
Code:
#!/bin/bash
emailPrefFile="/Library/Managed Preferences/com.netskope.plist"
if [ -f "$emailPrefFile" ];
then
    echo "exists"
    echo "plist exists" > /tmp/plist.txt
else
    /usr/libexec/PlistBuddy -c "add email string $userMail" com.netskope.plist
    cp com.netskope.plist /Library/Managed\ Preferences/
echo "added"
fi
In the
Variables
section, create a variable to be used in the script during execution. Add
userMail
and select
{EmailAddress}
in the
Key
and
Value
fields respectively. You can add other variable names. However, ensure to add the same variable name as provided in the ‘bash’ script.
Click
Save
.
Once deployed, the administrator sees the file: com.netskope.plist under directory: /Library/ManagedPreferences/ on the macOS device. This file must contain the user’s email address. If the email address is not in the Plist file, then review the WorkspaceOne console to ensure you assign an email address to the user. To learn more, view
Collect Data with Sensors in macOS
and seek assistance from Omnissa Workspace One support when required.
Deploy Netskope Pre-install Script and Client Package
The administrator can add the Netskope Client script and packages along with the instructions to run the script on the device. To learn more, view
Deploy Internal macOS Applications
.
Go to
Resources > Apps > Native > Interna
l.
Select
Add > Add Application
.
In
Add Applicatio
n, click
Upload
to add the
Netskope package
file.
Click
Save
.
Click
Continue
.
Select Full Storage Management in Deployment Type
Upload the meta data file (.plist). To create a metadata file, download and install
Omnissa Workspace ONE UEM Admin Assistant Tool
to your macOS computer. To learn more, view
Generate Metadata
.
Click
Continue
.
This navigates to
Add Application
.
Under
Details,
you can review the details and make modifications, if necessary.
Click
Scripts
.
Under
Install Scripts
,add
Pre-Install Script
that runs before the installation process. Choose one of the following scripts according to your requirements:
PLIST
IDP
If you are using PLIST mode for enrollment, add the following script in the Pre-Install Script field.
#!/bin/bash
####
# ws1_netskope_pre-install.sh
# WorkspaceOne Pre-install script used to prepare macOS devices for the Netskope client. This script has support for secure enrollment.
# You will need to set the following parameters:
#
# TENANT - This should be to addon-YOUR TENANT.goskope.com
# ORGID - You can obtain your Organization ID from your tenant (Settings > Security Cloud Platform > MDM Distrubtion)
# EMAIL - This value will be fetched from com.netskope.plist file which will be created by ws1_netskope_sensor.sh script
# enrollencryptiontoken - encryption token on Secure Enrollment page if enabled &amp; enforced
# enrollauthtoken - authentication token on Secure Enrollment page if enabled &amp; enforced
#
##
TENANT=addon-&lt;tenant>
ORGID=&lt;org_key>
EMAIL=`defaults read /Library/Managed\ Preferences/com.netskope.plist email`
enrollauthtoken=&lt;auth_token>
enrollencryptiontoken=&lt;encryption_token>
TEMP_BRANDING_DIR="/tmp/nsbranding"
TEMP_ENROLLMENT_TOKEN_FILE="$TEMP_BRANDING_DIR/enroll.conf"
if [ ! -d $TEMP_BRANDING_DIR ]; then
 mkdir -p $TEMP_BRANDING_DIR
fi
NSINSTPARAM_JSON_FILE="${TEMP_BRANDING_DIR}/nsinstparams.json"
echo "{\"TenantHostName\": \"$TENANT\", \"Email\": \"$EMAIL\", \"OrgKey\": \"$ORGID\"}" > "${NSINSTPARAM_JSON_FILE}"
Create_Json() {
    if [[ -f "$TEMP_ENROLLMENT_TOKEN_FILE" ]]; then
        rm "$TEMP_ENROLLMENT_TOKEN_FILE"
    fi  
    local a=$1
    local b=$2
    if ! [[ "$a" =~ ^[a-fA-F0-9]{32}$ ]] &amp;&amp; [[ "$a" != "0" ]]; then
        echo "Invalid auth token: must be 32 hexadecimal characters"
        return 1
    fi  
    if ! [[ "$b" =~ ^[a-fA-F0-9]{32}$ ]] &amp;&amp; [[ "$b" != "0" ]]; then
        echo "Invalid encryption token: must be 32 hexadecimal characters"
        return 1
    fi  
    echo "{" > $TEMP_ENROLLMENT_TOKEN_FILE
    if [[ "$a" != "0" &amp;&amp; "$b" != "0" ]]; then
        echo "\"enrollauthtoken\": \"$a\"," >> $TEMP_ENROLLMENT_TOKEN_FILE
        echo "\"enrollencryptiontoken\": \"$b\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    elif [[ "$a" == "0" &amp;&amp; "$b" != "0" ]]; then
        echo "\"enrollencryptiontoken\": \"$b\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    elif [[ "$b" == "0" &amp;&amp; "$a" != "0" ]]; then
          echo "\"enrollauthtoken\": \"$a\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    else
         echo "Unsupported use case"
    fi  
    echo "}" >> $TEMP_ENROLLMENT_TOKEN_FILE
    chmod 700 "$TEMP_ENROLLMENT_TOKEN_FILE"
    echo "enroll.conf created with provided tokens."
}
if [[ "$enrollencryptiontoken" != "0" || "$enrollauthtoken" != "0" ]]; then
    echo "Using secure enrollment"
    Create_Json "$enrollauthtoken" "$enrollencryptiontoken"
else
    echo "Not using secure enrollment"
    if [[ -f "$TEMP_ENROLLMENT_TOKEN_FILE" ]]; then
        rm "$TEMP_ENROLLMENT_TOKEN_FILE"
    fi
fi
– Replace  lines 19, 20, 24, and 25 with values from your tenant. Refer to
Client Deployment Parameters
to learn more about where to find these values in the Netskope Admin Console.
– Ensure not to add any space while adding values.
– If no secure enrollment token is enabled, add 0 as the token value. For example, if encryption token is not enabled in your tenant, then add enrollencryptiontoken=0
If you are using IDP enrollment method for single-user mode, add the following script in the Pre-Install Script field:
#!/bin/bash
set -euo pipefail
# Workspace ONE Pre-install script for IDP mode to prepare macOS devices for the Netskope client.
# Supports Secure Enrollment. Requires DOMAIN, TENANT_NAME, and optionally enroll tokens.
# ===== USER CONFIGURATION =====
DOMAIN="&lt;tenant domain>"        # e.g., eu.goskope.com
TENANT_NAME="&lt;tenant_name>"     # e.g., nsclient
REQ_EMAIL=true                  # true or false
perusermode=0		            # 1 for enabling per-user mode
enrollauthtoken=0		     # Always 0 in IDP mode
enrollencryptiontoken=0        # 32-character hex or 0 if secure enrollment not enabled
# ==============================
# Validate required inputs
if[["$DOMAIN"=="&lt;tenant_domain>"||"$TENANT_NAME"="&lt;tenant_name>"];then
echo "[ERROR] Please configure DOMAIN and TENANT_NAME before running this script."
exit 1
fi
# Paths
TEMP_BRANDING_DIR="/tmp/nsbranding"
TEMP_ENROLLMENT_TOKEN_FILE="$TEMP_BRANDING_DIR/enroll.conf"
IDPCONFIG_JSON_DIR="/Library/ApplicationSupport/Netskope/STAgent"
IDPCONFIG_JSON_FILE="$IDPCONFIG_JSON_DIR/nsidpconfig.json"
NSUSERCONFIG_JSON_FILE="$IDPCONFIG_JSON_DIR/nsuserconfig.json"
# Create required directories
mkdir -p "$TEMP_BRANDING_DIR"
mkdir -p "$IDPCONFIG_JSON_DIR"
echo "[INFO] Writing IDP config to $IDPCONFIG_JSON_FILE"
cat &lt;&lt;EOF> "$IDPCONFIG_JSON_FILE"
{
 "serviceProvider": {
   "domain": "$DOMAIN",
   "tenant": "$TENANT_NAME"
 },
 "requestEmail": "$REQ_EMAIL"
}
EOF
# Handle per-user mode if enabled
if[["$perusermode"-eq1]];then
echo " [INFO] Per-user mode enabled, writing $NSUSERCONFIG_JSON_FILE"
cat &lt;&lt;EOF>"$NSUSERCONFIG_JSON_FILE"
{
 "nsUserConfig": {
   "enablePerUserConfig": "true",
   "configLocation": "~/Library/Application Support/Netskope/STAgent",
   "token": "",
   "host": "",
   "autoupdate": "true"
 }
}
EOF
fi
# Function: Create enrollment token file
Create_Json(){
local auth_token="$1"
localencryption_token="$2"  
# Remove old file
rm -f "$TEMP_ENROLLMENT_TOKEN_FILE"
# Validate tokens
if![["$auth_token"==~ ^[a-fA-F0-9]{32}$]]&amp;&amp;[["$auth_token"!="0"]
];then
echo"[ERROR] Invalid auth token: must be 32 hexadecimal characters or 0"
return 1
fi
if![["$encryption_token"=~ ^[a-fA-F0-9]{32}$]]&amp;&amp;[["$encryption_token"!="0"]];then
echo "[ERROR] Invalid encryption token: must be 32 hexadecimal characters or 0"
return 1
fi
echo
"[INFO] Creating secure enrollment config at
$TEMP_ENROLLMENT_TOKEN_FILE"
{
echo"{"
[["$auth_token"!="0"]]&amp;&amp;echo" \"enrollauthtoken\":\"$auth_token\","
[["$encryption_token"!="0"]]&amp;&amp;echo" \"enrollencryptiontoken\":\"$encryption_token\""
echo"}"
} > "$TEMP_ENROLLMENT_TOKEN_FILE"
chmod 700 "$TEMP_ENROLLMENT_TOKEN_FILE"
echo "[INFO] enroll.conf created successfully"
}
# Secure Enrollment Block
if [["$enrollencryptiontoken"!="0"||"$enrollauthtoken"!="0"]];then
echo "[INFO] Using secure enrollment"
Create_Json "$enrollauthtoken" "$enrollencryptiontoken"
else
echo "[INFO] Not using secure enrollment"
rm -f "$TEMP_ENROLLMENT_TOKEN_FILE"
fi
– Replace  line 7, 8, 9, 10, 11, and 12 with values from your tenant. Refer to
Client Deployment Parameters
to learn more about where to find these values in the Netskope Admin Console.
– If the value given for REQ_EMAIL in “requestEmail”: “$REQ_EMAIL” is true, the SAML IDP URL where you need to enter the email address and navigate you to the OKTA login page. If the REQ_EMAIL value is false, then it directly navigates you to the OKTA login page.
Click
Save & Assign
.
Once you add an application to the console, start assigning devices to the application.
Click the application that you added.
Click the
Assignment
tab.
Click
Assign
available on the right corner of the screen.
Under
Assignments
, click
Add Assignment
.
On the
Assignment
screen, perform the following:
Provide a
Name
for the assignment.
In
Assignment Groups
, select the desired group
Click
Create
.
Click
Save
.
Verifying Client Installation
Check the installation logs on the user’s machine in the /var/log/install.log folder. If the user configuration download script fails and the Netskope client installer is executed, the installer will exit and display the
Configuration file missing, aborting installation!
error message.
Check Netskope Client Installation Status
To verify the status of each device, go to
Computer
>
Policies
and click on the policy you created.
Click the
Logs
button at the bottom to view the log files for each device and then click the
Show
button.
Confirming the Netskope Client Extension Approval
To confirm that the Netskope Client extension has been approved and the client is running, run the following command in your macOS terminal window:
systemextensionsctl list
The output should look like this:
% systemextensionsctl list  
1 extension(s)
--- com.apple.system_extension.network_extension
enabled active teamID bundleID (version) name [state]
* * 24W52P9M7W com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy (85.2.0.269/1) 
NetskopeClientMacAppProxy [activated enabled]
Additionally, inspect the system preferences and Network UI to confirm that Netskope Client extension is active.
Uninstalling the Netskope Client
See
Uninstalling the Netskope Client
for instructions on uninstalling the Netskope Client.
In this Topic
Deploy Client on macOS Using Omnissa Workspace ONE

---
## Deploy Client on macOS Using Kandji
**URL:** https://docs.netskope.com/en/deploy-client-on-macos-using-kandji/
**Last Modified:** 2026-05-27T13:29:50+00:00
**Scraped:** 2026-06-26T09:37:48.289364+00:00

Deploy Client on macOS Using Kandji - Netskope Knowledge Portal
Deploy Client on macOS Using Kandji
This article illustrates the procedure to deploy Netskope Client on macOS devices running Big Sur or later  using the Kandji MDM as the IdP. This process ensures reduced user interaction while deploying tenant certificates, system and network extensions.
Deployment Prerequisites
Download Netskope’s Root and Intermediate Certificates.
Download
VPN Proxy App script
from the Netskope Support Portal. This is required for macOS devices running Big Sur or later.
Administrator access to Kandji.
Administrator access to Netskope.
IdP setup with Netskope (for IdP-initiated enrollments).
IdP user integration setup with Kandji (for Kandji user-assigned enrollment).
Configure SAML authentication between
Netskope and your IDP
.
Before You Begin
Before you begin deployment, perform the following steps to upload the required certificates and configuration files in Kandji to successfully install and activate Client:
Download Netskope Certificates
Upload Netskope Certificates to Kandji.
Upload VPN Configuration to Kandji.
Add System Extension Profile.
Prevent disabling Netskope background items.
Allow Privacy Settings in Kandji
Download Netskope Certificates
Login to Netskope WebUI with admin access and go to
Settings
>
Manage
>
Certificates
.
Click the
Signing CA
tab and download both Netskope Root and Netskope Intermediate certificates.
Convert the downloaded certificates to
.cer
format by renaming the .pem files to .cer.
Upload Netskope Certificates to Kandji
To upload the certificates to Kandji:
Important
It is mandatory to upload the Netskope Root Certificate and Netskope Intermediate Certificate.
Login to Kandji and go to
Library
>
Add New
.
Select
Profiles
from the dropdown menu.
Click
Certificate
>
Add and Configure
Upload Netskope Root Certificate (
.cer
format).
Enter a name for this certificate, for example:
Netskope Root Certificate
Select
Certificate Type
as
PKCS#1-formatted certificate
.
Drag and drop the .cer certificate in the upload box.
Repeat this step to upload the Netskope Tenant Certificate. When uploading, give a name, for example:
Netskope Tenant Certificate
.
Upload VPN Configuration to Kandji
Go to
Library
>
Add New
> Custom Profile.
Click
Add and Configure
.
Provide a name.
Download the
AppVPN proxy script
from Netskope Support.
Extract the zip file and upload the
.mobileconfig
file.
Add System Extension Profile
Go to
Library
, select
Profiles
from the dropdown menu.
Select
System Extension
and click
Add and Configure
.
Specify the following for System Extension
Under General, select the checkbox to enable
Allow Users to approve system extension
s
.
Team Identifier :
24W52P9M7W
Name (optional): Netskope
Under System Extension, select
Allow all system extensions
from the dropdown menu.
Prevent Disabling Netskope Startup and Background Items
Go to
Library
>
Add New
(you can also add Netskope settings to a pre-existing Login &Background item).
Select
Profiles
from the drop-down >
Login & Background Items
>
Add & Configur
e.
Specify the following for Login and Background Items:
Provide a name. For example, Login & Background Items.
Click
Add Background Item
and enter details for the following:
Identifier Type: Team Identifier
Identifier: 24W52P9M7W
Comment: Netskope Client
Click
Save
.
Allow Privacy Settings in Kandji
Go to
Library
>
Add New
(you can also add Netskope settings to a pre-existing
Privacy
library item).
Select
Profiles
from the drop-down >
Privacy
>
Add & Configure
Under
APP ACCESS
, create the following:
Privacy setting #1
Identifier Type:
Bundle ID
Identifier:
com.netskope.client.Netskope-Client
Code Requirement:
anchor apple generic and identifier "com.netskope.client.Netskope-Client" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
App or Service:
Allow
Accessibility
and
SystemPolicyAllFiles
.
Privacy setting #
2
Identifier Type:
Bundle ID
Identifier:
com.netskope.epdlp.client
Code Requirement
:
anchor apple generic and identifier "com.netskope.epdlp.client" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
App or Service:
Allow
SystemPolicyAllFiles
To learn more:
Enabling Endpoint DLP
on
the Netskope Client for macOS
.
Privacy setting #3
Identifier Type:
Bundle ID
Identifier:
com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy
Code Requirement:
anchor apple generic and identifier "com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "24W52P9M7W")
App or Service:
Allow
SystemPolicyAllFiles
Deployment Procedure
After you complete adding the required certificates and files, you are ready to start with the deployment scripts using the pre-built scripts using the instructions provided in this section.
Kandji supports the following types of deployment methods:
IdP deployment in Single-User Mode.
IdP deployment in Multi-User Mode.
Deployment by the user assigned in Kandji.
Netskope provides documentation for three deployment methods. Choose the best method for your organization and follow the instructions in that section. If neither of these deployment methods are applicable to your organization, contact Netskope for additional assistance.
Option 1: Using IdP
Supports single and multi-user device enrollments.
Requires existing setup of the
SAML Forward Proxy
in your Netskope tenant to enable client enrollment.
Supports multi-factor authentication(MFA).
Option 2: Using Kandji Assigned User
Installs Netskope Client silently without end-user interaction.
Supports single-user mode enrollments.
The admin need to source Kandji users from IdP. To learn more, view
Kandji
documentation.
Assign each device to the users planned for enrollment.
Supports automated user assignment via IdP authentication during zero-touch deployments.
Add Deployment Scripts in Kandji
After you complete the steps to upload the required certificates and files, you can start adding the deployment scripts in Kandji. You can use the Netskope pre-built deployment scripts.
Deployment scripts are a combination of audit and remediation scripts that are required to deploy Netskope Client to the end user devices.
The audit script checks if Netskope Client is installed on the end-user devices.
The remediation script installs the clients on end-user devices that do not have the client installed.
The audit scripts are the same for each deployment method. You can start by creating the Kandji Library item and adding the audit script.
Go to
Library
>
Add New
.
Select
Custom Script
and click
Add &Configure
.
Create custom script with the following parameters:
Name: Enter any name. For example, Netskope Client Install.
Execution Frequency : Set this to value that suits your environment. Netskope recommends setting this value to Daily or 15 minutes.
Enter the following script in the
Audit Script
text box:
#!/bin/bash
#script for installing NSAgent on OSX machines
#will check to see if Netskope is Installed
function Test_NSClient(){
xz=$(/usr/bin/mdfind kMDItemFSName == Netskope Client.app -onlyin /Library/Application\ Support/)
 if [ -e "$xz" ]; then
     echo "$xz found netskope client is installed"
 exit 0
 else
     echo "client does not exist"
 exit 1
 fi
}
Test_NSClient
#end script
Click
+Add Remediation script
and add the following script:
The remediation script varies according to your choice of the enrollment method.
Remediation Script for IdP enrollment
Replace the values marked XXXXX with your tenant domain name and YYYYY with the tenant name.
spDomain= <tenant-domain>
Example: skope.com.
spTenant = <tenant-name>
Example: If your tenant URL is example.skope.com, then enter only
example
.
If you prefer normal installation with single-user mode no other changes are needed.
If you prefer to install in multi-user mode, change “perusermode=0” to  “perusermode=1”
If Secure Enrollment is enabled, replace the authentication and encryption enrollment tokens with the tokens generated on the tenant webUI:
enrollencryptiontoken
=<encryption token>
enrollauthtoken
=<authentication token>
If secure enrollment is not enabled, the following values are displayed in the script:
enrollencryptiontoken
=0
enrollauthtoken
=0
#!/bin/bash
#Script for installing Netskope Client on OSX machines
#function will install Netskope Client
function Ins_NSClient(){
ag="NSClient.pkg"
spDomain="XXXXX"
spTenant="YYYYY"
perusermode=0 # put 0 for normal installation, put 1 for per user config
# Initialize variables for the mandate failclose
enforceFailClose=0 # put 1 for enabling enforce enrollemnt 
steeringProfileID_val=""
frequency_val="5" # Set default value
host_val=""   #addon url
token_val=""  #org id
# end for mandate failclose variables
echo "Downloading NsAgent..."
curl -o /tmp/$ag  https://download.goskope.com/dlr/mac/get
echo "will now add config file..."
mkdir -p "/Library/Application Support/Netskope/STAgent"
NSIDPCONFIG_FILE_PATH="/Library/Application Support/Netskope/STAgent/nsidpconfig.json"
NSUSERCONFIG_JSON_FILE="/Library/Application Support/Netskope/STAgent/nsuserconfig.json"
echo "{ \"serviceProvider\": { \"domain\": \"$spDomain\", \"tenant\": \"$spTenant\" } }" > "${NSIDPCONFIG_FILE_PATH}"
# Determine the string value for enablePerUserConfig based on the perusermode flag.
    per_user_enabled="false"
    if [ $perusermode -eq 1 ]; then
        per_user_enabled="true"
    fi
   if [[ $perusermode -eq 1 || $enforceFailClose -eq 1 ]]; then
        json_config="{\"nsUserConfig\":{\"enablePerUserConfig\": ${per_user_enabled}, \"configLocation\": \"~/Library/Application Support/Netskope/STAgent\""
        mkdir -p "/Library/Application Support/Netskope/STAgent"
        # Conditionally add host and token directly under nsUserConfig
        json_config="$json_config, \"host\": \"$host_val\""
        json_config="$json_config, \"token\": \"$token_val\""
        if [ $enforceFailClose -eq 1 ]; then
            echo "Enforce fail close option is provided"
            json_config="$json_config, \"enforceEnrollment\": {"
            json_config="$json_config \"steeringProfileID\": \"$steeringProfileID_val\""
            json_config="$json_config, \"frequency\": \"$frequency_val\""
            json_config="$json_config }" # Close the nested object
        fi
        # Add the remaining static parts and close the main JSON object
        json_config="$json_config, \"autoupdate\": \"true\"$fail_close_option}}"
        # Write the final, valid JSON to the file
        echo "$json_config" > "${NSUSERCONFIG_JSON_FILE}"
    fi
echo "Installing Agent..."
installer -dumplog -pkg /tmp/$ag -target / && rm /tmp/$ag
}
# Function to create JSON file with provided tokens
Create_Json() {
    # Create directory if it doesn't exist
    mkdir -p $TEMP_BRANDING_DIR
    # Delete previous enroll.conf if it exists
    if [[ -f "$TEMP_ENROLLMENT_TOKEN_FILE" ]]; then
        rm "$TEMP_ENROLLMENT_TOKEN_FILE"
    fi 
    local a=$1 #auth token
    local b=$2 #encryption token
    # Check if parameters are 32 characters hexadecimal
    if ! [[ "$a" =~ ^[a-fA-F0-9]{32}$ ]] && [[ "$a" != "0" ]]; then
        echo "Invalid auth token: must be 32 hexadecimal characters"
        return 1
    fi
    if ! [[ "$b" =~ ^[a-fA-F0-9]{32}$ ]] && [[ "$b" != "0" ]]; then
        echo "Invalid encryption token: must be 32 hexadecimal characters"
        return 1
    fi
    # Start the JSON structure
    echo "{" > $TEMP_ENROLLMENT_TOKEN_FILE
    #if both token is present
    if [[ "$a" != "0" && "$b" != "0" ]]; then
        echo "\"enrollauthtoken\": \"$a\"," >> $TEMP_ENROLLMENT_TOKEN_FILE
        echo "\"enrollencryptiontoken\": \"$b\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    # only encryption token present
    elif [[ "$a" == "0" && "$b" != "0" ]]; then
        echo "\"enrollencryptiontoken\": \"$b\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    #only authtoken present
    elif [[ "$b" == "0" && "$a" != "0" ]]; then
          echo "\"enrollauthtoken\": \"$a\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    else
         echo "Unsupported use case"
    fi
    # End the JSON structure
    echo "}" >> $TEMP_ENROLLMENT_TOKEN_FILE
    chmod 700 "$TEMP_ENROLLMENT_TOKEN_FILE"
    echo "enroll.conf created with provided tokens."
}
# Main script execution
#update these tokens to valid tokens
enrollencryptiontoken=0
enrollauthtoken=0
TEMP_BRANDING_DIR="/tmp/nsbranding"
TEMP_ENROLLMENT_TOKEN_FILE="$TEMP_BRANDING_DIR/enroll.conf"
# Check if atleast one of the token is present, then create enroll.conf
if [[ "$enrollencryptiontoken" != "0" || "$enrollauthtoken" != "0" ]]; then
    echo "Using secure enrollment"
    Create_Json "$enrollauthtoken" "$enrollencryptiontoken"
else
    echo "Not using secure enrollment"
    # Delete previous enroll.conf if it exists
    if [[ -f "$TEMP_ENROLLMENT_TOKEN_FILE" ]]; then
        rm "$TEMP_ENROLLMENT_TOKEN_FILE"
    fi
fi
Ins_NSClient
#end script
Remediation script for Kandji assigned user
If Secure Enrollment is enabled, replace the authentication and encryption enrollment tokens with the tokens generated on the tenant webUI:
enrollencryptiontoken
=<encryption token>
enrollauthtoken
=<authentication token>
If secure enrollment is not enabled, the following values are displayed in the script:
enrollencryptiontoken
=0
enrollauthtoken
=0
Replace the values marked XXXXX with your tenantUrl and YYYYY with your Organization ID.
tenantUrl= addon-<tenant url>
Example: If your tenant URL is example.skope.com, then it would be addon-example.skope.com
orgKey = <Organization ID>
This is found in your Netskope tenant at this location: Settings > Security Cloud Platform > MDM Distribution > Deployment Resources for iOS > Create VPN Configuration > Organization ID: YYYYY
#!/bin/bash
#Script for installing Netskope Client on OSX machines by the Kandji assigned user
#function will install Netskope Client
function Ins_NSClient(){
ag="NSClient.pkg"
tenantUrl="addon-XXXXX"                                                                                                                                                                                                                              
emailAddress="$(/usr/libexec/PlistBuddy -c 'print :EMAIL' /Library/Managed\ Preferences/io.kandji.globalvariables.plist)"
orgKey="YYYYY"
echo "will now add config file..."
mkdir -p "/tmp/nsbranding"
NSINSTPARAM_JSON_FILE="/tmp/nsbranding/nsinstparams.json"
echo "{\"TenantHostName\":\"$tenantUrl\", \"Email\":\"$emailAddress\", \"OrgKey\":\"$orgKey\"}" > "${NSINSTPARAM_JSON_FILE}"
echo "Downloading NsAgent..."
curl -o /tmp/$ag  https://download.goskope.com/dlr/mac/get
echo "Installing Agent..."
installer -dumplog -pkg /tmp/$ag -target / && rm /tmp/$ag
echo "Cleaning up..."
}
# Function to create JSON file with provided tokens
Create_Json() {
    # Create directory if it doesn't exist
    mkdir -p $TEMP_BRANDING_DIR
    # Delete previous enroll.conf if it exists
    if [[ -f "$TEMP_ENROLLMENT_TOKEN_FILE" ]]; then
        rm "$TEMP_ENROLLMENT_TOKEN_FILE"
    fi  
    local a=$1 #auth token
    local b=$2 #encryption token
    # Check if parameters are 32 characters hexadecimal
    if ! [[ "$a" =~ ^[a-fA-F0-9]{32}$ ]] && [[ "$a" != "0" ]]; then
        echo "Invalid auth token: must be 32 hexadecimal characters"
        return 1
    fi  
    if ! [[ "$b" =~ ^[a-fA-F0-9]{32}$ ]] && [[ "$b" != "0" ]]; then
        echo "Invalid encryption token: must be 32 hexadecimal characters"
        return 1
    fi  
    # Start the JSON structure
    echo "{" > $TEMP_ENROLLMENT_TOKEN_FILE
    #if both token is present
    if [[ "$a" != "0" && "$b" != "0" ]]; then
        echo "\"enrollauthtoken\": \"$a\"," >> $TEMP_ENROLLMENT_TOKEN_FILE
        echo "\"enrollencryptiontoken\": \"$b\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    # only encryption token present
    elif [[ "$a" == "0" && "$b" != "0" ]]; then
        echo "\"enrollencryptiontoken\": \"$b\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    #only authtoken present
    elif [[ "$b" == "0" && "$a" != "0" ]]; then
          echo "\"enrollauthtoken\": \"$a\"" >> $TEMP_ENROLLMENT_TOKEN_FILE
    else
         echo "Unsupported use case"
    fi  
    # End the JSON structure
    echo "}" >> $TEMP_ENROLLMENT_TOKEN_FILE
    chmod 700 "$TEMP_ENROLLMENT_TOKEN_FILE"
    echo "enroll.conf created with provided tokens."
}
# Main script execution
#update these tokens to valid tokens
enrollencryptiontoken=0
enrollauthtoken=0
TEMP_BRANDING_DIR="/tmp/nsbranding"
TEMP_ENROLLMENT_TOKEN_FILE="$TEMP_BRANDING_DIR/enroll.conf"
# Check if atleast one of the token is present, then create enroll.conf
if [[ "$enrollencryptiontoken" != "0" || "$enrollauthtoken" != "0" ]]; then
    echo "Using secure enrollment"
    Create_Json "$enrollauthtoken" "$enrollencryptiontoken"
else
    echo "Not using secure enrollment"
    # Delete previous enroll.conf if it exists
    if [[ -f "$TEMP_ENROLLMENT_TOKEN_FILE" ]]; then
        rm "$TEMP_ENROLLMENT_TOKEN_FILE"
    fi
fi
Ins_NSClient
#end script
Click
Save
.
Add Custom Profile for Kandji Global Variables
Primarily, you need to deploy a .plist file to the local devices to run the remediation script. The script uses the .plist file during installation to identify the the user of any device.
Note
Download
Kandji-Global-Variables.mobileconfig
file from the
Support
portal.
To add a custom profile:
Go to
Library
>
Add New
.
Select
Profiles
from the drop-down >
Custom Profile
.
Click
Add & Configure
.
Enter a name for the profile. For example, Kandji Global Variables.
Upload the downloaded
Kandji-Global-Variables.mobileconfig
file.
Click
Save
.
Apply New Kandji Library items to your BlueprintKandji
Netskope recommends creating a test blueprint to ensure Netskope Client deploys as expected.
Navigate to your Blueprint.
Uncheck the box next to Show enabled only.
Toggle to enable the following items:
Netskope Root Certificate(Profiles / Certificates)
Netskope Tenant Certificate(Profiles / Certificates)
Netskope-AppProxyVPN (Custom Profile)
Netskope System Extension(System Extension)
Login & Background Item(Login & Background Items)
Install Netskope Client(Custom Scripts)
Kandji Global Variables(Custom Profile) ***** only needed if enrolling by
Kandji assigned Users
Click
Save
.
In this Topic
Deploy Client on macOS Using Kandji

---
## Netskope Client For Windows
**URL:** https://docs.netskope.com/en/netskope-client-for-windows/
**Last Modified:** 2026-06-09T04:08:46+00:00
**Scraped:** 2026-06-26T09:37:49.425405+00:00

Netskope Client For Windows
This document describes the available deployment methods and users enrollment options when users install Netskope Client on Windows devices.
Supported Operating Systems
Refer to
Netskope Client Supported OS and Platform
for more details on the supported Windows operating system  (OS) versions.
Download Client Packages
You can download Netskope Client installers from
Netskope Support Portal
.
Netskope Client MSIEXEC Parameters
Use Windows Installer (msiexec) to deploy Netskope Client on Windows devices.
Refer to the following table to view the parameters available to the Windows Installer. You can customize these parameters and adjust based on the installation requirements.
Parameter
Description
/I <package name>
Not required for some MDM configurations.
Required for command line installations through Windows Installer (msiexec). For more information, view
Microsoft MSIEXEC
.
tenant=<tenant-name>
Required only for deployments using IDP user enrollment. Do not use it when enrolling a user using UPN. For example,
If your tenant hostname is corp.goskope.com, use tenant=corp
If your tenant hostname is corp.eu.goskope.com, use tenant=corp
domain=[region.]<tenant-domain>
Required only for deployments using IDP user enrollment. Do not use it when enrolling a user using UPN. For example,
If your tenant hostname is corp.goskope.com, use domain=goskope.com
If your tenant hostname is corp.eu.goskope.com, use domain=eu.goskope.com
installmode=idp
Required only for deployment using IDP user enrollment. Do not use it when enrolling a user using UPN.
host=addon-<tenant-name>.[region.]<tenant-domain>
Required only for deployments using UPN user enrollment. Do not use it when enrolling users using IDP. This is the addon hostname of your tenant. For example,
If your tenant hostname is corp.goskope.com, use host=addon-corp.goskope.com
If your tenant hostname is corp.eu.goskope.com, use host=addon-corp.eu.goskope.com
token=<Organization ID>
Required only for deployments using UPN user enrollment. Do not use it when enrolling users using IDP. To find your organization ID:
Login to your Netskope Admin Console with admin credentials.
Go to
Settings
>
Security Cloud Platform
>
MDM Distribution
.
Locate your
Organization ID
under the
Create VPN Configuration
section. The organization ID is case-sensitive.
enrollauthtoken=<Authentication Token>
Required when enrolling users using UPN with
Secure Enrollment
Authentication Token that is enabled and enforced in the Netskope admin console.
Required when using
Private Access Prelogon
(UPN and IdP enrollment) with
Secure Enrollment
Authentication Token  that is enabled and enforced in the Netskope admin console.
Requires elevated admin privileges to register a token on the endpoint device.
enrollencryptiontoken=<Encryption Token>
Required when enrolling users using
UPN
or
IdP
with Secure Enrollment Encryption token enabled and enforced in the Netskope admin console.
Requires elevated admin privileges to register a token on the endpoint device.
mode=peruserconfig
(Optional Parameter)
Use when installing on a multi-user system. With this parameter set, each user needs to enroll Netskope Client independently. Without this parameter set, the Netskope Client can enroll one time for all users.
npavdimode=on
(Optional Parameter)
Use when installing on a multi-user Windows desktop with concurrent users logged on at the same time, such as some Citrix VDI and Azure Virtual Desktop Environments.
userconfiglocation=<path>
(Optional Parameter)
Overrides the default path for storing the user configuration. It is recommended to not use this parameter unless users' home directories are hosted on external file servers or network shares. In addition, this parameter is recommended to be used only for multi-user systems (when mode=peruserconfig is included in the parameters).
The default path:
%AppData%\Netskope\STAgent
Note: The custom path can be an absolute path, a network share, or a path utilizing environment variables. Environment variables need to be properly escaped depending on how the Windows installer (msiexec) command is run:
If running from a command prompt, append ^ before each %
Example:
>msiexec /I NSClient.msi mode=peruserconfig userconfiglocation=C:\Users\^%USERNAME^%\Netskope
If running from a batch script, append % before each %
Example:
>msiexec /I NSClient.msi mode=peruserconfig userconfiglocation=C:\Users\%%USERNAME%%\Netskope
If running from SCCM (or other mass deployment tool), append ^ before each % and prefix with cmd /c
Example:
>cmd /c msiexec /I NSClient.msi mode=peruserconfig userconfiglocation=C:\Users\^%USERNAME^%\Netskope
fail-close=disable|no-npa
(Optional Parameter)
This setting overrides the Fail Close settings in the Client Configuration.
disable: Explicitly disable fail-close on this device.
no-npa: Allow Private Access (NPA) traffic even if the Internet Security tunnel cannot be established and Fail Close is blocking Internet traffic.
For more details, view
Fail Close
.
prelogonuser=<prelogon username> @prelogon.netskope.com
(Optional Parameter)
Use when deploying Private Access Prelogon. For more information, view
Prelogon
.
autoupdate=on|off
(optional Parameter)
on: Default value which allows auto updating of Netskope Client based on the Client Configuration. If Client Configuration has auto update disabled then Netskope Client will not auto update on this system.
off: Disable auto updating of Netskope Client. This overrides the Client Configuration and prevents any Netskope Client auto updates on this system.
/l*v
(optional Parameter)
Sets the Windows Installer (msiexec) installation log file path. For Example:
/l*v %PUBLIC%nscinstall.log
/qn
(optional Parameter)
Use this option for silent installation.
enforceenrollsteeringprofileid
(Optional Parameter)
Copy and paste the Steering Profile ID from the Steering Configuration profile > Enforce Enrollment > Steering Profile ID.
enforceenrollfrequency
(Optional Parameter)
If the end-user closes the Netskope Client enrollment window, an enrollment reminder appears on the screen periodically. The frequency of the enrollment reminder is determined by this parameter. The unit is minutes and the allowed values are 1 - 1440 (24 hours). The default frequency is 5 minutes if this parameter is not set or if the value is outside the allowed range.
INSTTAG
(Optional Parameter)
Use when installing Client using Device Tags. These tags can be used as part of Steering configuration or Device Classification rules as a match parameters.
Add
Device Tags
configured in the Device webUI.
Note: This is a Beta feature. Contact Netskope Support team or your Sales Representative to enable this feature for your tenant.
Netskope Client Deployment Commands – Examples
The parameters used depend on the deployment mode, user enrollment method, features required, and environment. Use the table in the previous section and the following examples for more information.
– Always enter the command and parameters in a single line without any line-breaks.
– Some MDM deployments (for example, Microsoft Intune) only require the parameters and do not require the leading
msiexec /I NSClient.msi
part in the following examples. Refer to
Netskope Client deployment
section for more details.
– The Windows installer (msiexec)
/j
option is not supported for Netskope Client installation.
IDP
UPN
Prelogon Connectivity for Netskope Private Access
To learn more, view
Deploy Netskope Client Using IDP
.
Deployment Option
Command
All MSIEXEC IDP Options
msiexec /I NSClient.msi tenant=<tenant-name> domain=[region.]<tenant-domain> installmode=idp [enrollauthtoken=<Authentication Token>] [enrollencryptiontoken=<Encryption Token>] [mode=peruserconfig [npavdimode=on] [userconfiglocation=<path>]] [fail-close=no-npa|disable] [prelogonuser=<prelogon username>@prelogon.netskope.com] [autoupdate=on|off] [enforceenrollsteeringprofileid=<steering profile ID>] [enforceenrollfrequency=<time in minutes>] [INSTTAG=Tag 1, Tag 2] [/l*v %PUBLIC%nscinstall.log] [/qn]
Note: If you are using Enforce enrollment parameters: [enforceenrollsteeringprofileid] and [enforceenrollfrequency] , ensure to add the the following parameters:
host=addon-<tenant-name>.[region.]<tenant-domain>
token=<Organization ID>.
Single-User Mode Installation for IDP-based Enrollment
System-level enrollment based on the first user to enroll Netskope Client using IDP
msiexec /I NSClient.msi tenant=<tenant-name> domain=[region.]<tenant-domain> enrollencryptiontoken=<Encryption Token> /qn
Example 1:
msiexec /I NSClient.msi tenant=corp domain=goskope.com installmode=IDP enrollencryptiontoken=XXX /qn
Example 2:
msiexec /I NSClient.msi tenant=corp domain=eu.goskope.com installmode=IDP enrollencryptiontoken=XXX /qn
Multi-User Mode Installation for IDP-based Enrollment
Per-user enrollment; each user must enroll in the Netskope Client using IDP
msiexec /I NSClient.msi tenant=<tenant-name> domain=[region.]<tenant-domain> enrollencryptiontoken=<Encryption Token> mode=peruserconfig /qn
Example 1:
msiexec /I NSClient.msi tenant=corp domain=goskope.com installmode=IDP mode=peruserconfig enrollencryptiontoken=XXX /qn
Example 2:
msiexec /I NSClient.msi tenant=corp domain=eu.goskope.com  installmode=IDP mode=peruserconfig enrollencryptiontoken=XXX /qn
Deployment Option
Command
All MSIEXEC UPN Options
msiexec /I NSClient.msi host=addon-<tenant-name>.[region.]<tenant-domain> token=<Organization ID> [enrollauthtoken=<Authentication Token>] [enrollencryptiontoken=<Encryption Token>] [mode=peruserconfig [npavdimode=on] [userconfiglocation=<path>]] [fail-close=no-npa|disable] [prelogonuser=<prelogon username>@prelogon.netskope.com] [INSTTAG=Tag 1, Tag 2] [autoupdate=on|off] [/l*v %PUBLIC%nscinstall.log] [/qn]
Single-User Mode Installation for Domain-joined Endpoints
System-level enrollment; auto-enrolled one time based on the UPN of the first domain user to log in
msiexec /I NSClient.msi host=addon-<tenant-name>.[region.]<tenant-domain> token=<Organization ID> enrollauthtoken=<Authentication Token> enrollencryptiontoken=<Encryption Token> /qn
Example 1:
msiexec /I NSClient.msi host=addon-corp.goskope.com token=XXX enrollauthtoken=XXX enrollencryptiontoken=XXX /qn
Example 2:
msiexec /I NSClient.msi host=addon-corp.eu.goskope.com token=XXX enrollauthtoken=XXX enrollencryptiontoken=XXX /qn
Multi-User Mode Installation for Domain-joined Endpoints
Per-user enrollment; each user auto-enrolled at login based on their UPN
msiexec /I NSClient.msi host=addon-<tenant-name>.[region.]<tenant-domain> token=<Organization ID> enrollauthtoken=<Authentication Token> enrollencryptiontoken=<Encryption Token> mode=peruserconfig /qn
Example 1:
msiexec /I NSClient.msi host=addon-corp.goskope.com token=XXX enrollauthtoken=XXX enrollencryptiontoken=XXX mode=peruserconfig /qn
Example 2:
msiexec /I NSClient.msi host=addon-corp.eu.goskope.com token=XXX enrollauthtoken=XXX enrollencryptiontoken=XXX mode=peruserconfig /qn
To install and enable the Netskope Client for
Netskope Private Access Prelogon connectivity
, include the prelogonuser, enrollauthtoken, and enrollencryptiontoken parameters in the table referenced in the previous
section
.
Prelogon Usernames are configured in Client Configurations. The Prelogon Username set in the Windows installer (msiexec) parameters must match an existing Client Configuration.
msiexec /I NSClient.msi host=addon-<tenant-name>.[region.]<tenant-domain> token=<Organization ID> enrollauthtoken=<Authentication Token> enrollencryptiontoken=<Encryption Token> mode=peruserconfig prelogonuser=<prelogon user>@prelogon.netskope.com /qn
Example with Client Configuration configured with Prelogon User user1@prelogon.netskope.com:
msiexec /I NSClient.msi host=addon-corp.goskope.com token=XXX enrollauthtoken=XXX enrollencryptiontoken=XXX mode=peruserconfig prelogonuser=user1@prelogon.netskope.com /qn
To learn more, view
Configure Client Prelogon Connectivity
.
For MDM-specific deployments, view
Netskope Client Deployment Options
.
Netskope Client Support for 64-Bit Version
With version 131.0.0, Netskope upgraded its support from 32-bit to 64-bit mode for Windows OS. This enhancement allows Netskope Client to utilize the native 64-bit capabilities of the operating system; that may improve the traffic forwarding performance. Administrators can comply to their organization software policies by having 64-bit native agents running on their end-user devices.
After the feature is available for all tenants, you can upgrade to the latest version of Netskope Client for your 64-bit OS through
auto-upgrade
or using the existing the
Netskope Client deployment options
.
On a Windows machine, the Netskope Client detects if the OS is running in 64-bit or 32-bit mode and runs in 64-bit mode only if the OS supports; otherwise it fallback to the 32-bit mode.
While upgrading from 32 bit to 64 bit:
The 32 bit Netskope Client automatically upgrades to the 64 bit version during the subsequent upgrade cycle if the Auto-Upgrade option in  Client Configuration is set to 64 bit.
Users can view the Client architecture (for example, x64) alongside the version number by navigating to Netskope Client UI > About.
Upgrade Rollback
In case of any MSI issues during the upgrade process to the 64-bit Netskope Client for Windows, the Netskope Client roll back and restores the original 32-bit Netskope Client for Windows. The upgrade service monitor can also restart the upgrade process on failure.
Uninstall Netskope Client In Windows
This section provides the instructions to uninstall Netskope Client from your Windows devices. You can uninstall using multiple methods as outlined in the following sections.
Manual Uninstallation
To uninstall Client from Settings in Windows:
Go to
Start
>
Settings
>
Apps
>
Apps & Features
.
Find and select the Netskope Client app.
Click
Uninstall
.
You are prompted to enter your administrative credentials at this point.
Click
OK
.
The Netskope Client is uninstalled from your machine.
The Password protection for Client uninstallation and service stop option under Client Configuration > Tamperproof lets the administrator restrict unauthorized Client uninstallation by the end users. The end user must know the password set by the administrator while uninstalling the Client. To learn more, view
Netskope Client Configuration
.
You can check
Apps & features
under
Apps
to ensure that the Netskope Client is uninstalled from your device. To learn more about uninstalling applications used in other Windows features, view
Uninstall Apps in Windows
.
Using MSI file From PowerShell
To uninstall Client:
Open PowerShell as an administrator.
Enter the following command:
Start-Process msiexec.exe -ArgumentList "/x <PRODUCT_CODE> PASSWORD=<PASSWORD> /qn /norestart /l*v `"$env:PUBLIC\nscuninstall.log`"" -Wait -Verb RunAs
The PASSWORD parameter is optional unless Password Protection for Client uninstallation is configured under
Tamperproof
in Client Configuration.
Execute the following command in PowerShell to find the product code:
Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*,HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* -ErrorAction SilentlyContinue | Where-Object {$_.DisplayName -eq "Netskope Client"} | Select-Object -ExpandProperty PSChildName
Using GPO Scripts
You can uninstall through GPO using a batch script similar to installation. The uninstallation script is:
Get-WmiObject Win32_Product | Where-Object Name -eq "Netskope Client" | % { $_.Uninstall() }
Using Script in Microsoft Endpoint Configuration Manager
@echo off
REM ---------------------------------------------------------------
REM Improved Uninstall Netskope Client (Password Protected)
REM Uses PowerShell to read registry and extract MSI GUID
REM ---------------------------------------------------------------
setlocal
set "LOGFILE=%PUBLIC%\nscuninstall.log"
set "PASSWORD=<password>"
echo Searching for Netskope Client...
powershell -NoLogo -NoProfile -Command ^
    "$apps = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*,HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Where-Object { $_.DisplayName -eq 'Netskope Client' };" ^
    "if (-not $apps) { Write-Host 'Netskope Client not found.'; exit 1 };" ^
    "$success = $false;" ^
    "foreach ($app in $apps) {" ^
    "    Write-Host 'Found:' $($app.DisplayName);" ^
    "    if ($app.UninstallString -and $app.UninstallString -match '\{[A-F0-9\-]+\}') {" ^
    "        $guid = $matches[0];" ^
    "        Write-Host \"Uninstalling $($app.DisplayName) with GUID: $guid\";" ^
    "        try {" ^
    "            Start-Process msiexec.exe -ArgumentList \"/x $guid PASSWORD=`\"%PASSWORD%`\" /qn /l*v `\"%LOGFILE%`\"\" -Wait -PassThru | Out-Null;" ^
    "            Write-Host 'Uninstall completed for:' $($app.DisplayName);" ^
    "            $success = $true;" ^
    "        } catch {" ^
    "            Write-Error \"Failed to uninstall $($app.DisplayName): $_\";" ^
    "            exit 2;" ^
    "        }" ^
    "    } else {" ^
    "        Write-Host 'No MSI GUID found for:' $($app.DisplayName);" ^
    "    }" ^
    "};" ^
    "if (-not $success) { exit 2 } else { exit 0 }"
set "ec=%ERRORLEVEL%"
if %ec%==0 (
    echo Uninstallation completed successfully.
) else if %ec%==1 (
    echo Netskope Client not found.
) else (
    echo Uninstallation failed. Check the log file: %LOGFILE%.
)
endlocal
exit /b
– You can also save this script as a .bat file and execute it locally from Windows Command Prompt.
– This script works only in Admin mode.
Multilingual Support For Windows
Netskope supports the following languages for Netskope Client:
French
German
This helps non-english speaking users understand Netskope Client menu and notifications. To display end-user Netskope Client notifications in French and German, modify your language and region settings in the Windows devices. To learn more about how to change your language and region settings in your Windows devices, view
Manage display language settings in Windows
.
English Language Support For Netskope Client UI
With version 130.0.0, Netskope allows displaying the Netskope Client UI options for Windows in a language selected in the
Windows display language
setting. To configure:
In Windows 11, go to
Settings
>
Time & Language
>
Language & region
and select the desired language in
Windows display language
.
In Windows 10, go to
Settings
>
Time & Language
>
Language
and select the desired language in
Windows display language
.
This option is more suitable for instances where the Netskope Client UI is displayed in one language while the Regional Format setting for the device is in another language.
Windows Support For WSLv2
Netskope Client supports
Windows Subsystem for Linux
(WSL) version 2 that allows you to run  Linux on your Windows devices without the need of a separate virtual machine. This enables a seamless and simultaneous usage of Windows and Linux operating systems. You can deploy
Netskope Client for Linux
onto a Linux distribution to extend Netskope services to WSLv2 Linux environment.
– Currently, Netskope Client extends only command-line interface (CLI) support for WSLv2.
– Windows support for WSLv2 is now available for Netskope Private Access.
– Periodic reauthentication is not supported with the CLI version of the Linux Client on WSLv2.
To learn more, view
Install Linux on Windows Using WSL
.
Supported Versions
Windows OS: Windows 10 and later versions.
WSLv2  and Minor Version 0.67.6 or above.
Netskope Client: Version 113.0.0 or later.
Set the
systemd
flag in your WSL distro settings.  If systemd is disabled, turn on the flag and reboot the distro.Check the WSL version and Netskope Client does not support WSLv1.
Limitations
WSL Linux distribution contains no login name as it does not support UI desktop by default. This info only appears as an install log message and not used by Netskope Client features. Hence it does not impact any functionalities.
The device manufacture information is not available in WSL Linux distributions as the standard file “/sys/devices/virtual/dmi/id/sys_vendor”  does not exist. Device Manufacture information is for display only and does not impact any functionalities of the product.
If the Netskope Client for Linux is installed before the installation of browser applications such as Firefox and Chrome, a reboot of the WSL distro is required.
Netskope Client Auto-Restart
To address situations where users forget to re-enable the Netskope Client after disabling it, Netskope introduced a feature flag called
AutoStart NSClient with Reboot/Relogin
. After the administrator enables the feature flag, Netskope Client re-enables automatically the next time the user restarts their system or logs out and logs in again.
– Contact Netskope Support to enable this feature for your tenant.
– This feature is available only for Windows and macOS devices.
– Administrators cannot use this feature flag alongside NPA services.
– This feature does not apply when the user puts the device in sleep mode.
Netskope Client Auto-Upgrade Failures and Rollback
In certain situations, the Netskope Client can encounter issues during the auto-upgrade process that require halting the upgrade and reverting to the previous version.
In the event of an upgrade or uninstallation failures, the Netskope Client rolls back to the previous version of the Client thereby preventing disruption on the end-user device.
To view the events related to Client upgrades or upgrade failures, navigate to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Devices
to view the events displayed during the Client upgrade failure. Click the device name to view the related events and the corresponding details. The following table lists the different events displayed in the event of a Client upgrade or uninstallation:
Event
Event Details
Installed
Installed client version ‘x’
Uninstalled
Uninstalled client version ‘x’
Installation Failure
Failed to install client version ‘x’ – < reason for failure>
Uninstallation Failure
Failed to uninstall client version ‘x’ – < reason for failure >
Upgraded
Upgraded from client version ‘x’ to ‘y’
Upgrade Failure
Failed to upgrade from ‘x’ to ‘y’ – < Reason for failure >
Rollback Success
Rolled back to client version ‘x’
Rollback Failure
Failed to rollback to client version ‘x’
Rollback Success, Upgrade Failure, Installed
Rollback Failure
Uninstalled, Uninstallation Failure
Upgraded
Client Upgrade Failure During System Restart/ Shutdown/ Hard Reboot/ Power Failure
There are occurrences where the auto-upgrade processes gets impacted due to unplanned events such as:
System restart
Shutdown
Crash
Hard reboot
Power failure
To reduce issues during the upgrade process, Netskope creates an installation monitor service
stAgentSvcMon.exe
that is a copy of the existing Netskope Client Services, with limited functionality. The installation monitor service relaunches the Client installation process on the end-user device whenever the auto-upgrade process is interrupted by system restart, crash, shutdown, hard-reboot, or power failure. Once the auto-upgrade process is completed, this monitor service is removed from the endpoint.
However, there are a few scenarios that stops the monitor service from relaunching the Client installation process. Refer to the following table to learn more:
Scenario
Client Behavior
Consecutive system restarts during the auto-upgrade process
The monitor service stops the auto-upgrade process after two attempts.
The monitor service stops
In case of improper upgrade, Installation monitor service reattempts to upgrade twice before ending the process.
The auto-upgrade process fails and an unplanned event like system restart or crash happens during rollback phase
The monitor service attempts to reinstall the new build.
Antivirus configurations block the monitor services
The copy of the Client services is not launched.
Unplanned Windows Installer (msiexec) behavior during upgrades
Sometimes, Windows Installer (msiexec) may restart the system during this process.
Private Access Tunnel Status Update in Windows Registry
Private Access service on Netskope Windows Client updates the status of the tunnel in the following registry location:
HKEY_LOCAL_MACHINE\SOFTWARE\NetSkope\NpaTunnel/NpaStatus
Status Descriptions
Tunnel Status              Registry Value
Enabled                        Connected
Disabled                       Disconnected
In addition, the timestamp at which this status change was made is updated in the following registry location: HKEY_LOCAL_MACHINE\SOFTWARE\NetSkope\NpaTunnel/NpaStatusLastChanged.
In this Topic
Netskope Client For Windows

---
## Deploy Client on iOS Using Jamf School
**URL:** https://docs.netskope.com/en/deploy-client-on-ios-using-jamf-school/
**Last Modified:** 2025-12-08T18:01:01+00:00
**Scraped:** 2026-06-26T09:38:00.911263+00:00

Deploy Client on iOS Using Jamf School
This section describes the steps to deploy the Netskope Client app in an iOS device using Jamf School.
Prerequisites
Administrators must possess proficient working knowledge of Jamf School.
Administrators must review
Netskope Client Enrollment Methods
to understand the Client User Enrollment methods available for their environment.
Users must be imported into the Netskope tenant – see
Provisioning Users for Netskope Client
Download
Netskope Root and Tenant Certificates
and ensure the certificates are available when needed.
Download the Netskope package for macOS from
Netskope Support
.
See
Deploy Netskope Client via IdP
when using IDP as the method of user enrollment.
In Jamf School, enable the
Scripting
option under
Organization
>
Settings
>
Modules
to allow you to add the required scripts.
Supported Platforms and Enrollment Methods
This article outlines Netskope Client deployment instructions for the following user enrollment methods and support platforms. User enrollment methods not documented here are not supported at this time.
Enrollment Methods
Single User
Multi-user
IDP
N
N
PLIST
Y
N
Profile Setup
Jamf Configuration Profiles manage the core configuration for Client installation. The following sections provide a detailed overview of how to configure these profiles effectively.
Create Profile
Creating profiles is useful as it can help define and configure the system settings such as VPN, Restrictions, and so on for your device. Always create a profile before you start configuring the profile settings. For more information, view
Profiles
.
Log into
JAMF School
.
Go to
Profiles
.
Click
+Create Profile
.
In
Platform
, select the following:
Select the
Platform
as
iOS
Select the
Enrollment Type.
Click
Next
.
In
Details
, perform the following:
Enter the profile name.
Enter the description for the profile.
Click
Next
.
In
Time Filter
, select the checkbox to configure the time at which you want to apply the profile to the devices.
Click
Finish
.
After creating the profile, it navigates to the page where you can set up the profile details such as
Certificates
,
System Extensions
, and so on. Refer to the following sections to learn more about adding different attributes in your profile.
Pre-Approve VPN Popup for App Proxy
The Netskope Client on macOS installs a network extension that triggers updates to the device’s Network settings. The following configuration pre-approves these updates and suppresses end-user notifications requesting approval.
In the Jamf School console, go to
Profiles
.
Select and open the required Profile.
Click
Scope
.
Click
+
to add the desired group.
Click
Save
.
Go to
iOS Payload
>
VPN
.
The Netskope Client updates this definition, pre-creating it to prevent prompting the user to add a new VPN configuration.
Refer to the following table to understand the VPN configuration attributes:
Attribute Name
Value
Connection Name
Anything
Connection Type
Custom SSL
Identifier
com.netskope.Netskope (case sensitive)
Provider Type
Packet Tunnel
Server
gateway-[tenantname].goskope.com
User Authentication
Password
Enable VPN on-demand
Note: This document goes with the On-demand VPN. You can choose to use Per-App VPN config
enable option
On demand rules configuration XML
Action
Connect
InterfaceTypeMatch
WiFi
Action
Connect
InterfaceTypeMatch
Cellular
Prohibit users from disabling on-demand VPN settings
enable option
Click
Save
.
To add zero-touch configuration, use the Custom Data field in VPN. Adding zero-touch configurations allow automated deployment of the Client thereby removing the user interaction for enrollment. To add zero-touch, use the following Key-Value pair:
OrgKey: Use the tenant organizational key
AddonHost: Use the addon URL for the tenant:
addon-<tenant-URL>
UserEmail: Use the variable that contains the user identity for the enrolment. Most likely %Email%
Do not use Managed Configuration if you are planning to automate the deployment process of the NS Client.
Restrict App Proxy Removal
Netskope recommends adding two optional deployment parameters
Prevent Disabling of System Extensions
and
Restrict App Proxy Removal
to manage user permissions regarding System Extensions in macOS 15 (Sequoia) and above. These controls prevent the removal of the specified system extension by the user.
In the Jamf School console, go to
Profiles
.
Select and open the required Profile.
Click
Scope
.
Click
+
to add the desired group.
Click
Save
.
Go to
iOS Payload
>
Restrictions
.
Disable
Allow creation of VPN configurations
in the
Connectivity
settings.
Setup Notifications
This step is optional.
Perform the following steps to configure Notifications:
In the Jamf School console, go to Profiles.
Select and open the required Profile.
Click
Scope
.
Click + to add the desired group.
Click Save.
Go to
General Payload
>
Notifications
.
Configure this part to prevent the Netskope Client from prompting the user to enable its notifications.
Click
Save
.
Push Netskope Root and Tenant Certificates Through Jamf School
Provide additional trust to end users by pushing Netskope certificates during Client installation. Before pushing the root and tenant certificates, ensure that you do the following:
Download root and tenant certificates from Netskope MDM distribution page.
Login to Netskope tenant admin console with admin credentials.
Go to
Settings
>
Security Cloud Platform
>
MDM Distribution
. The certificate download options are displayed in the Certificate Setup section.
Convert the downloaded certificates to
.cer
format by renaming the
.pem
files to
.cer
.
Perform the following steps to add certificates to Jamf School:
In the Jamf School console, go to
Profiles
.
Select and open the required Profile.
Click
Scope
.
Click
+
to add the desired group.
Click
Save
.
Go to
General Payload
>
Certificates
.
In
Select your file
, click
Choose
File
and upload the root certificate.
Click
Upload Certificate
.
Repeat the same steps to upload the Netskope Intermediate certificate.
Click
Save
.
Create an App
To create an app:
Next, click
Apps
>
Inventory
.
Click
+ Add App
to add the Netskope application and select
Add iOS App
from the dropdown menu.
Add Netskope Client application.
Edit the installed application and ensure to select
Apply Managed Configuration
.
Go to the
Managed Configuration
section and provide the configuration details.
<plist version="1.0">
<dict>
<key>OrgKey</key>
<string>xxxxxxxxxxxxxx</string>
<key>UserEmail</key>
<string>%Email%</string>
<key>AddonHost</key>
<string>addon-<tenant-URL>/string>
<key>EnrollAuthToken</key>
<string>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</string>
<key>EnrollEncryptionToken</key>
<string>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</string>
</dict>
</plist>
– You must replace OrgKey and Addon Host with tenant values.
– Ensure that the managed configuration is applied to the user/device before deploying. Failure to do so prevents the Netskope client from downloading its configuration.
– Zero-touch deployment: Do not use the managed configuration as it conflicts with the VPN profile.
Verifying Client Installation
Check the installation logs on the user’s machine in the /var/log/install.log folder. If the user configuration download script fails and the Netskope client installer is executed, the installer will exit and display the “Configuration file missing, aborting installation! error” message.
Check Netskope Client Installation Status
To verify the status of each device, go to
Computer
>
Policies
and click on the policy you created.
Click the
Logs
button at the bottom to view the log files for each device and then click the
Show
button.
Confirming the Netskope Client Extension Approval
To confirm that the Netskope Client extension has been approved and the client is running, run the following command in your macOS terminal window:
systemextensionsctl list
The output should look like this:
% systemextensionsctl list  
1 extension(s)
--- com.apple.system_extension.network_extension
enabled active teamID bundleID (version) name [state]
* * 24W52P9M7W com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy (85.2.0.269/1) 
NetskopeClientMacAppProxy [activated enabled]
Additionally, inspect the system preferences and Network UI to confirm that Netskope Client extension is active.
Uninstalling Netskope Client
See
Uninstalling the Netskope Client
for instructions on uninstalling the Netskope Client.
In this Topic
Deploy Client on iOS Using Jamf School

---
## Event Streaming Client
**URL:** https://docs.netskope.com/en/event-streaming-client/
**Last Modified:** 2026-01-07T19:45:12+00:00
**Scraped:** 2026-06-26T09:39:07.305763+00:00

Event Streaming Client - Netskope Knowledge Portal
Event Streaming Client
Event Streaming Client provides a high performance and centrally managed solution to stream Transaction Events to a SIEM.
This page provides an overview and references to other sections.
To learn more:
Event Streaming Client Architecture
Event Streaming Client Requirements
Event Streaming Client Deployment
Event Streaming Client Configuration
Proxy Configuration for Docker
Red Hat and Podman Configuration
Event Streaming Client Format Examples
Event Streaming Client API Access
Event Streaming Client Operations and Troubleshooting
Event Streaming Client FAQs
Supported features
Events generated by Netskope Proxy are forwarded to the SIEM via syslog in less than five minutes
Active/Active Event Streaming Clients to Active/Active SIEM
Transaction events only, up to format 4
Syslog TCP and UDP (TCP recommended to ensure no event is lost)
Customizable Syslog Header
Event format: JSON, CEF, ELFF
Customizable field selection:
Field selection with ordering
Field rename
Default value
Remove empty fields
HTTP proxy support for internet access
Weekly auto upgrade
All configuration is done via API to the cloud management, UI in the management console will be delivered in a second phase
Processing metrics available on the host. Metrics are collected centrally but are not yet exposed in the central console.
Known Limitations
FedRamp/PBMM environments are not yet supported
Multiple tenants on the same host are not yet supported
In this Topic
Event Streaming Client

---
## Event Streaming Client Architecture
**URL:** https://docs.netskope.com/en/event-streaming-client-architecture/
**Last Modified:** 2026-01-07T08:09:57+00:00
**Scraped:** 2026-06-26T09:39:08.421122+00:00

Event Streaming Client Architecture - Netskope Knowledge Portal
Event Streaming Client Architecture
Event Streaming Client can be deployed with or without high availability.
In all deployment modes, the solution includes:
No service to be published publicly on the customer side, all requests from Event Streaming Client are outgoing
Events are pushed from Event Streaming Server located in the tenant Management Plane to Event Streaming Client over GRPC tunnel. Event Streaming Client is not pulling events.
The events are packaged in batches of 50MB maximum.
No event loss with end to end acknowledgement (with syslog TCP): each event batch is acknowledged when fully streamed to the syslog target. In case of interruption during the processing or transfer, the batch will be restarted.
An event batch is following a single path: all events of a batch are processed by a single Streaming Client and sent to only one syslog server.
An event batch is only sent once, it cannot be distributed to multiple syslog servers.
There are no communication required between the Event Streaming Clients.
Data retention is only done in the Management Plane, not on the Event Streaming Client.
Data processing is done in memory only, events are not stored on disk inside the Event Streaming Client.
Network flows
To work properly, the Event Streaming Client require outgoing Internet connectivity direct or via HTTP Proxy.
All flows are initiated by the Event Streaming Client, there are no service to publish publicly.
Direct
Event Streaming Client – Direct flows
HTTP Proxy
Event Streaming Client – HTTP Proxy flows
Event Streaming Client without High Availability
In this mode all batches are processed by a single Event Streaming Client and sent to a single syslog Server.
In this example, a single target is configured:
Client 1 → Syslog Server A
Event path without High Availability
Event Streaming Client with High Availability on the Client
When two or more clients are available, the Event Streaming Servers are load balancing the event batches to each Event Streaming Clients.
In this example, 2 targets are configured:
Client 1 → Syslog Server A
Client 2 → Syslog Server A
Event path with High Availability
Event Streaming Client with High Availability on the Client and the Syslog Server
In addition to Event Streaming Client load balancing, when a Client has two or more Syslog Servers defined, the batches will be load balanced by the Client between available Syslog Servers.
In this example, 4 targets are configured:
Client 1 → Syslog Server A
Client 1 → Syslog Server B
Client 2 → Syslog Server A
Client 2 → Syslog Server B
Event path with High Availability and Syslog load balancing
Event batches will be load balanced between the two Syslog Servers.
Event Streaming Client with High Availability on Multiple Datacenters
To provide High Availability on multiple datacenters, it’s possible to have one Event Streaming Client on each location.
In this example, 4 targets are configured:
Client 1 → Syslog Server A
Client 2 → Syslog Server A
Client 3 → Syslog Server B
Client 4 → Syslog Server B
Event path with load balancing on multiple locations
Event batches will be load balanced between the two Syslog Servers.
In this Topic
Event Streaming Client Architecture

---
## Event Streaming Client Requirements
**URL:** https://docs.netskope.com/en/event-streaming-client-requirements/
**Last Modified:** 2026-02-10T17:02:31+00:00
**Scraped:** 2026-06-26T09:39:09.537138+00:00

Event Streaming Client Requirements - Netskope Knowledge Portal
Event Streaming Client Requirements
Licensing requirements
Event Streaming Client is available for customers with “Log Streaming” or “Transaction Event Streaming” licenses. Please contact Netskope to get a trial license.
Sizing guide with expected performance
Instance Type
Specifications
Large
16 cores
3 GHz
16 GB of RAM
Disk 16 GB for the docker system
10 Gbps network interface
Medium
8 cores
3 GHz
8 GB of RAM
Disk 16 GB for the docker system
2.5 Gbps network interface
Small
4 cores
3 GHz
4 GB of RAM
Disk 16 GB for the docker system
1 Gbps network interface
Network requirements
Flows for building and running the docker, either with direct connectivity or via HTTP Proxy:
streamingclient-<MP>.events.goskope.com, ports 443 (HTTPS for config and monitoring), 50051 (GRPC over TLS)
access to
http://hub.docker.com
to download the image and auto update
Event flow to SIEM
syslog flow to the configured destination
Software requirements
Supported OS: Ubuntu 22 and 24, Red Hat 8 and 9
Supported Python version: 3.9 or above
Supported containers: Docker or Podman
In this Topic
Event Streaming Client Requirements

---
## Event Streaming Client Deployment
**URL:** https://docs.netskope.com/en/event-streaming-client-deployment/
**Last Modified:** 2026-01-07T17:19:31+00:00
**Scraped:** 2026-06-26T09:39:10.689885+00:00

Event Streaming Client Deployment
Before deployment, please:
review
Event Streaming Client Architectures
and define the target architecture.
review
Event Streaming Client Requirements
The deployment of Event Streaming Client requires the following steps:
Setting up API Access
Client installation for each Event Streaming Client to deploy.
One format configuration to define what data will be forwarded to the SIEM
One destination configuration to define the SIEM targets for each client and the active format
Log streaming configuration will then enable Event Streaming Client Destination
API access
Creating a role and token is covered in
Event Streaming Client API Access
Client Installation
Client installation is done in 2 steps:
Declaring a new client via API and generating a token
Deploying the client on the host device
Client Configuration
After successful authentication to Netskope API Swagger, the Event Streaming Client configuration is available with /api/v2/streamingclient/clients endpoints:
Create a new Client with the POST method by using “Try it out” button:
It is possible to check created Clients with GET method
For more details, check
Event Streaming Client Configuration
Download the installer
From Swagger
From Linux
Command:
curl -X 'GET' 'https://<tenant>.goskope.com/api/v2/streamingclient/installer' -H 'accept: application/gzip' -H 'Authorization: Bearer XXXX' -OJ
Example:
root@lab-esc1:~# curl -X 'GET' 'https://<tenant>.goskope.com/api/v2/streamingclient/installer' -H 'accept: application/gzip' -H 'Authorization: Bearer XXXX' -OJ
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10796  100 10796    0     0  57922      0 --:--:-- --:--:-- --:--:-- 58994
root@lab-esc1:~# tar -zxvf NS_StreamingClient_Installer.tar.gz
netskope_event_streamingclient_installer.py
README.md
Instance Deployment
Connect to the Linux Server
Make sure Python3 and Docker are installed
Get the installer from the previous step
Check dedicated configuration for your system
To use docker with an HTTP Proxy, refer to
Proxy configuration for Docker
To use RHEL with Podman, refer to
Red Hat and Podman configuration
Run the installer script
python3 netskope_event_streamingclient_installer.py
6. Select
install
option and answer all requested inputs:
location of the files, by default
/root/ns
Enter the client key
is the token generated with the API
/api/v2/streamingclient/clients/{id}/token
Day and time of the week for the auto update
Optionally define the HTTP Proxy
Example
root@lab-esc2:~# python3 netskope_event_streamingclient_installer.py
NETSKOPE LOG STREAM CLIENT INSTALLER I.2025.11.1
Please specify an option:
1. install   - Set up and configure the container
2. reinstall - Remove and recreate the container
3. uninstall - Remove the container and cleanup
Enter option (install/reinstall/uninstall): 1
INSTALLATION
>>> Checking if operating system is supported...
SUCCESS: Check for operating system passed.
>>> Checking if hardware architecture is supported...
SUCCESS: Check for Architecture passed.
>>> Checking if Docker is installed and running...
SUCCESS: Docker is installed.
SUCCESS: Docker daemon is running.
SUCCESS: All the systems checks passed.
Configuring container ...
Enter the directory path to store the installation files and logs [default: /root/ns]:
Enter the client key : eyJDT05ORUNUSU9OX0tFWSI6InN0cmVhb
Client key: eyJDT05ORUNUSU9OX0tFWSI6InN0cmVhbWluZ2NsaWVudC1h
Please set up a weekly schedule for automatic Docker image updates.
Do you want to use the default schedule (Thursday at 23:00)? [y/n]: y
>>> Configuring proxy settings...
Do you need proxy setup for Streaming Client? [y/n] (default: n): y
INFO: Configuring proxy for containers
--- Streaming Client Container Proxy Configuration ---
This proxy will be used by the running containers for their operations.
HTTPS Proxy URL (e.g., http://proxy.company.com:8080 or https://proxy.company.com:8080): http://163.xxx.xxx.80:80
INFO: Container HTTPS proxy configured: http://163.xxx.xxx.80:80
>>> Setting up and starting the container...
INFO: Using existing installation directory: /root/ns
>>> Pulling Docker image: netskope/nsstreamingclient:stable
The process might take a moment...
stable: Pulling from netskope/nsstreamingclient
645635fbf4d2: Pull complete
c9debdf8207a: Pull complete
94e09fa58eb4: Pull complete
c5b5b574d9eb: Pull complete
9a47257481ca: Pull complete
2f5e1dfb2cd4: Pull complete
f9514487b3cf: Pull complete
78e884c4c39d: Pull complete
2aac2ff272d9: Pull complete
da51ee03c947: Pull complete
a84060cbac16: Pull complete
477d64974173: Pull complete
9a1325d79269: Pull complete
a71a358f9aef: Pull complete
44d06538ce68: Pull complete
14477cceda61: Pull complete
8fb98c22d537: Pull complete
db9fdfbf3f52: Pull complete
4958661942a9: Pull complete
1540d139dc0c: Pull complete
b1f4e241f375: Pull complete
94bfc05d13f2: Pull complete
7f247b6c83f6: Pull complete
a8cda5c427fe: Pull complete
28eedd26b6c7: Pull complete
b9ce487eef38: Pull complete
0f452909bfe0: Pull complete
bcdfc9f5c9e1: Pull complete
082b67164622: Pull complete
336355755be8: Pull complete
9e505fd59acf: Pull complete
c4a41b87cf93: Pull complete
de55d536641a: Pull complete
11aacba49461: Pull complete
Digest: sha256:ea143d8520
Status: Downloaded newer image for netskope/nsstreamingclient:stable
docker.io/netskope/nsstreamingclient:stable
SUCCESS: Docker image pulled successfully!
INFO: Configuring container volumes and environment variables...
INFO: Initialized installer information log file.
INFO: Container configuration file created successfully
INFO: Creating proxy configuration file...
INFO: Creating proxy configuration file...
SUCCESS: Proxy configuration saved to proxy.env
INFO: Starting container...
INFO: Adding HTTPS proxy to container: http://163.xxx.xxx.80:80
e9fe4c230e5cc191
SUCCESS: Container 'nsstreamingclient' started successfully!
Container files and Log files will be stored in: /root/ns
>>> Setting up watcher container to monitor the main container...
INFO: Pulling watcher image...
stable: Pulling from netskope/nswatcher
21b919804656: Pull complete
891cc33da41a: Pull complete
e6eb3a86a632: Pull complete
edeb9247ddd4: Pull complete
f988b2dd9cbf: Pull complete
ef090e4f8d13: Pull complete
b935cef6a087: Pull complete
06e748922bc3: Pull complete
49b990c12c1f: Pull complete
fa2956f00aa5: Pull complete
3df31e584803: Pull complete
4164121f60f1: Pull complete
f99197fd9601: Pull complete
1737cff1e8c9: Pull complete
60957cee4d80: Pull complete
964929934f06: Pull complete
5d335edf6f34: Pull complete
26ddf93d0751: Pull complete
141fda38c9b5: Pull complete
093dc20aa13e: Pull complete
Digest: sha256:8eb9a2
Status: Downloaded newer image for netskope/nswatcher:stable
docker.io/netskope/nswatcher:stable
INFO: Starting watcher container...
INFO: Adding container HTTPS proxy to watcher container: http://163.xxx.xxx.80:80
f519daf55cax
SUCCESS: Watcher container started successfully!
>>> Waiting for configuration to complete (max 60 seconds)...
PROGRESS: Client is not enabled
INFO: Installation successful. Waiting for configuration download...
INFO: Monitoring for 15s ...
Successfully downloaded stream configuration
INSTALLATION COMPLETE
root@lab-esc2:~#
Instance validation
To verify the instance is running we recommend to check
Instance is running
root@lab-esc1:~# docker ps
CONTAINER ID   IMAGE                               COMMAND                  CREATED         STATUS         PORTS     NAMES
ac518e00355f   netskope/nsstreamingclient:stable   "./start.sh s h ' ' …"   2 minutes ago   Up 2 minutes             nsstreamingclient
bf534b   netskope/nswatcher:stable           "bash start.sh"          2 days ago      Up 2 days                ns-watcher
root@lab-esc1:~#
Docker logs
root@lab-esc1:~# docker logs nsstreamingclient
2025/09/04 13:16:53 Primary config missing (/opt/ns/cfg/container_config). Trying fallback (/app/container_config)...
Install Log: Starting static configuration and token loading process.
Install Log: Configuration variables loaded successfully.
2025/09/04 13:16:53 Start decrypting container and connection keys from the env app.env file
2025/09/04 13:16:53 Starting metrics logging
{"level":"info","timestamp":"2025-09-04T13:16:53.112Z","caller":"log/log.go:86","msg":"Start collecting the system metrics"}
{"level":"info","timestamp":"2025-09-04T13:16:53.201Z","caller":"log/log.go:86","msg":"PROGRESS: Connected with syslog."}
{"level":"info","timestamp":"2025-09-04T13:16:53.201Z","caller":"log/log.go:86","msg":"PROGRESS: Syslog details verified."}
{"level":"info","timestamp":"2025-09-04T13:16:53.201Z","caller":"log/log.go:86","msg":"PROGRESS: Configuration verified."}
{"level":"info","timestamp":"2025-09-04T13:16:53.201Z","caller":"log/log.go:86","msg":"Successfully downloaded stream configuration"}
{"level":"info","timestamp":"2025-09-04T13:16:53.202Z","caller":"log/log.go:86","msg":"starting stream config watcher"}
{"level":"info","timestamp":"2025-09-04T13:16:53.209Z","caller":"log/log.go:86","msg":"Creating connections for log streamer","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","containerId":"0198eb4f-b0cd-71b8-8c20-0311959d806c","conNum":8}
{"level":"info","timestamp":"2025-09-04T13:16:53.346Z","caller":"log/log.go:86","msg":"GRPC connection established successfully"}
{"level":"info","timestamp":"2025-09-04T13:16:53.346Z","caller":"log/log.go:86","msg":"Successfully registered with Proxy","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"b4be021a-669a-49bb-856b-3fd284a00451"}
{"level":"info","timestamp":"2025-09-04T13:16:53.396Z","caller":"log/log.go:86","msg":"GRPC connection established successfully"}
{"level":"info","timestamp":"2025-09-04T13:16:53.396Z","caller":"log/log.go:86","msg":"Successfully registered with Proxy","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"15807d37-795a-49a2-a71c-c8036de319f6"}
{"level":"info","timestamp":"2025-09-04T13:16:53.442Z","caller":"log/log.go:86","msg":"GRPC connection established successfully"}
{"level":"info","timestamp":"2025-09-04T13:16:53.442Z","caller":"log/log.go:86","msg":"Successfully registered with Proxy","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"aa1fb4d5-112f-4300-933c-f074e3327e36"}
{"level":"info","timestamp":"2025-09-04T13:16:53.488Z","caller":"log/log.go:86","msg":"GRPC connection established successfully"}
{"level":"info","timestamp":"2025-09-04T13:16:53.488Z","caller":"log/log.go:86","msg":"Successfully registered with Proxy","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"b036e41f-7ab0-4ab4-b10f-2346700b1710"}
{"level":"info","timestamp":"2025-09-04T13:16:53.535Z","caller":"log/log.go:86","msg":"GRPC connection established successfully"}
{"level":"info","timestamp":"2025-09-04T13:16:53.535Z","caller":"log/log.go:86","msg":"Successfully registered with Proxy","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"eb579304-6a57-4cf3-a6aa-f2150ddef1bd"}
{"level":"info","timestamp":"2025-09-04T13:16:53.582Z","caller":"log/log.go:86","msg":"GRPC connection established successfully"}
{"level":"info","timestamp":"2025-09-04T13:16:53.583Z","caller":"log/log.go:86","msg":"Successfully registered with Proxy","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"73f362f1-30d3-4889-802b-740fcf382ac0"}
{"level":"info","timestamp":"2025-09-04T13:16:53.629Z","caller":"log/log.go:86","msg":"GRPC connection established successfully"}
{"level":"info","timestamp":"2025-09-04T13:16:53.629Z","caller":"log/log.go:86","msg":"Successfully registered with Proxy","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"bf3b6503-0ff9-47a4-ab09-3e4c7591936d"}
{"level":"info","timestamp":"2025-09-04T13:16:53.676Z","caller":"log/log.go:86","msg":"GRPC connection established successfully"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Successfully registered with Proxy","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"0a07b1dc-5a07-4496-b934-864a74dfeac3"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"starting stream...."}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log streamer","containerId":"0198eb4f-b0cd-71b8-8c20-0311959d806c"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log reader","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"b4be021a-669a-49bb-856b-3fd284a00451"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log reader","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"0a07b1dc-5a07-4496-b934-864a74dfeac3"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log reader","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"b036e41f-7ab0-4ab4-b10f-2346700b1710"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log reader","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"eb579304-6a57-4cf3-a6aa-f2150ddef1bd"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log reader","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"aa1fb4d5-112f-4300-933c-f074e3327e36"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log reader","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"bf3b6503-0ff9-47a4-ab09-3e4c7591936d"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log reader","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"15807d37-795a-49a2-a71c-c8036de319f6"}
{"level":"info","timestamp":"2025-09-04T13:16:53.677Z","caller":"log/log.go:86","msg":"Starting the Log reader","groupId":"0199054e-5765-72cf-803a-ebd2dcfc17e2","connID":"73f362f1-30d3-4889-802b-740fcf382ac0"}
Log files can also be found under folder
container_files/logs
inside the selected location at the installation
Description of log messages is provided in the “Troubleshooting” section at the bottom of the guide.
Format configuration
Event Streaming Client supports the following formats:
CEF
ELFF
JSON
While JSON is the most universal, it’s also the slowest because the structure. CEF is generally a good compromise between wide support and performance. ELFF remains the most performant but is not natively supported by all SIEMs.
Use POST to create a first Format
PATCH can be used to add or change options after creation
The Format ID is required to configure Destination object
For more details, check
Event Streaming Client Configuration
Example with Default JSON Format:
{
  "name": "Default JSON",
  "type": "JSON",
  "definition": {
    "remove_empty_fields": true,
    "customize": false
  }
}
Destination configuration
Destination object is used to define the SIEM address for each client.
To provide a fully working configuration, the following informations are required:
The Client ID found in the Client object (the Client object must be enabled)
The Format ID found in the Format object
The IP/Domain of the SIEM, the port and protocol to use
Create a destination with POST API
PATCH can be used to add or change options after creation
Make sure the Destination has
A Target with a working Client ID
The target is enabled
The Destination object is enabled
The Client object is enabled
For more details, check
Event Streaming Client Configuration
Example:
{
    "name": "Sample destination",
    "enabled": true,
    "type": "syslog_tcp",
    "format": "019914ed",
    "targets":
    [
        {
            "client": "0198eb4f",
            "ip": "lab-splunk4.info",
            "port": 5151,
            "enabled": true
        }
    ]
}
Log Streaming configuration
Only one Log streaming can be configured for Transaction Events
There is currently no validation of the Destination ID, make sure the destination ID is correct
Use POST /api/v2/events/logstreaming/stream API to register the Destination
{
  "streamType": "transaction",
  "name": "Transaction Stream",
  "provider": "streamingclient",
  "credential": {
    "streamingclient": {
      "client-destination": "REPLACE WITH YOUR DESTINATION ID"
    }
  },
  "compressionType": "zstd"
}
To edit an existing configuration, use the PUT /api/v2/events/logstreaming/stream/{streamId} API
For more details, check
Event Streaming Client Configuration
In this Topic
Event Streaming Client Deployment

---
## Event Streaming Client Configuration
**URL:** https://docs.netskope.com/en/event-streaming-client-configuration/
**Last Modified:** 2026-01-07T17:32:29+00:00
**Scraped:** 2026-06-26T09:39:11.831208+00:00

Event Streaming Client Configuration
Configuration on the Event Streaming Client is currently only available via REST APIv2. To learn how to setup API access refer to,
Event Streaming Client Deployment
.
This page provides reference for each API Endpoint.
To learn more:
Proxy configuration for Docker
Red Hat and Podman configuration
Format examples
Event Streaming Client API Access
To view a step-by-step configuration refer to,
Event Streaming Client Deployment
.
API Endpoint Standard Definition
For each object, there are five standard endpoints:
GET {object endpoint}
: List all objects with their configuration, pagination is available for long lists
POST {object endpoint}
: Create a new object
GET {object endpoint}/{id}
: Retrieve the definition of a single object
PATCH {object endpoint}/{id}
: Update the definition of a single object, it’s possible to only change one of the parameters
DELETE {object endpoint}/{id}
: Delete a single object, which is only possible if the object is not referenced in another configuration
Here is an example of the Format:
Each object is identified by its
id
attribute. This
id
is read only after creation and is unique per object type.
Creation example
POST
endpoint can be easily used to create a new object. Use the “Try it out” button and customize the json to define parameters.
Predefined json are only examples, remove parameters that are not relevant and edit remaining ones.
In the following example, a new client is created by defining only its name:
In the response, undefined parameters have a default value. If
id
is not defined at creation, a new one is automatically generated:
Read example
Both
GET
endpoints can be used to read existing configuration. The “List” will return all objects while adding the
/{id}
endpoint allows to read only one object
Example read for the object previously created:
Partial edit example
PATCH
endpoint can be used to edit an object.
Unmodified parameters can be removed from the JSON file.
In the following example, we will only enable the client:
The response will return the full configuration, allowing to control the status of all parameters:
Delete example
DELETE endpoint is used to delete any unreferenced object.
Example:
Client Configuration
Client Object Definition
{
  "id": "0198",
  "name": "Client-1",
  "description": "Primary streaming client for production environment",
  "enabled": true,
  "create_by": "esc",
  "create_time": "2025-08-27T13:59:51.83Z",
  "modify_by": "esc",
  "modify_time": "2025-08-27T13:59:51.83Z"
}
id
: UUID of the object, can defined at the creation time but read only after creation
name
: name of the object
description
: description of the object
enabled
: define if the client is disable or enabled. A disabled client can be installed but will not receive any log.
create_by
: admin account used for object creation (read only)
create_time
: creation time (read only)
modify_by
: admin account used for the last edit (read only)
modify_time
: time of the last edit (read only)
Client Object API Endpoints
Client Token Generation
/api/v2/streamingclient/clients/{id}/token
allows an admin to enroll an Event Streaming Client by returning a jwtToken. This token is requested when running the installer.
Example:
Format Configuration
Format object is used to define fields selected to the message sent via Syslog.
To learn more:
Event Streaming Client Format Examples
Format Object Definition
Format 1 CEF Example (click carrot to view details)
{
  "id": "019adf54-4d79-77e4-a224-8d9a941e1dad",
  "name": "Format 1 CEF",
  "description": "Transaction Event Format 1",
  "type": "CEF",
  "definition": {
    "remove_empty_fields": true,
    "customize": true,
    "custom_fields": [
      {
        "name": "date",
        "source": "date",
        "default": ""
      },
      {
        "name": "time",
        "source": "time",
        "default": ""
      },
      {
        "name": "time-taken",
        "source": "time-taken",
        "default": ""
      },
      {
        "name": "cs-bytes",
        "source": "cs-bytes",
        "default": ""
      },
      {
        "name": "sc-bytes",
        "source": "sc-bytes",
        "default": ""
      },
      {
        "name": "bytes",
        "source": "bytes",
        "default": ""
      },
      {
        "name": "c-ip",
        "source": "c-ip",
        "default": ""
      },
      {
        "name": "s-ip",
        "source": "s-ip",
        "default": ""
      },
      {
        "name": "cs-username",
        "source": "cs-username",
        "default": ""
      },
      {
        "name": "cs-method",
        "source": "cs-method",
        "default": ""
      },
      {
        "name": "cs-uri-scheme",
        "source": "cs-uri-scheme",
        "default": ""
      },
      {
        "name": "cs-uri-query",
        "source": "cs-uri-query",
        "default": ""
      },
      {
        "name": "cs-user-agent",
        "source": "cs-user-agent",
        "default": ""
      },
      {
        "name": "cs-content-type",
        "source": "cs-content-type",
        "default": ""
      },
      {
        "name": "sc-status",
        "source": "sc-status",
        "default": ""
      },
      {
        "name": "sc-content-type",
        "source": "sc-content-type",
        "default": ""
      },
      {
        "name": "cs-dns",
        "source": "cs-dns",
        "default": ""
      },
      {
        "name": "cs-host",
        "source": "cs-host",
        "default": ""
      },
      {
        "name": "cs-uri",
        "source": "cs-uri",
        "default": ""
      },
      {
        "name": "cs-uri-port",
        "source": "cs-uri-port",
        "default": ""
      },
      {
        "name": "cs-referer",
        "source": "cs-referer",
        "default": ""
      },
      {
        "name": "x-cs-session-id",
        "source": "x-cs-session-id",
        "default": ""
      },
      {
        "name": "x-cs-access-method",
        "source": "x-cs-access-method",
        "default": ""
      },
      {
        "name": "x-cs-app",
        "source": "x-cs-app",
        "default": ""
      },
      {
        "name": "x-s-country",
        "source": "x-s-country",
        "default": ""
      },
      {
        "name": "x-s-latitude",
        "source": "x-s-latitude",
        "default": ""
      },
      {
        "name": "x-s-longitude",
        "source": "x-s-longitude",
        "default": ""
      },
      {
        "name": "x-s-location",
        "source": "x-s-location",
        "default": ""
      },
      {
        "name": "x-s-region",
        "source": "x-s-region",
        "default": ""
      },
      {
        "name": "x-s-zipcode",
        "source": "x-s-zipcode",
        "default": ""
      },
      {
        "name": "x-c-country",
        "source": "x-c-country",
        "default": ""
      },
      {
        "name": "x-c-latitude",
        "source": "x-c-latitude",
        "default": ""
      },
      {
        "name": "x-c-longitude",
        "source": "x-c-longitude",
        "default": ""
      },
      {
        "name": "x-c-location",
        "source": "x-c-location",
        "default": ""
      },
      {
        "name": "x-c-region",
        "source": "x-c-region",
        "default": ""
      },
      {
        "name": "x-c-zipcode",
        "source": "x-c-zipcode",
        "default": ""
      },
      {
        "name": "x-c-os",
        "source": "x-c-os",
        "default": ""
      },
      {
        "name": "x-c-browser",
        "source": "x-c-browser",
        "default": ""
      },
      {
        "name": "x-c-browser-version",
        "source": "x-c-browser-version",
        "default": ""
      },
      {
        "name": "x-c-device",
        "source": "x-c-device",
        "default": ""
      },
      {
        "name": "x-cs-site",
        "source": "x-cs-site",
        "default": ""
      },
      {
        "name": "x-cs-timestamp",
        "source": "x-cs-timestamp",
        "default": ""
      },
      {
        "name": "x-cs-page-id",
        "source": "x-cs-page-id",
        "default": ""
      },
      {
        "name": "x-cs-userip",
        "source": "x-cs-userip",
        "default": ""
      },
      {
        "name": "x-cs-traffic-type",
        "source": "x-cs-traffic-type",
        "default": ""
      },
      {
        "name": "x-cs-tunnel-id",
        "source": "x-cs-tunnel-id",
        "default": ""
      },
      {
        "name": "x-category",
        "source": "x-category",
        "default": ""
      },
      {
        "name": "x-other-category",
        "source": "x-other-category",
        "default": ""
      },
      {
        "name": "x-type",
        "source": "x-type",
        "default": ""
      },
      {
        "name": "x-server-ssl-err",
        "source": "x-server-ssl-err",
        "default": ""
      },
      {
        "name": "x-client-ssl-err",
        "source": "x-client-ssl-err",
        "default": ""
      },
      {
        "name": "x-transaction-id",
        "source": "x-transaction-id",
        "default": ""
      },
      {
        "name": "x-request-id",
        "source": "x-request-id",
        "default": ""
      },
      {
        "name": "x-cs-sni",
        "source": "x-cs-sni",
        "default": ""
      },
      {
        "name": "x-cs-domain-fronted-sni",
        "source": "x-cs-domain-fronted-sni",
        "default": ""
      },
      {
        "name": "x-category-id",
        "source": "x-category-id",
        "default": ""
      },
      {
        "name": "x-other-category-id",
        "source": "x-other-category-id",
        "default": ""
      },
      {
        "name": "x-sr-headers-name",
        "source": "x-sr-headers-name",
        "default": ""
      },
      {
        "name": "x-sr-headers-value",
        "source": "x-sr-headers-value",
        "default": ""
      }
    ],
    "header": [
      {
        "name": "device_vendor",
        "source": "vendor_field",
        "default": "Updated Vendor"
      },
      {
        "name": "device_product",
        "source": "product_field",
        "default": "WebTX"
      },
      {
        "name": "device_version",
        "source": "version_field",
        "default": "2.0"
      },
      {
        "name": "signature_id",
        "source": "signature_id_field",
        "default": "unknown_signature"
      },
      {
        "name": "name",
        "source": "name_field",
        "default": "unknown_name"
      },
      {
        "name": "severity",
        "source": "severity_field",
        "default": "medium"
      }
    ],
    "syslog_header": "<%priority%>%timestamp% netskope"
  },
  "create_by": "esc",
  "create_time": "2025-12-02T13:50:35.385Z",
  "modify_by": "esc",
  "modify_time": "2025-12-02T14:00:03.728Z"
}
id
: UUID of the object, can defined at the creation time but read only after creation
name
: name of the object
description
: description of the object
type
: Format type from the following values:
JSON
,
CEF
,
ELFF
definition
: configuration of the fields list and content
remove_empty_fields
: if a field has no value, this option will remove the key (supported for
JSON
and
CEF
)
customize
: enable the
custom_fields
configuration to customize the content sent to the SIEM. Please note
customize
=
true
is now mandatory.
custom_fields
: ordered list of fields which support field selection, field rename and default value
name
: field name visible in the SIEM
source
: Netskope source field name, this value can be empty to create static fields (same value for all events, defined by
default
value) or must be one of the supported Transaction Events fields.
default
: if the
source
field has empty value (or
source
configuration is empty), Event Streaming Client will replace it with this definition.
header
: header configuration (only for
CEF
format)
name
: name of the CEF field
source
: Netskope source field name, this value can be empty to create static fields (same value for all events, defined by
default
value) or must be one of the supported Transaction Events fields.
default
: if the
source
field has empty value (or
source
configuration is empty), Event Streaming Client will replace it with this definition.
syslog_header
: configuration of the header added at the beginning of each syslog event following RFC 3164. The string can include variables enclosed between
%
, the following variables are supported:
%timestamp%
: host system time in UTC/GMT timezone in RFC 3164 format
Mmm dd
hh:mm:ss
. This is the host time, not the event time.
%hostname%
: system hostname
%priority%
: event priority
%pid%
: service running PID
create_by
: admin account used for object creation (read only)
create_time
: creation time (read only)
modify_by
: admin account used for the last edit (read only)
modify_time
: time of the last edit (read only)
Format Object API Endpoints
Only standard Endpoints are available for Format object:
Destination Configuration
Destination object definition
Example with two targets to the same syslog server:
{
    "id": "0198eb",
    "name": "Syslog1",
    "description": "Primary SIEM destination for production logs",
    "enabled": true,
    "type": "syslog_tcp",
    "format": "0198f093",
    "targets": [
      {
        "client": "0198ec",
        "ip": "syslog1.domain.local",
        "port": 514,
        "enabled": true
      },
      {
        "client": "0198f5410",
        "ip": "syslog1.domain.local",
        "port": 514,
        "enabled": true
      }
    ],
    "create_by": "esc",
    "create_time": "2025-08-27T11:44:40.557Z",
    "modify_by": "esc",
    "modify_time": "2025-09-01T12:45:13.966Z"
  }
Format object is used to define fields selected to the message sent via Syslog.
id
: UUID of the object, can defined at the creation time but read only after creation
name
: name of the object
description
: description of the object
enabled
: define if the destination is disable or enabled. A disabled destination will not streal any events. Only one destination can be enabled per tenant.
type
: either
syslog_udp
or
syslog_tcp
. We highly recommend
syslog_tcp
to avoid loss of events.
format
: the id of the format object previously configured
targets
: array which reference a streaming client and a syslog destination. Create a record for each client to syslog definition (the same client id can be used multiple times, the same syslog server destination can be used multiple times)
client
: the id of the client object previously configured
ip
: IP or FQDN of the syslog server
port
: TCP/UDP port of the syslog server
enabled
: status of the target. A disabled target will not receive any event
create_by
: admin account used for object creation (read only)
create_time
: creation time (read only)
modify_by
: admin account used for the last edit (read only)
modify_time
: time of the last edit (read only)
Destination Object API Endpoints
Only standard Endpoints are available for Destination object:
Log Streaming Configuration
There are currently three endpoints for log streaming configuration. Endpoints are
not
following API structure defined in the section,
API Endpoint Standard Definition
.
Create Stream for Event Streaming Client
Only one Log streaming can be configured for Transaction Events.
Example of JSON for stream creation:
{
  "streamType": "transaction",
  "name": "Transaction Stream",
  "provider": "streamingclient",
  "credential": {
    "streamingclient": {
      "client-destination": "019914ea"
    }
  },
  "compressionType": "zstd"
}
There is currently no validation of the Destination ID, make sure the destination ID is correct.
Read Stream Configuration
Edit Stream Configuration
There is currently no validation of the Destination ID, make sure the destination ID is correct.
Delete a Stream
HTTP Proxy Configuration
If Event Streaming Client requires an HTTP Proxy to download updates (docker pull), it must be configured at the systemd level following
Proxy configuration for Docker
.
If the Event Streaming Client requires an HTTP Proxy to connect to the Management Plane for configuration and events, it must be configured with the installation script, as covered in
Event Streaming Client Deployment
.
In this Topic
Event Streaming Client Configuration

---
## Event Streaming Client Format Examples
**URL:** https://docs.netskope.com/en/event-streaming-client-format-examples/
**Last Modified:** 2026-03-06T16:06:19+00:00
**Scraped:** 2026-06-26T09:39:15.291817+00:00

Event Streaming Client Format Examples - Netskope Knowledge Portal
Event Streaming Client Format Examples
Format examples
This page provide examples for format configuration.
JSON Format 1 to Format 4
CEF native Format 1 to Format 4
CEF Cloud Exchange Format 3
ELFF Format 1 to Format 4
JSON Format 1 to Format 4
Those configurations are providing mapping for legacy Format 1 to Format 4 field list.
Sample format 1 JSON
{
    "name": "Sample Format 1 JSON",
    "description": "From Online Help, Transaction Event Format 1 in JSON, Cloud Exchange migration",
    "type": "JSON",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,
        "custom_fields":
        &#91;
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            }
        ],
        "syslog_header": "&lt;%priority%>%timestamp% netskope"
    }
}</code></pre>
<!-- /wp:code -->
Sample format 2 JSON
{
    "name": "Sample Format 2 JSON",
    "description": "From Online Help, Transaction Event Format 2 in JSON, Cloud Exchange migration",
    "type": "JSON",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
Sample format 3 JSON
{
    "name": "Sample Format 3 JSON",
    "description": "From Online Help, Transaction Event Format 3 in JSON, Cloud Exchange migration",
    "type": "JSON",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,        
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            },
            {
                "name": "x-s-dp-name",
                "source": "x-s-dp-name",
                "default": ""
            },
            {
                "name": "x-cs-src-ip",
                "source": "x-cs-src-ip",
                "default": ""
            },
            {
                "name": "x-cs-src-port",
                "source": "x-cs-src-port",
                "default": ""
            },
            {
                "name": "x-cs-dst-ip",
                "source": "x-cs-dst-ip",
                "default": ""
            },
            {
                "name": "x-cs-dst-port",
                "source": "x-cs-dst-port",
                "default": ""
            },
            {
                "name": "x-sr-src-ip",
                "source": "x-sr-src-ip",
                "default": ""
            },
            {
                "name": "x-sr-src-port",
                "source": "x-sr-src-port",
                "default": ""
            },
            {
                "name": "x-sr-dst-ip",
                "source": "x-sr-dst-ip",
                "default": ""
            },
            {
                "name": "x-sr-dst-port",
                "source": "x-sr-dst-port",
                "default": ""
            },
            {
                "name": "x-cs-ip-connect-xff",
                "source": "x-cs-ip-connect-xff",
                "default": ""
            },
            {
                "name": "x-cs-ip-xff",
                "source": "x-cs-ip-xff",
                "default": ""
            },
            {
                "name": "x-cs-connect-host",
                "source": "x-cs-connect-host",
                "default": ""
            },
            {
                "name": "x-cs-connect-port",
                "source": "x-cs-connect-port",
                "default": ""
            },
            {
                "name": "x-cs-connect-user-agent",
                "source": "x-cs-connect-user-agent",
                "default": ""
            },
            {
                "name": "x-cs-url",
                "source": "x-cs-url",
                "default": ""
            },
            {
                "name": "x-cs-uri-path",
                "source": "x-cs-uri-path",
                "default": ""
            },
            {
                "name": "x-cs-http-version",
                "source": "x-cs-http-version",
                "default": ""
            },
            {
                "name": "rs-status",
                "source": "rs-status",
                "default": ""
            },
            {
                "name": "x-cs-app-category",
                "source": "x-cs-app-category",
                "default": ""
            },
            {
                "name": "x-cs-app-cci",
                "source": "x-cs-app-cci",
                "default": ""
            },
            {
                "name": "x-cs-app-ccl",
                "source": "x-cs-app-ccl",
                "default": ""
            },
            {
                "name": "x-cs-app-tags",
                "source": "x-cs-app-tags",
                "default": ""
            },
            {
                "name": "x-cs-app-suite",
                "source": "x-cs-app-suite",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-id",
                "source": "x-cs-app-instance-id",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-name",
                "source": "x-cs-app-instance-name",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-tag",
                "source": "x-cs-app-instance-tag",
                "default": ""
            },
            {
                "name": "x-cs-app-activity",
                "source": "x-cs-app-activity",
                "default": ""
            },
            {
                "name": "x-cs-app-from-user",
                "source": "x-cs-app-from-user",
                "default": ""
            },
            {
                "name": "x-cs-app-to-user",
                "source": "x-cs-app-to-user",
                "default": ""
            },
            {
                "name": "x-cs-app-object-type",
                "source": "x-cs-app-object-type",
                "default": ""
            },
            {
                "name": "x-cs-app-object-name",
                "source": "x-cs-app-object-name",
                "default": ""
            },
            {
                "name": "x-cs-app-object-id",
                "source": "x-cs-app-object-id",
                "default": ""
            },
            {
                "name": "x-rs-file-type",
                "source": "x-rs-file-type",
                "default": ""
            },
            {
                "name": "x-rs-file-category",
                "source": "x-rs-file-category",
                "default": ""
            },
            {
                "name": "x-rs-file-language",
                "source": "x-rs-file-language",
                "default": ""
            },
            {
                "name": "x-rs-file-size",
                "source": "x-rs-file-size",
                "default": ""
            },
            {
                "name": "x-rs-file-md5",
                "source": "x-rs-file-md5",
                "default": ""
            },
            {
                "name": "x-rs-file-sha256",
                "source": "x-rs-file-sha256",
                "default": ""
            },
            {
                "name": "x-error",
                "source": "x-error",
                "default": ""
            },
            {
                "name": "x-c-local-time",
                "source": "x-c-local-time",
                "default": ""
            },
            {
                "name": "x-policy-action",
                "source": "x-policy-action",
                "default": ""
            },
            {
                "name": "x-policy-name",
                "source": "x-policy-name",
                "default": ""
            },
            {
                "name": "x-policy-src-ip",
                "source": "x-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-ip",
                "source": "x-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-host",
                "source": "x-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-policy-dst-host-source",
                "source": "x-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-policy-justification-type",
                "source": "x-policy-justification-type",
                "default": ""
            },
            {
                "name": "x-policy-justification-reason",
                "source": "x-policy-justification-reason",
                "default": ""
            },
            {
                "name": "x-sc-notification-name",
                "source": "x-sc-notification-name",
                "default": ""
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
Sample format 4 JSON
{
    "name": "Sample Format 4 JSON",
    "description": "From Online Help, Transaction Event Format 4 in JSON, Cloud Exchange migration",
    "type": "JSON",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            },
            {
                "name": "x-s-dp-name",
                "source": "x-s-dp-name",
                "default": ""
            },
            {
                "name": "x-cs-src-ip",
                "source": "x-cs-src-ip",
                "default": ""
            },
            {
                "name": "x-cs-src-port",
                "source": "x-cs-src-port",
                "default": ""
            },
            {
                "name": "x-cs-dst-ip",
                "source": "x-cs-dst-ip",
                "default": ""
            },
            {
                "name": "x-cs-dst-port",
                "source": "x-cs-dst-port",
                "default": ""
            },
            {
                "name": "x-sr-src-ip",
                "source": "x-sr-src-ip",
                "default": ""
            },
            {
                "name": "x-sr-src-port",
                "source": "x-sr-src-port",
                "default": ""
            },
            {
                "name": "x-sr-dst-ip",
                "source": "x-sr-dst-ip",
                "default": ""
            },
            {
                "name": "x-sr-dst-port",
                "source": "x-sr-dst-port",
                "default": ""
            },
            {
                "name": "x-cs-ip-connect-xff",
                "source": "x-cs-ip-connect-xff",
                "default": ""
            },
            {
                "name": "x-cs-ip-xff",
                "source": "x-cs-ip-xff",
                "default": ""
            },
            {
                "name": "x-cs-connect-host",
                "source": "x-cs-connect-host",
                "default": ""
            },
            {
                "name": "x-cs-connect-port",
                "source": "x-cs-connect-port",
                "default": ""
            },
            {
                "name": "x-cs-connect-user-agent",
                "source": "x-cs-connect-user-agent",
                "default": ""
            },
            {
                "name": "x-cs-url",
                "source": "x-cs-url",
                "default": ""
            },
            {
                "name": "x-cs-uri-path",
                "source": "x-cs-uri-path",
                "default": ""
            },
            {
                "name": "x-cs-http-version",
                "source": "x-cs-http-version",
                "default": ""
            },
            {
                "name": "rs-status",
                "source": "rs-status",
                "default": ""
            },
            {
                "name": "x-cs-app-category",
                "source": "x-cs-app-category",
                "default": ""
            },
            {
                "name": "x-cs-app-cci",
                "source": "x-cs-app-cci",
                "default": ""
            },
            {
                "name": "x-cs-app-ccl",
                "source": "x-cs-app-ccl",
                "default": ""
            },
            {
                "name": "x-cs-app-tags",
                "source": "x-cs-app-tags",
                "default": ""
            },
            {
                "name": "x-cs-app-suite",
                "source": "x-cs-app-suite",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-id",
                "source": "x-cs-app-instance-id",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-name",
                "source": "x-cs-app-instance-name",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-tag",
                "source": "x-cs-app-instance-tag",
                "default": ""
            },
            {
                "name": "x-cs-app-activity",
                "source": "x-cs-app-activity",
                "default": ""
            },
            {
                "name": "x-cs-app-from-user",
                "source": "x-cs-app-from-user",
                "default": ""
            },
            {
                "name": "x-cs-app-to-user",
                "source": "x-cs-app-to-user",
                "default": ""
            },
            {
                "name": "x-cs-app-object-type",
                "source": "x-cs-app-object-type",
                "default": ""
            },
            {
                "name": "x-cs-app-object-name",
                "source": "x-cs-app-object-name",
                "default": ""
            },
            {
                "name": "x-cs-app-object-id",
                "source": "x-cs-app-object-id",
                "default": ""
            },
            {
                "name": "x-rs-file-type",
                "source": "x-rs-file-type",
                "default": ""
            },
            {
                "name": "x-rs-file-category",
                "source": "x-rs-file-category",
                "default": ""
            },
            {
                "name": "x-rs-file-language",
                "source": "x-rs-file-language",
                "default": ""
            },
            {
                "name": "x-rs-file-size",
                "source": "x-rs-file-size",
                "default": ""
            },
            {
                "name": "x-rs-file-md5",
                "source": "x-rs-file-md5",
                "default": ""
            },
            {
                "name": "x-rs-file-sha256",
                "source": "x-rs-file-sha256",
                "default": ""
            },
            {
                "name": "x-error",
                "source": "x-error",
                "default": ""
            },
            {
                "name": "x-c-local-time",
                "source": "x-c-local-time",
                "default": ""
            },
            {
                "name": "x-policy-action",
                "source": "x-policy-action",
                "default": ""
            },
            {
                "name": "x-policy-name",
                "source": "x-policy-name",
                "default": ""
            },
            {
                "name": "x-policy-src-ip",
                "source": "x-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-ip",
                "source": "x-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-host",
                "source": "x-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-policy-dst-host-source",
                "source": "x-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-policy-justification-type",
                "source": "x-policy-justification-type",
                "default": ""
            },
            {
                "name": "x-policy-justification-reason",
                "source": "x-policy-justification-reason",
                "default": ""
            },
            {
                "name": "x-sc-notification-name",
                "source": "x-sc-notification-name",
                "default": ""
            },
            {
                "name": "sr-bytes",
                "source": "sr-bytes",
                "default": ""
            },
            {
                "name": "rs-bytes",
                "source": "rs-bytes",
                "default": ""
            },
            {
                "name": "x-action",
                "source": "x-action",
                "default": ""
            },
            {
                "name": "x-action-reason",
                "source": "x-action-reason",
                "default": ""
            },
            {
                "name": "x-c-authn-user",
                "source": "x-c-authn-user",
                "default": ""
            },
            {
                "name": "x-c-authn-source",
                "source": "x-c-authn-source",
                "default": ""
            },
            {
                "name": "x-c-authn-surrogate",
                "source": "x-c-authn-surrogate",
                "default": ""
            },
            {
                "name": "x-c-authn-surrogate-status",
                "source": "x-c-authn-surrogate-status",
                "default": ""
            },
            {
                "name": "x-c-authz-groups",
                "source": "x-c-authz-groups",
                "default": ""
            },
            {
                "name": "x-c-authz-ou",
                "source": "x-c-authz-ou",
                "default": ""
            },
            {
                "name": "x-cs-xau",
                "source": "x-cs-xau",
                "default": ""
            },
            {
                "name": "x-cs-connect-xau",
                "source": "x-cs-connect-xau",
                "default": ""
            },
            {
                "name": "x-c-user-confidence-index",
                "source": "x-c-user-confidence-index",
                "default": ""
            },
            {
                "name": "x-c-hostname",
                "source": "x-c-hostname",
                "default": ""
            },
            {
                "name": "x-c-device-uid",
                "source": "x-c-device-uid",
                "default": ""
            },
            {
                "name": "x-c-os-family",
                "source": "x-c-os-family",
                "default": ""
            },
            {
                "name": "x-c-os-version",
                "source": "x-c-os-version",
                "default": ""
            },
            {
                "name": "x-c-nsclient-version",
                "source": "x-c-nsclient-version",
                "default": ""
            },
            {
                "name": "x-c-nsclient-client-profile",
                "source": "x-c-nsclient-client-profile",
                "default": ""
            },
            {
                "name": "x-c-nsclient-steering-profile",
                "source": "x-c-nsclient-steering-profile",
                "default": ""
            },
            {
                "name": "x-c-device-classification",
                "source": "x-c-device-classification",
                "default": ""
            },
            {
                "name": "x-cs-nsclient-tunnel-type",
                "source": "x-cs-nsclient-tunnel-type",
                "default": ""
            },
            {
                "name": "x-cs-process",
                "source": "x-cs-process",
                "default": ""
            },
            {
                "name": "x-cs-pid",
                "source": "x-cs-pid",
                "default": ""
            },
            {
                "name": "x-cs-parent-process",
                "source": "x-cs-parent-process",
                "default": ""
            },
            {
                "name": "x-cs-ppid",
                "source": "x-cs-ppid",
                "default": ""
            },
            {
                "name": "x-tp-result",
                "source": "x-tp-result",
                "default": ""
            },
            {
                "name": "x-tp-engine",
                "source": "x-tp-engine",
                "default": ""
            },
            {
                "name": "x-tp-malware-name",
                "source": "x-tp-malware-name",
                "default": ""
            },
            {
                "name": "x-tp-severity",
                "source": "x-tp-severity",
                "default": ""
            },
            {
                "name": "x-sr-forward-dest",
                "source": "x-sr-forward-dest",
                "default": ""
            },
            {
                "name": "x-ssl-policy-issuer",
                "source": "x-ssl-policy-issuer",
                "default": ""
            },
            {
                "name": "x-eip-policy-name",
                "source": "x-eip-policy-name",
                "default": ""
            },
            {
                "name": "x-eip-policy-footprint",
                "source": "x-eip-policy-footprint",
                "default": ""
            },
            {
                "name": "x-policy-categories",
                "source": "x-policy-categories",
                "default": ""
            },
            {
                "name": "x-c-timezone",
                "source": "x-c-timezone",
                "default": ""
            },
            {
                "name": "x-support",
                "source": "x-support",
                "default": ""
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
CEF Native Format 1 to Format 4
Those configurations are providing mapping for legacy Format 1 to Format 4 field list in CEF format without any field rename.
Sample Format 1 CEF Native
{
    "name": "Sample Format 1 CEF native",
    "description": "From Online Help, Transaction Event Format 1 in CEF, fields not renamed",
    "type": "CEF",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            }
        ],
        "header":
        [
            {
                "name": "device_vendor",
                "source": "",
                "default": "Netskope"
            },
            {
                "name": "device_product",
                "source": "",
                "default": "WebTX"
            },
            {
                "name": "device_version",
                "source": "",
                "default": "NULL"
            },
            {
                "name": "signature_id",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "name",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "severity",
                "source": "",
                "default": "Unknown"
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
Sample Format 2 CEF Native
{
    "name": "Sample Format 2 CEF native",
    "description": "From Online Help, Transaction Event Format 2 in CEF, fields not renamed",
    "type": "CEF",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            }
        ],
        "header":
        [
            {
                "name": "device_vendor",
                "source": "",
                "default": "Netskope"
            },
            {
                "name": "device_product",
                "source": "",
                "default": "WebTX"
            },
            {
                "name": "device_version",
                "source": "",
                "default": "NULL"
            },
            {
                "name": "signature_id",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "name",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "severity",
                "source": "",
                "default": "Unknown"
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
Sample Format 3 CEF Native
{
    "name": "Sample Format 3 CEF native",
    "description": "From Online Help, Transaction Event Format 3 in CEF, fields not renamed",
    "type": "CEF",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            },
            {
                "name": "x-s-dp-name",
                "source": "x-s-dp-name",
                "default": ""
            },
            {
                "name": "x-cs-src-ip",
                "source": "x-cs-src-ip",
                "default": ""
            },
            {
                "name": "x-cs-src-port",
                "source": "x-cs-src-port",
                "default": ""
            },
            {
                "name": "x-cs-dst-ip",
                "source": "x-cs-dst-ip",
                "default": ""
            },
            {
                "name": "x-cs-dst-port",
                "source": "x-cs-dst-port",
                "default": ""
            },
            {
                "name": "x-sr-src-ip",
                "source": "x-sr-src-ip",
                "default": ""
            },
            {
                "name": "x-sr-src-port",
                "source": "x-sr-src-port",
                "default": ""
            },
            {
                "name": "x-sr-dst-ip",
                "source": "x-sr-dst-ip",
                "default": ""
            },
            {
                "name": "x-sr-dst-port",
                "source": "x-sr-dst-port",
                "default": ""
            },
            {
                "name": "x-cs-ip-connect-xff",
                "source": "x-cs-ip-connect-xff",
                "default": ""
            },
            {
                "name": "x-cs-ip-xff",
                "source": "x-cs-ip-xff",
                "default": ""
            },
            {
                "name": "x-cs-connect-host",
                "source": "x-cs-connect-host",
                "default": ""
            },
            {
                "name": "x-cs-connect-port",
                "source": "x-cs-connect-port",
                "default": ""
            },
            {
                "name": "x-cs-connect-user-agent",
                "source": "x-cs-connect-user-agent",
                "default": ""
            },
            {
                "name": "x-cs-url",
                "source": "x-cs-url",
                "default": ""
            },
            {
                "name": "x-cs-uri-path",
                "source": "x-cs-uri-path",
                "default": ""
            },
            {
                "name": "x-cs-http-version",
                "source": "x-cs-http-version",
                "default": ""
            },
            {
                "name": "rs-status",
                "source": "rs-status",
                "default": ""
            },
            {
                "name": "x-cs-app-category",
                "source": "x-cs-app-category",
                "default": ""
            },
            {
                "name": "x-cs-app-cci",
                "source": "x-cs-app-cci",
                "default": ""
            },
            {
                "name": "x-cs-app-ccl",
                "source": "x-cs-app-ccl",
                "default": ""
            },
            {
                "name": "x-cs-app-tags",
                "source": "x-cs-app-tags",
                "default": ""
            },
            {
                "name": "x-cs-app-suite",
                "source": "x-cs-app-suite",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-id",
                "source": "x-cs-app-instance-id",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-name",
                "source": "x-cs-app-instance-name",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-tag",
                "source": "x-cs-app-instance-tag",
                "default": ""
            },
            {
                "name": "x-cs-app-activity",
                "source": "x-cs-app-activity",
                "default": ""
            },
            {
                "name": "x-cs-app-from-user",
                "source": "x-cs-app-from-user",
                "default": ""
            },
            {
                "name": "x-cs-app-to-user",
                "source": "x-cs-app-to-user",
                "default": ""
            },
            {
                "name": "x-cs-app-object-type",
                "source": "x-cs-app-object-type",
                "default": ""
            },
            {
                "name": "x-cs-app-object-name",
                "source": "x-cs-app-object-name",
                "default": ""
            },
            {
                "name": "x-cs-app-object-id",
                "source": "x-cs-app-object-id",
                "default": ""
            },
            {
                "name": "x-rs-file-type",
                "source": "x-rs-file-type",
                "default": ""
            },
            {
                "name": "x-rs-file-category",
                "source": "x-rs-file-category",
                "default": ""
            },
            {
                "name": "x-rs-file-language",
                "source": "x-rs-file-language",
                "default": ""
            },
            {
                "name": "x-rs-file-size",
                "source": "x-rs-file-size",
                "default": ""
            },
            {
                "name": "x-rs-file-md5",
                "source": "x-rs-file-md5",
                "default": ""
            },
            {
                "name": "x-rs-file-sha256",
                "source": "x-rs-file-sha256",
                "default": ""
            },
            {
                "name": "x-error",
                "source": "x-error",
                "default": ""
            },
            {
                "name": "x-c-local-time",
                "source": "x-c-local-time",
                "default": ""
            },
            {
                "name": "x-policy-action",
                "source": "x-policy-action",
                "default": ""
            },
            {
                "name": "x-policy-name",
                "source": "x-policy-name",
                "default": ""
            },
            {
                "name": "x-policy-src-ip",
                "source": "x-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-ip",
                "source": "x-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-host",
                "source": "x-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-policy-dst-host-source",
                "source": "x-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-policy-justification-type",
                "source": "x-policy-justification-type",
                "default": ""
            },
            {
                "name": "x-policy-justification-reason",
                "source": "x-policy-justification-reason",
                "default": ""
            },
            {
                "name": "x-sc-notification-name",
                "source": "x-sc-notification-name",
                "default": ""
            }
        ],
        "header":
        [
            {
                "name": "device_vendor",
                "source": "",
                "default": "Netskope"
            },
            {
                "name": "device_product",
                "source": "",
                "default": "WebTX"
            },
            {
                "name": "device_version",
                "source": "",
                "default": "NULL"
            },
            {
                "name": "signature_id",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "name",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "severity",
                "source": "",
                "default": "Unknown"
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
Sample Format 4 CEF Native
{
    "name": "Sample Format 4 CEF native",
    "description": "From Online Help, Transaction Event Format 4 in CEF, fields not renamed",
    "type": "CEF",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            },
            {
                "name": "x-s-dp-name",
                "source": "x-s-dp-name",
                "default": ""
            },
            {
                "name": "x-cs-src-ip",
                "source": "x-cs-src-ip",
                "default": ""
            },
            {
                "name": "x-cs-src-port",
                "source": "x-cs-src-port",
                "default": ""
            },
            {
                "name": "x-cs-dst-ip",
                "source": "x-cs-dst-ip",
                "default": ""
            },
            {
                "name": "x-cs-dst-port",
                "source": "x-cs-dst-port",
                "default": ""
            },
            {
                "name": "x-sr-src-ip",
                "source": "x-sr-src-ip",
                "default": ""
            },
            {
                "name": "x-sr-src-port",
                "source": "x-sr-src-port",
                "default": ""
            },
            {
                "name": "x-sr-dst-ip",
                "source": "x-sr-dst-ip",
                "default": ""
            },
            {
                "name": "x-sr-dst-port",
                "source": "x-sr-dst-port",
                "default": ""
            },
            {
                "name": "x-cs-ip-connect-xff",
                "source": "x-cs-ip-connect-xff",
                "default": ""
            },
            {
                "name": "x-cs-ip-xff",
                "source": "x-cs-ip-xff",
                "default": ""
            },
            {
                "name": "x-cs-connect-host",
                "source": "x-cs-connect-host",
                "default": ""
            },
            {
                "name": "x-cs-connect-port",
                "source": "x-cs-connect-port",
                "default": ""
            },
            {
                "name": "x-cs-connect-user-agent",
                "source": "x-cs-connect-user-agent",
                "default": ""
            },
            {
                "name": "x-cs-url",
                "source": "x-cs-url",
                "default": ""
            },
            {
                "name": "x-cs-uri-path",
                "source": "x-cs-uri-path",
                "default": ""
            },
            {
                "name": "x-cs-http-version",
                "source": "x-cs-http-version",
                "default": ""
            },
            {
                "name": "rs-status",
                "source": "rs-status",
                "default": ""
            },
            {
                "name": "x-cs-app-category",
                "source": "x-cs-app-category",
                "default": ""
            },
            {
                "name": "x-cs-app-cci",
                "source": "x-cs-app-cci",
                "default": ""
            },
            {
                "name": "x-cs-app-ccl",
                "source": "x-cs-app-ccl",
                "default": ""
            },
            {
                "name": "x-cs-app-tags",
                "source": "x-cs-app-tags",
                "default": ""
            },
            {
                "name": "x-cs-app-suite",
                "source": "x-cs-app-suite",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-id",
                "source": "x-cs-app-instance-id",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-name",
                "source": "x-cs-app-instance-name",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-tag",
                "source": "x-cs-app-instance-tag",
                "default": ""
            },
            {
                "name": "x-cs-app-activity",
                "source": "x-cs-app-activity",
                "default": ""
            },
            {
                "name": "x-cs-app-from-user",
                "source": "x-cs-app-from-user",
                "default": ""
            },
            {
                "name": "x-cs-app-to-user",
                "source": "x-cs-app-to-user",
                "default": ""
            },
            {
                "name": "x-cs-app-object-type",
                "source": "x-cs-app-object-type",
                "default": ""
            },
            {
                "name": "x-cs-app-object-name",
                "source": "x-cs-app-object-name",
                "default": ""
            },
            {
                "name": "x-cs-app-object-id",
                "source": "x-cs-app-object-id",
                "default": ""
            },
            {
                "name": "x-rs-file-type",
                "source": "x-rs-file-type",
                "default": ""
            },
            {
                "name": "x-rs-file-category",
                "source": "x-rs-file-category",
                "default": ""
            },
            {
                "name": "x-rs-file-language",
                "source": "x-rs-file-language",
                "default": ""
            },
            {
                "name": "x-rs-file-size",
                "source": "x-rs-file-size",
                "default": ""
            },
            {
                "name": "x-rs-file-md5",
                "source": "x-rs-file-md5",
                "default": ""
            },
            {
                "name": "x-rs-file-sha256",
                "source": "x-rs-file-sha256",
                "default": ""
            },
            {
                "name": "x-error",
                "source": "x-error",
                "default": ""
            },
            {
                "name": "x-c-local-time",
                "source": "x-c-local-time",
                "default": ""
            },
            {
                "name": "x-policy-action",
                "source": "x-policy-action",
                "default": ""
            },
            {
                "name": "x-policy-name",
                "source": "x-policy-name",
                "default": ""
            },
            {
                "name": "x-policy-src-ip",
                "source": "x-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-ip",
                "source": "x-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-host",
                "source": "x-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-policy-dst-host-source",
                "source": "x-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-policy-justification-type",
                "source": "x-policy-justification-type",
                "default": ""
            },
            {
                "name": "x-policy-justification-reason",
                "source": "x-policy-justification-reason",
                "default": ""
            },
            {
                "name": "x-sc-notification-name",
                "source": "x-sc-notification-name",
                "default": ""
            },
            {
                "name": "sr-bytes",
                "source": "sr-bytes",
                "default": ""
            },
            {
                "name": "rs-bytes",
                "source": "rs-bytes",
                "default": ""
            },
            {
                "name": "x-action",
                "source": "x-action",
                "default": ""
            },
            {
                "name": "x-action-reason",
                "source": "x-action-reason",
                "default": ""
            },
            {
                "name": "x-c-authn-user",
                "source": "x-c-authn-user",
                "default": ""
            },
            {
                "name": "x-c-authn-source",
                "source": "x-c-authn-source",
                "default": ""
            },
            {
                "name": "x-c-authn-surrogate",
                "source": "x-c-authn-surrogate",
                "default": ""
            },
            {
                "name": "x-c-authn-surrogate-status",
                "source": "x-c-authn-surrogate-status",
                "default": ""
            },
            {
                "name": "x-c-authz-groups",
                "source": "x-c-authz-groups",
                "default": ""
            },
            {
                "name": "x-c-authz-ou",
                "source": "x-c-authz-ou",
                "default": ""
            },
            {
                "name": "x-cs-xau",
                "source": "x-cs-xau",
                "default": ""
            },
            {
                "name": "x-cs-connect-xau",
                "source": "x-cs-connect-xau",
                "default": ""
            },
            {
                "name": "x-c-user-confidence-index",
                "source": "x-c-user-confidence-index",
                "default": ""
            },
            {
                "name": "x-c-hostname",
                "source": "x-c-hostname",
                "default": ""
            },
            {
                "name": "x-c-device-uid",
                "source": "x-c-device-uid",
                "default": ""
            },
            {
                "name": "x-c-os-family",
                "source": "x-c-os-family",
                "default": ""
            },
            {
                "name": "x-c-os-version",
                "source": "x-c-os-version",
                "default": ""
            },
            {
                "name": "x-c-nsclient-version",
                "source": "x-c-nsclient-version",
                "default": ""
            },
            {
                "name": "x-c-nsclient-client-profile",
                "source": "x-c-nsclient-client-profile",
                "default": ""
            },
            {
                "name": "x-c-nsclient-steering-profile",
                "source": "x-c-nsclient-steering-profile",
                "default": ""
            },
            {
                "name": "x-c-device-classification",
                "source": "x-c-device-classification",
                "default": ""
            },
            {
                "name": "x-cs-nsclient-tunnel-type",
                "source": "x-cs-nsclient-tunnel-type",
                "default": ""
            },
            {
                "name": "x-cs-process",
                "source": "x-cs-process",
                "default": ""
            },
            {
                "name": "x-cs-pid",
                "source": "x-cs-pid",
                "default": ""
            },
            {
                "name": "x-cs-parent-process",
                "source": "x-cs-parent-process",
                "default": ""
            },
            {
                "name": "x-cs-ppid",
                "source": "x-cs-ppid",
                "default": ""
            },
            {
                "name": "x-tp-result",
                "source": "x-tp-result",
                "default": ""
            },
            {
                "name": "x-tp-engine",
                "source": "x-tp-engine",
                "default": ""
            },
            {
                "name": "x-tp-malware-name",
                "source": "x-tp-malware-name",
                "default": ""
            },
            {
                "name": "x-tp-severity",
                "source": "x-tp-severity",
                "default": ""
            },
            {
                "name": "x-sr-forward-dest",
                "source": "x-sr-forward-dest",
                "default": ""
            },
            {
                "name": "x-ssl-policy-issuer",
                "source": "x-ssl-policy-issuer",
                "default": ""
            },
            {
                "name": "x-eip-policy-name",
                "source": "x-eip-policy-name",
                "default": ""
            },
            {
                "name": "x-eip-policy-footprint",
                "source": "x-eip-policy-footprint",
                "default": ""
            },
            {
                "name": "x-policy-categories",
                "source": "x-policy-categories",
                "default": ""
            },
            {
                "name": "x-c-timezone",
                "source": "x-c-timezone",
                "default": ""
            },
            {
                "name": "x-support",
                "source": "x-support",
                "default": ""
            }
        ],
        "header":
        [
            {
                "name": "device_vendor",
                "source": "",
                "default": "Netskope"
            },
            {
                "name": "device_product",
                "source": "",
                "default": "WebTX"
            },
            {
                "name": "device_version",
                "source": "",
                "default": "NULL"
            },
            {
                "name": "signature_id",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "name",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "severity",
                "source": "",
                "default": "Unknown"
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
CEF Cloud Exchange Format 3
This configuration reproduces the default mapping for Cloud Exchange.
Sample Format 3 CEF CLS
{
    "name": "Sample Format 3 CEF CLS",
    "description": "From Online Help, Transaction Event Format 3 in CEF, field mapping with Cloud Exchange default syslog mapping",
    "type": "CEF",
    "definition":
    {
        "remove_empty_fields": true,
        "customize": true,
        "custom_fields":
        [
            {
                "name": "NetskopeJustificationReason",
                "source": "x-policy-justification-reason",
                "default": ""
            },
            {
                "name": "NetskopeJustificationType",
                "source": "x-policy-justification-type",
                "default": ""
            },
            {
                "name": "act",
                "source": "x-policy-action",
                "default": ""
            },
            {
                "name": "app",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cat",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "cn1",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cn1Label",
                "source": "",
                "default": "time-taken"
            },
            {
                "name": "cn2",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "cn2Label",
                "source": "",
                "default": "bytes"
            },
            {
                "name": "cn3",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "cn3Label",
                "source": "",
                "default": "transaction-id"
            },
            {
                "name": "cs1",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs1Label",
                "source": "",
                "default": "uri-query"
            },
            {
                "name": "cs2",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "cs2Label",
                "source": "",
                "default": "content-type"
            },
            {
                "name": "cs3",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "cs3Label",
                "source": "",
                "default": "client-device"
            },
            {
                "name": "cs4",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "cs4Label",
                "source": "",
                "default": "other-category"
            },
            {
                "name": "cs5",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "cs5Label",
                "source": "",
                "default": "server-ssl-error"
            },
            {
                "name": "cs6",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "cs6Label",
                "source": "",
                "default": "client-ssl-err"
            },
            {
                "name": "destinationTranslatedPort",
                "source": "x-cs-connect-port",
                "default": ""
            },
            {
                "name": "deviceCustomDate1",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "deviceCustomDate1Label",
                "source": "",
                "default": "x-cs-timestamp"
            },
            {
                "name": "deviceDnsDomain",
                "source": "x-cs-app-instance-id",
                "default": ""
            },
            {
                "name": "devicePayloadId",
                "source": "x-cs-app-object-id",
                "default": ""
            },
            {
                "name": "dhost",
                "source": "x-policy-dst-host",
                "default": ""
            },
            {
                "name": "dlat",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "dlong",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "dpt",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "dst",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "duid",
                "source": "x-cs-app-from-user",
                "default": ""
            },
            {
                "name": "duser",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "dvchost",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "fileHash",
                "source": "x-rs-file-md5",
                "default": ""
            },
            {
                "name": "fileType",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "flexString1",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "flexString1Label",
                "source": "",
                "default": "client-site"
            },
            {
                "name": "flexString2",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "flexString2Label",
                "source": "",
                "default": "type"
            },
            {
                "name": "fname",
                "source": "x-cs-app-object-name",
                "default": ""
            },
            {
                "name": "in",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "out",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "reason",
                "source": "x-error",
                "default": ""
            },
            {
                "name": "request",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "requestClientApplication",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "requestContext",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "requestMethod",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "shost",
                "source": "x-cs-connect-host",
                "default": ""
            },
            {
                "name": "slat",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "slong",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "sourceDnsDomain",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "sourceServiceName",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "sourceTranslatedAddress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            },
            {
                "name": "sproc",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "spt",
                "source": "x-cs-src-port",
                "default": ""
            },
            {
                "name": "src",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "suser",
                "source": "x-cs-app-to-user",
                "default": ""
            }
        ],
        "header":
        [
            {
                "name": "device_vendor",
                "source": "",
                "default": "Netskope"
            },
            {
                "name": "device_product",
                "source": "",
                "default": "WebTX"
            },
            {
                "name": "device_version",
                "source": "",
                "default": "NULL"
            },
            {
                "name": "signature_id",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "name",
                "source": "",
                "default": "webtx"
            },
            {
                "name": "severity",
                "source": "",
                "default": "Unknown"
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
ELFF Format 1 to Format 4
Those configurations provide a mapping for legacy Format 1 to Format 4 field lists in ELFF format, this reproduces previous SplunkTA event.
Sample Format 1 ELFF
{
    "name": "Sample Format 1 ELFF",
    "description": "From Online Help, Transaction Event Format 1 in ELFF, Splunk TA migration",
    "type": "ELFF",
    "definition":
    {
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
Sample Format 2 ELFF
{
    "name": "Sample Format 2 ELFF",
    "description": "From Online Help, Transaction Event Format 2 in ELFF, Splunk TA migration",
    "type": "ELFF",
    "definition":
    {
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
Sample Format 3 ELFF
{
    "name": "Sample Format 3 ELFF",
    "description": "From Online Help, Transaction Event Format 3 in ELFF, Splunk TA migration",
    "type": "ELFF",
    "definition":
    {
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            },
            {
                "name": "x-s-dp-name",
                "source": "x-s-dp-name",
                "default": ""
            },
            {
                "name": "x-cs-src-ip",
                "source": "x-cs-src-ip",
                "default": ""
            },
            {
                "name": "x-cs-src-port",
                "source": "x-cs-src-port",
                "default": ""
            },
            {
                "name": "x-cs-dst-ip",
                "source": "x-cs-dst-ip",
                "default": ""
            },
            {
                "name": "x-cs-dst-port",
                "source": "x-cs-dst-port",
                "default": ""
            },
            {
                "name": "x-sr-src-ip",
                "source": "x-sr-src-ip",
                "default": ""
            },
            {
                "name": "x-sr-src-port",
                "source": "x-sr-src-port",
                "default": ""
            },
            {
                "name": "x-sr-dst-ip",
                "source": "x-sr-dst-ip",
                "default": ""
            },
            {
                "name": "x-sr-dst-port",
                "source": "x-sr-dst-port",
                "default": ""
            },
            {
                "name": "x-cs-ip-connect-xff",
                "source": "x-cs-ip-connect-xff",
                "default": ""
            },
            {
                "name": "x-cs-ip-xff",
                "source": "x-cs-ip-xff",
                "default": ""
            },
            {
                "name": "x-cs-connect-host",
                "source": "x-cs-connect-host",
                "default": ""
            },
            {
                "name": "x-cs-connect-port",
                "source": "x-cs-connect-port",
                "default": ""
            },
            {
                "name": "x-cs-connect-user-agent",
                "source": "x-cs-connect-user-agent",
                "default": ""
            },
            {
                "name": "x-cs-url",
                "source": "x-cs-url",
                "default": ""
            },
            {
                "name": "x-cs-uri-path",
                "source": "x-cs-uri-path",
                "default": ""
            },
            {
                "name": "x-cs-http-version",
                "source": "x-cs-http-version",
                "default": ""
            },
            {
                "name": "rs-status",
                "source": "rs-status",
                "default": ""
            },
            {
                "name": "x-cs-app-category",
                "source": "x-cs-app-category",
                "default": ""
            },
            {
                "name": "x-cs-app-cci",
                "source": "x-cs-app-cci",
                "default": ""
            },
            {
                "name": "x-cs-app-ccl",
                "source": "x-cs-app-ccl",
                "default": ""
            },
            {
                "name": "x-cs-app-tags",
                "source": "x-cs-app-tags",
                "default": ""
            },
            {
                "name": "x-cs-app-suite",
                "source": "x-cs-app-suite",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-id",
                "source": "x-cs-app-instance-id",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-name",
                "source": "x-cs-app-instance-name",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-tag",
                "source": "x-cs-app-instance-tag",
                "default": ""
            },
            {
                "name": "x-cs-app-activity",
                "source": "x-cs-app-activity",
                "default": ""
            },
            {
                "name": "x-cs-app-from-user",
                "source": "x-cs-app-from-user",
                "default": ""
            },
            {
                "name": "x-cs-app-to-user",
                "source": "x-cs-app-to-user",
                "default": ""
            },
            {
                "name": "x-cs-app-object-type",
                "source": "x-cs-app-object-type",
                "default": ""
            },
            {
                "name": "x-cs-app-object-name",
                "source": "x-cs-app-object-name",
                "default": ""
            },
            {
                "name": "x-cs-app-object-id",
                "source": "x-cs-app-object-id",
                "default": ""
            },
            {
                "name": "x-rs-file-type",
                "source": "x-rs-file-type",
                "default": ""
            },
            {
                "name": "x-rs-file-category",
                "source": "x-rs-file-category",
                "default": ""
            },
            {
                "name": "x-rs-file-language",
                "source": "x-rs-file-language",
                "default": ""
            },
            {
                "name": "x-rs-file-size",
                "source": "x-rs-file-size",
                "default": ""
            },
            {
                "name": "x-rs-file-md5",
                "source": "x-rs-file-md5",
                "default": ""
            },
            {
                "name": "x-rs-file-sha256",
                "source": "x-rs-file-sha256",
                "default": ""
            },
            {
                "name": "x-error",
                "source": "x-error",
                "default": ""
            },
            {
                "name": "x-c-local-time",
                "source": "x-c-local-time",
                "default": ""
            },
            {
                "name": "x-policy-action",
                "source": "x-policy-action",
                "default": ""
            },
            {
                "name": "x-policy-name",
                "source": "x-policy-name",
                "default": ""
            },
            {
                "name": "x-policy-src-ip",
                "source": "x-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-ip",
                "source": "x-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-host",
                "source": "x-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-policy-dst-host-source",
                "source": "x-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-policy-justification-type",
                "source": "x-policy-justification-type",
                "default": ""
            },
            {
                "name": "x-policy-justification-reason",
                "source": "x-policy-justification-reason",
                "default": ""
            },
            {
                "name": "x-sc-notification-name",
                "source": "x-sc-notification-name",
                "default": ""
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
Sample Format 4 ELFF
{
    "name": "Sample Format 4 ELFF",
    "description": "From Online Help, Transaction Event Format 4 in ELFF, Splunk TA migration",
    "type": "ELFF",
    "definition":
    {
        "customize": true,
        "custom_fields":
        [
            {
                "name": "date",
                "source": "date",
                "default": ""
            },
            {
                "name": "time",
                "source": "time",
                "default": ""
            },
            {
                "name": "time-taken",
                "source": "time-taken",
                "default": ""
            },
            {
                "name": "cs-bytes",
                "source": "cs-bytes",
                "default": ""
            },
            {
                "name": "sc-bytes",
                "source": "sc-bytes",
                "default": ""
            },
            {
                "name": "bytes",
                "source": "bytes",
                "default": ""
            },
            {
                "name": "c-ip",
                "source": "c-ip",
                "default": ""
            },
            {
                "name": "s-ip",
                "source": "s-ip",
                "default": ""
            },
            {
                "name": "cs-username",
                "source": "cs-username",
                "default": ""
            },
            {
                "name": "cs-method",
                "source": "cs-method",
                "default": ""
            },
            {
                "name": "cs-uri-scheme",
                "source": "cs-uri-scheme",
                "default": ""
            },
            {
                "name": "cs-uri-query",
                "source": "cs-uri-query",
                "default": ""
            },
            {
                "name": "cs-user-agent",
                "source": "cs-user-agent",
                "default": ""
            },
            {
                "name": "cs-content-type",
                "source": "cs-content-type",
                "default": ""
            },
            {
                "name": "sc-status",
                "source": "sc-status",
                "default": ""
            },
            {
                "name": "sc-content-type",
                "source": "sc-content-type",
                "default": ""
            },
            {
                "name": "cs-dns",
                "source": "cs-dns",
                "default": ""
            },
            {
                "name": "cs-host",
                "source": "cs-host",
                "default": ""
            },
            {
                "name": "cs-uri",
                "source": "cs-uri",
                "default": ""
            },
            {
                "name": "cs-uri-port",
                "source": "cs-uri-port",
                "default": ""
            },
            {
                "name": "cs-referer",
                "source": "cs-referer",
                "default": ""
            },
            {
                "name": "x-cs-session-id",
                "source": "x-cs-session-id",
                "default": ""
            },
            {
                "name": "x-cs-access-method",
                "source": "x-cs-access-method",
                "default": ""
            },
            {
                "name": "x-cs-app",
                "source": "x-cs-app",
                "default": ""
            },
            {
                "name": "x-s-country",
                "source": "x-s-country",
                "default": ""
            },
            {
                "name": "x-s-latitude",
                "source": "x-s-latitude",
                "default": ""
            },
            {
                "name": "x-s-longitude",
                "source": "x-s-longitude",
                "default": ""
            },
            {
                "name": "x-s-location",
                "source": "x-s-location",
                "default": ""
            },
            {
                "name": "x-s-region",
                "source": "x-s-region",
                "default": ""
            },
            {
                "name": "x-s-zipcode",
                "source": "x-s-zipcode",
                "default": ""
            },
            {
                "name": "x-c-country",
                "source": "x-c-country",
                "default": ""
            },
            {
                "name": "x-c-latitude",
                "source": "x-c-latitude",
                "default": ""
            },
            {
                "name": "x-c-longitude",
                "source": "x-c-longitude",
                "default": ""
            },
            {
                "name": "x-c-location",
                "source": "x-c-location",
                "default": ""
            },
            {
                "name": "x-c-region",
                "source": "x-c-region",
                "default": ""
            },
            {
                "name": "x-c-zipcode",
                "source": "x-c-zipcode",
                "default": ""
            },
            {
                "name": "x-c-os",
                "source": "x-c-os",
                "default": ""
            },
            {
                "name": "x-c-browser",
                "source": "x-c-browser",
                "default": ""
            },
            {
                "name": "x-c-browser-version",
                "source": "x-c-browser-version",
                "default": ""
            },
            {
                "name": "x-c-device",
                "source": "x-c-device",
                "default": ""
            },
            {
                "name": "x-cs-site",
                "source": "x-cs-site",
                "default": ""
            },
            {
                "name": "x-cs-timestamp",
                "source": "x-cs-timestamp",
                "default": ""
            },
            {
                "name": "x-cs-page-id",
                "source": "x-cs-page-id",
                "default": ""
            },
            {
                "name": "x-cs-userip",
                "source": "x-cs-userip",
                "default": ""
            },
            {
                "name": "x-cs-traffic-type",
                "source": "x-cs-traffic-type",
                "default": ""
            },
            {
                "name": "x-cs-tunnel-id",
                "source": "x-cs-tunnel-id",
                "default": ""
            },
            {
                "name": "x-category",
                "source": "x-category",
                "default": ""
            },
            {
                "name": "x-other-category",
                "source": "x-other-category",
                "default": ""
            },
            {
                "name": "x-type",
                "source": "x-type",
                "default": ""
            },
            {
                "name": "x-server-ssl-err",
                "source": "x-server-ssl-err",
                "default": ""
            },
            {
                "name": "x-client-ssl-err",
                "source": "x-client-ssl-err",
                "default": ""
            },
            {
                "name": "x-transaction-id",
                "source": "x-transaction-id",
                "default": ""
            },
            {
                "name": "x-request-id",
                "source": "x-request-id",
                "default": ""
            },
            {
                "name": "x-cs-sni",
                "source": "x-cs-sni",
                "default": ""
            },
            {
                "name": "x-cs-domain-fronted-sni",
                "source": "x-cs-domain-fronted-sni",
                "default": ""
            },
            {
                "name": "x-category-id",
                "source": "x-category-id",
                "default": ""
            },
            {
                "name": "x-other-category-id",
                "source": "x-other-category-id",
                "default": ""
            },
            {
                "name": "x-sr-headers-name",
                "source": "x-sr-headers-name",
                "default": ""
            },
            {
                "name": "x-sr-headers-value",
                "source": "x-sr-headers-value",
                "default": ""
            },
            {
                "name": "x-cs-ssl-ja3",
                "source": "x-cs-ssl-ja3",
                "default": ""
            },
            {
                "name": "x-sr-ssl-ja3s",
                "source": "x-sr-ssl-ja3s",
                "default": ""
            },
            {
                "name": "x-ssl-bypass",
                "source": "x-ssl-bypass",
                "default": ""
            },
            {
                "name": "x-ssl-bypass-reason",
                "source": "x-ssl-bypass-reason",
                "default": ""
            },
            {
                "name": "x-r-cert-subject-cn",
                "source": "x-r-cert-subject-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-issuer-cn",
                "source": "x-r-cert-issuer-cn",
                "default": ""
            },
            {
                "name": "x-r-cert-startdate",
                "source": "x-r-cert-startdate",
                "default": ""
            },
            {
                "name": "x-r-cert-enddate",
                "source": "x-r-cert-enddate",
                "default": ""
            },
            {
                "name": "x-r-cert-valid",
                "source": "x-r-cert-valid",
                "default": ""
            },
            {
                "name": "x-r-cert-expired",
                "source": "x-r-cert-expired",
                "default": ""
            },
            {
                "name": "x-r-cert-untrusted-root",
                "source": "x-r-cert-untrusted-root",
                "default": ""
            },
            {
                "name": "x-r-cert-incomplete-chain",
                "source": "x-r-cert-incomplete-chain",
                "default": ""
            },
            {
                "name": "x-r-cert-self-signed",
                "source": "x-r-cert-self-signed",
                "default": ""
            },
            {
                "name": "x-r-cert-revoked",
                "source": "x-r-cert-revoked",
                "default": ""
            },
            {
                "name": "x-r-cert-revocation-check",
                "source": "x-r-cert-revocation-check",
                "default": ""
            },
            {
                "name": "x-r-cert-mismatch",
                "source": "x-r-cert-mismatch",
                "default": ""
            },
            {
                "name": "x-cs-ssl-fronting-error",
                "source": "x-cs-ssl-fronting-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-handshake-error",
                "source": "x-cs-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-handshake-error",
                "source": "x-sr-ssl-handshake-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-client-certificate-error",
                "source": "x-sr-ssl-client-certificate-error",
                "default": ""
            },
            {
                "name": "x-sr-ssl-malformed-ssl",
                "source": "x-sr-ssl-malformed-ssl",
                "default": ""
            },
            {
                "name": "x-s-custom-signing-ca-error",
                "source": "x-s-custom-signing-ca-error",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action",
                "source": "x-cs-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-cs-ssl-engine-action-reason",
                "source": "x-cs-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action",
                "source": "x-sr-ssl-engine-action",
                "default": ""
            },
            {
                "name": "x-sr-ssl-engine-action-reason",
                "source": "x-sr-ssl-engine-action-reason",
                "default": ""
            },
            {
                "name": "x-ssl-policy-src-ip",
                "source": "x-ssl-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-ip",
                "source": "x-ssl-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host",
                "source": "x-ssl-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-ssl-policy-dst-host-source",
                "source": "x-ssl-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-ssl-policy-categories",
                "source": "x-ssl-policy-categories",
                "default": ""
            },
            {
                "name": "x-ssl-policy-action",
                "source": "x-ssl-policy-action",
                "default": ""
            },
            {
                "name": "x-ssl-policy-name",
                "source": "x-ssl-policy-name",
                "default": ""
            },
            {
                "name": "x-cs-ssl-version",
                "source": "x-cs-ssl-version",
                "default": ""
            },
            {
                "name": "x-cs-ssl-cipher",
                "source": "x-cs-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-sr-ssl-version",
                "source": "x-sr-ssl-version",
                "default": ""
            },
            {
                "name": "x-sr-ssl-cipher",
                "source": "x-sr-ssl-cipher",
                "default": ""
            },
            {
                "name": "x-cs-src-ip-egress",
                "source": "x-cs-src-ip-egress",
                "default": ""
            },
            {
                "name": "x-s-dp-name",
                "source": "x-s-dp-name",
                "default": ""
            },
            {
                "name": "x-cs-src-ip",
                "source": "x-cs-src-ip",
                "default": ""
            },
            {
                "name": "x-cs-src-port",
                "source": "x-cs-src-port",
                "default": ""
            },
            {
                "name": "x-cs-dst-ip",
                "source": "x-cs-dst-ip",
                "default": ""
            },
            {
                "name": "x-cs-dst-port",
                "source": "x-cs-dst-port",
                "default": ""
            },
            {
                "name": "x-sr-src-ip",
                "source": "x-sr-src-ip",
                "default": ""
            },
            {
                "name": "x-sr-src-port",
                "source": "x-sr-src-port",
                "default": ""
            },
            {
                "name": "x-sr-dst-ip",
                "source": "x-sr-dst-ip",
                "default": ""
            },
            {
                "name": "x-sr-dst-port",
                "source": "x-sr-dst-port",
                "default": ""
            },
            {
                "name": "x-cs-ip-connect-xff",
                "source": "x-cs-ip-connect-xff",
                "default": ""
            },
            {
                "name": "x-cs-ip-xff",
                "source": "x-cs-ip-xff",
                "default": ""
            },
            {
                "name": "x-cs-connect-host",
                "source": "x-cs-connect-host",
                "default": ""
            },
            {
                "name": "x-cs-connect-port",
                "source": "x-cs-connect-port",
                "default": ""
            },
            {
                "name": "x-cs-connect-user-agent",
                "source": "x-cs-connect-user-agent",
                "default": ""
            },
            {
                "name": "x-cs-url",
                "source": "x-cs-url",
                "default": ""
            },
            {
                "name": "x-cs-uri-path",
                "source": "x-cs-uri-path",
                "default": ""
            },
            {
                "name": "x-cs-http-version",
                "source": "x-cs-http-version",
                "default": ""
            },
            {
                "name": "rs-status",
                "source": "rs-status",
                "default": ""
            },
            {
                "name": "x-cs-app-category",
                "source": "x-cs-app-category",
                "default": ""
            },
            {
                "name": "x-cs-app-cci",
                "source": "x-cs-app-cci",
                "default": ""
            },
            {
                "name": "x-cs-app-ccl",
                "source": "x-cs-app-ccl",
                "default": ""
            },
            {
                "name": "x-cs-app-tags",
                "source": "x-cs-app-tags",
                "default": ""
            },
            {
                "name": "x-cs-app-suite",
                "source": "x-cs-app-suite",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-id",
                "source": "x-cs-app-instance-id",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-name",
                "source": "x-cs-app-instance-name",
                "default": ""
            },
            {
                "name": "x-cs-app-instance-tag",
                "source": "x-cs-app-instance-tag",
                "default": ""
            },
            {
                "name": "x-cs-app-activity",
                "source": "x-cs-app-activity",
                "default": ""
            },
            {
                "name": "x-cs-app-from-user",
                "source": "x-cs-app-from-user",
                "default": ""
            },
            {
                "name": "x-cs-app-to-user",
                "source": "x-cs-app-to-user",
                "default": ""
            },
            {
                "name": "x-cs-app-object-type",
                "source": "x-cs-app-object-type",
                "default": ""
            },
            {
                "name": "x-cs-app-object-name",
                "source": "x-cs-app-object-name",
                "default": ""
            },
            {
                "name": "x-cs-app-object-id",
                "source": "x-cs-app-object-id",
                "default": ""
            },
            {
                "name": "x-rs-file-type",
                "source": "x-rs-file-type",
                "default": ""
            },
            {
                "name": "x-rs-file-category",
                "source": "x-rs-file-category",
                "default": ""
            },
            {
                "name": "x-rs-file-language",
                "source": "x-rs-file-language",
                "default": ""
            },
            {
                "name": "x-rs-file-size",
                "source": "x-rs-file-size",
                "default": ""
            },
            {
                "name": "x-rs-file-md5",
                "source": "x-rs-file-md5",
                "default": ""
            },
            {
                "name": "x-rs-file-sha256",
                "source": "x-rs-file-sha256",
                "default": ""
            },
            {
                "name": "x-error",
                "source": "x-error",
                "default": ""
            },
            {
                "name": "x-c-local-time",
                "source": "x-c-local-time",
                "default": ""
            },
            {
                "name": "x-policy-action",
                "source": "x-policy-action",
                "default": ""
            },
            {
                "name": "x-policy-name",
                "source": "x-policy-name",
                "default": ""
            },
            {
                "name": "x-policy-src-ip",
                "source": "x-policy-src-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-ip",
                "source": "x-policy-dst-ip",
                "default": ""
            },
            {
                "name": "x-policy-dst-host",
                "source": "x-policy-dst-host",
                "default": ""
            },
            {
                "name": "x-policy-dst-host-source",
                "source": "x-policy-dst-host-source",
                "default": ""
            },
            {
                "name": "x-policy-justification-type",
                "source": "x-policy-justification-type",
                "default": ""
            },
            {
                "name": "x-policy-justification-reason",
                "source": "x-policy-justification-reason",
                "default": ""
            },
            {
                "name": "x-sc-notification-name",
                "source": "x-sc-notification-name",
                "default": ""
            },
            {
                "name": "sr-bytes",
                "source": "sr-bytes",
                "default": ""
            },
            {
                "name": "rs-bytes",
                "source": "rs-bytes",
                "default": ""
            },
            {
                "name": "x-action",
                "source": "x-action",
                "default": ""
            },
            {
                "name": "x-action-reason",
                "source": "x-action-reason",
                "default": ""
            },
            {
                "name": "x-c-authn-user",
                "source": "x-c-authn-user",
                "default": ""
            },
            {
                "name": "x-c-authn-source",
                "source": "x-c-authn-source",
                "default": ""
            },
            {
                "name": "x-c-authn-surrogate",
                "source": "x-c-authn-surrogate",
                "default": ""
            },
            {
                "name": "x-c-authn-surrogate-status",
                "source": "x-c-authn-surrogate-status",
                "default": ""
            },
            {
                "name": "x-c-authz-groups",
                "source": "x-c-authz-groups",
                "default": ""
            },
            {
                "name": "x-c-authz-ou",
                "source": "x-c-authz-ou",
                "default": ""
            },
            {
                "name": "x-cs-xau",
                "source": "x-cs-xau",
                "default": ""
            },
            {
                "name": "x-cs-connect-xau",
                "source": "x-cs-connect-xau",
                "default": ""
            },
            {
                "name": "x-c-user-confidence-index",
                "source": "x-c-user-confidence-index",
                "default": ""
            },
            {
                "name": "x-c-hostname",
                "source": "x-c-hostname",
                "default": ""
            },
            {
                "name": "x-c-device-uid",
                "source": "x-c-device-uid",
                "default": ""
            },
            {
                "name": "x-c-os-family",
                "source": "x-c-os-family",
                "default": ""
            },
            {
                "name": "x-c-os-version",
                "source": "x-c-os-version",
                "default": ""
            },
            {
                "name": "x-c-nsclient-version",
                "source": "x-c-nsclient-version",
                "default": ""
            },
            {
                "name": "x-c-nsclient-client-profile",
                "source": "x-c-nsclient-client-profile",
                "default": ""
            },
            {
                "name": "x-c-nsclient-steering-profile",
                "source": "x-c-nsclient-steering-profile",
                "default": ""
            },
            {
                "name": "x-c-device-classification",
                "source": "x-c-device-classification",
                "default": ""
            },
            {
                "name": "x-cs-nsclient-tunnel-type",
                "source": "x-cs-nsclient-tunnel-type",
                "default": ""
            },
            {
                "name": "x-cs-process",
                "source": "x-cs-process",
                "default": ""
            },
            {
                "name": "x-cs-pid",
                "source": "x-cs-pid",
                "default": ""
            },
            {
                "name": "x-cs-parent-process",
                "source": "x-cs-parent-process",
                "default": ""
            },
            {
                "name": "x-cs-ppid",
                "source": "x-cs-ppid",
                "default": ""
            },
            {
                "name": "x-tp-result",
                "source": "x-tp-result",
                "default": ""
            },
            {
                "name": "x-tp-engine",
                "source": "x-tp-engine",
                "default": ""
            },
            {
                "name": "x-tp-malware-name",
                "source": "x-tp-malware-name",
                "default": ""
            },
            {
                "name": "x-tp-severity",
                "source": "x-tp-severity",
                "default": ""
            },
            {
                "name": "x-sr-forward-dest",
                "source": "x-sr-forward-dest",
                "default": ""
            },
            {
                "name": "x-ssl-policy-issuer",
                "source": "x-ssl-policy-issuer",
                "default": ""
            },
            {
                "name": "x-eip-policy-name",
                "source": "x-eip-policy-name",
                "default": ""
            },
            {
                "name": "x-eip-policy-footprint",
                "source": "x-eip-policy-footprint",
                "default": ""
            },
            {
                "name": "x-policy-categories",
                "source": "x-policy-categories",
                "default": ""
            },
            {
                "name": "x-c-timezone",
                "source": "x-c-timezone",
                "default": ""
            },
            {
                "name": "x-support",
                "source": "x-support",
                "default": ""
            }
        ],
        "syslog_header": "<%priority%>%timestamp% netskope"
    }
}
In this Topic
Event Streaming Client Format Examples

---
## Event Streaming Client API Access
**URL:** https://docs.netskope.com/en/event-streaming-client-api-access/
**Last Modified:** 2026-01-07T07:39:26+00:00
**Scraped:** 2026-06-26T09:39:16.512091+00:00

Event Streaming Client API Access - Netskope Knowledge Portal
Event Streaming Client API Access
Role and Token with RBACv3
Role and Token with RBACv2
Log to Swagger UI
Event Streaming Client configuration is only available via API. This page describe how to configure a role for the Event Streaming Client configuration.
If you need API access, please follow the steps:
Role definition
Token Creation
Log to Swagger UI
Roles and Tokens with RBACv3
Role definition in Settings > Administration > Administrators & Roles > Roles > New
Only “Administration” > “Event Streaming” permission is required:
In “Administrators”, create a new “Service Account” with the new role created:
After the “Create,” copy the token
Roles and Tokens with RBACv2
Go to Settings > Tools > Rest API v2, make sure the API is enabled:
Select “New Token” and select all the /api/v2/streamingclient and /api/v2/logstreaming endpoints:
After the “Save,” copy the token:
Log in to Swagger
Once the token is retrieved, open the Netskope Swagger API in Settings > Tools > REST API v2 > API DOCUMENTATION:
Use “Authorize” to input your token:
If the token is lost, it can be regenerated.
In this Topic
Event Streaming Client API Access

---
## Event Streaming Client Operations and Troubleshooting
**URL:** https://docs.netskope.com/en/event-streaming-client-operations-and-troubleshooting/
**Last Modified:** 2026-01-07T19:49:11+00:00
**Scraped:** 2026-06-26T09:39:17.637449+00:00

Event Streaming Client Operations and Troubleshooting - Netskope Knowledge Portal
Event Streaming Client Operations and Troubleshooting
This page provides help for operations and troubleshooting of Event Streaming Client.
Maintenance Operations
Force configuration update (which happen automatically every 2 minutes):
docker restart nsstreamingclient
Stopping all events from being sent to all SIEMs: Disable the Destination Object
Stopping one of the Streaming Client to receive and process events: Disable the Client Object
Stopping one SIEM target to receive events: Disable the relevant Destination Targets
Changing the event format: Create a new format and replace the format ID in the Destination (to have a simple rollback if needed)
Changing the protocol, the clients, the type of format: For breaking changes in production, it is recommended to create a new Destination and switch the enabled destination (both in Destination Object and Log Streaming configuration) to allow a simple rollback. Editing the active Destination is also supported.
Adding/Removing Streaming Clients: Edit the Destination object by Adding/Removing targets for permanent changes. Disabling the Client object or the Target is recommended for temporary changes.
Manual upgrade of the Event Streaming Client: run the installation script with
reinstall
option
Troubleshooting
Version Identification
Both Installer and Container have a version which can be identified:
Installer prompt the version when executed (the version starts with a
I.
like
I.2025.11.1
)
>python3 netskope_event_streamingclient_installer.py
NETSKOPE LOG STREAM CLIENT INSTALLER I.2025.11.1
Please specify an option:
1. install   - Set up and configure the container
2. reinstall - Remove and recreate the container
3. uninstall - Remove the container and cleanup
Enter option (install/reinstall/uninstall):
The container is logging the version at start and can be found with the command
docker logs nsstreamingclient 2>/dev/null |grep "client version"
(the version starts with a
C.
like
C.2025.11.1
)
Example:
# docker logs nsstreamingclient 2>/dev/null |grep "client version"
Install Log: NS Streaming client version number  : C.2025.11.1
{"level":"info","timestamp":"2025-12-03T14:23:22.389Z","caller":"log/log.go:86","msg":"NS Streaming client version number  : C.2025.11.1"}
Known Behavior
Initial configuration of Log Streaming to streaming client can take 1 hour to be effective
Verify the status returned by Log Streaming API is “Running” (after 15 minutes)
Wait max 1 hour after after the configuration
Any update of Log Streaming to another Destination ID will take 15 minutes to propagate
Troubleshooting Steps If No Logs Are Received On The SIEM
Check Docker logs and logs on disk to review messages
Verify that configuration is complete:
Log Streaming
Destination
Verify that all objects are enabled
Client
Destination
Destination targets
Verify that SIEM is configured to accept Syslog (verify TCP vs UDP) from the Event Streaming Client
Verify that requests are generated by looking at either:
Current Transaction Events log export
In Skope IT: Page Events for Inline Access Methods
Message Details
GRPC Connection Error
{"level":"info","timestamp":"2025-08-29T11:23:08.666Z","caller":"log/log.go:77","msg":"GRPC connection error, retrying","error":"rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp 31.xxx.xxx.xxx:50051: connect: connection refused\"","attempt":5}
Reason: Port 50051 is likely to be blocked by the firewall.
Container Group is Disabled
{"level":"info","timestamp":"2025-09-02T12:01:44.602Z","caller":"log/log.go:86","msg":"Container group is disabled, skipping stream creation","containerId":"0198f0"}
Event Streaming Client configuration is not complete, no event will be sent to this client.
Successful Configuration
{"level":"info","timestamp":"2025-08-29T11:25:49.060Z","caller":"log/log.go:77","msg":"Successfully registered with Proxy","groupId":"0198ebf7c785","connID":"c2a8f8e1c9c45c4f"}
{"level":"info","timestamp":"2025-08-29T11:25:49.060Z","caller":"log/log.go:77","msg":"Starting the Log streamer","containerId":"0198f545010"}
{"level":"info","timestamp":"2025-08-29T11:25:49.060Z","caller":"log/log.go:77","msg":"Starting the Log reader","groupId":"0198eb585","connID":"c2a8b651"}
Successful Log Processing
{"level":"info","timestamp":"2025-08-29T11:35:35.304Z","caller":"log/log.go:77","msg":"Start to receive file","fname":"0c3be6ff8c2f5f"}
{"level":"info","timestamp":"2025-08-29T11:35:35.493Z","caller":"log/log.go:77","msg":"Successfully processed file","fname":"0c35f","dt":28,"crt":47,"ct":135,"st":109,"t":189,"end2endMs":189,"ContainerId":"0198f544-6890","ConnectionId":"922e4f87"}
All values are in milliseconds:
dt
: decompression time
crt
: csv read time
ct
: conversion time
st
: syslog time
t
and
end2end
: end to end time
In this Topic
Event Streaming Client Operations and Troubleshooting

---
## Event Streaming Client FAQs
**URL:** https://docs.netskope.com/en/event-streaming-client-faqs/
**Last Modified:** 2026-01-07T17:42:41+00:00
**Scraped:** 2026-06-26T09:39:18.771848+00:00

Event Streaming Client FAQs - Netskope Knowledge Portal
Event Streaming Client FAQs
How quickly is my configuration change applied?
Any change on streamingclient API configuration is synchronized to clients in two minutes. However, Log Streaming initialization can take up to one hour and Log Streaming configuration changes can take up to 15 minutes.
How can I verify that my configuration is complete?
Check the following:
Log streaming is configured to “streamingclient” with correct Destination ID
Destination ID is enabled, with enabled targets
Client ID defines is Destination targets are enabled
Finally, verify the logs on the Event Streaming Client
How does High Availability work?
Cloud Architecture managed by Netskope is fully redundant with multiple nodes and multiple Internal links. Once initialized, the Cloud Infrastructure retain up to 24 hours if no SIEM can be reached
It is recommended to deploy 2 or more Event Client Streaming nodes to ensure high availability on the Customer side. All clients are receiving events in parallel.
Best practice, it is recommended to have two or more syslog targets for each Event Client Streaming nodes using syslog TCP.
For more details, review
Event Streaming Client Architecture
.
I have multiple tenants, how should I deploy Event Streaming Client?
Only one Event Streaming Client per host is currently supported. A different Linux host is required to streaming events from another server.
Does Event Streaming Client support HTTP Proxy?
Yes, HTTP Proxy support has been released. Please make sure the latest version of installation script is used to configure it.
Is port 50051 mandatory?
Yes, this port is used to download events.
In this Topic
Event Streaming Client FAQs

---
## Netskope Client for macOS
**URL:** https://docs.netskope.com/en/netskope-client-for-macos/
**Last Modified:** 2026-05-05T06:32:46+00:00
**Scraped:** 2026-06-26T09:39:33.625040+00:00

Netskope Client for macOS
This document describes the available deployment methods and user enrolment options when installing the Netskope Client on macOS devices.
Supported Versions
Refer to
Netskope Client Supported OS and Platform
for more details on the supported MacOS versions.
Download Netskope Client Packages
You can download Netskope Client installers from
Download Netskope Client and Scripts
.
Install Netskope Client
You can install Netskope Client in macOS using one of the following methods:
Email Invite
You can install Netskope Client using an email invitation sent from the Netskope Admin console. To learn more, view:
Email Invite
.
Email invites are time-bound and can be used only by the intended user.
After you receive the email:
Check your email from Netskope Onboarding and click the link for
Mac Client
.
Click
Download
. This downloads to your default location.
Click the installer file.
Administrator rights are required to unblock the Client and authorize all system prompts during installation to ensure proper functionality.
To install the software, enter device password on
Installer
pop-up and click
Install Software
.
If the admin pre-approves
Network Extension
through MDM, the Netskope Client will install and activate seamlessly once the user runs the installer.
Once the installation is complete,  click
Open System Setting
on
System Extension Blocked
pop-up.
In
System Settings
, select
Allow
under
Security
in
Privacy & Security.
Enter the device password on
Privacy & Security
pop-up > select
Modify Settings
,  and you can see the Netskope Client running on your taskbar.
Full Disk Access is enabled automatically once the Client installation is complete.
PLIST
The installation method uses a Netskope script and a PLIST file to install Netskope Client and enroll the user. This method installs users on macOS devices in a single-user mode. The steps include:
Generate .plist file.
Execute script.
Generate .plist File
Run the following command in a terminal:
sudo /usr/libexec/PlistBuddy -c "add email string user@example.com" /Library/Managed\ Preferences/template.plist
Add PLIST files to
“/Library/Managed Preferences
“.  The script fails if the “
/Library/Managed Preferences
“folder does not exist.  Use the following command to create the folder:
sudo mkdir “/Library/Managed Preferences
”
Execute Script
Download the configuration script: MAC-MDM-script.zip  from the
Netskope Support
portal. The file contains the essential command-line executable scripts to install and configure Netskope Client.
Extract the contents of the downloaded script.
Execute this command in Terminal:
sudo ./mac_mdm_installconfig.sh 0 0 0 addon-<tenant-name>[.region].<tenant-domain> <Organization ID> <plist file name> preference_email enrollauthtoken=<enrollauthtoken> enrollencryptiontoken=<enrollencryptiontoken>
Place the Netskope Client installer in the same folder as the configuration script and install the Netskope client.
MDM Deployment Methods
Netskope offers support for a wide range of MDM solutions. For MDM-specific instructions on deploying Netskope Client, view
Netskope Client Deployment Options
.
Uninstall Client in macOS
To uninstall Client in macOS:
Click the Spotlight icon from your dock or the magnifying glass on the top of your taskbar. Use Spotlight or a manual review of installation applications to find application Remove Netskope Client.
Run Remove Netskope Client app.
You are prompted to enter administrative credentials during the uninstallation process.
The Netskope Client is uninstalled from your machine.
Click OK.
The Password protection for client uninstallation and service stop option under
Client Configuration > Tamperproof
lets the administrator restrict unauthorized uninstallation of Client by the end users. If enabled, the end user must know and enter the password set by the administrator while uninstalling the Client. Service stop option is available only to Windows devices. To learn more, view Netskope Client Configuration.
Tamperproofing of Netskope Client for macOS
This section describes ways to tamperproof various attributes of Netskope Client for macOS.
Tamperproof – macOS Processes
Tampering can be malicious or accidental. Netskope integrates APIs into each Netskope process and implements them to validate and monitor the Netskope Client binary paths, signatures, and file system permissions. The API detects anomalies, logs them, and terminates them.
You must explicitly enable the required configurations for tamperproofing, as they are disabled by default, in a local configuration file. The local configuration file helps you define new policies and must be in the PLIST format. Ensure to check that the tamperproof.plist file is available in the following location:
/Library/Application Support/Netskope/STAgent/tamperproof.plist
.  The API checks for tampered files when you enable the process check in the PLIST configuration. If the API detects tampered files, the process self-terminates upon launch.
This is currently in Beta. Contact your Netskope Sales Representative to enable this feature in your account.
Prerequisites
Save the following tamperproof.plist file in
/Library/Application Support/Netskope/STAgent/tamperproof.plist
. Modify this file according to your requirement.
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
	<dict>
		<key>TeamIdentifiers</key>
		<dict>
			<key>24W52P9M7W.com.netskope.client.Netskope-Client</key>
			<dict>
				<key>DenyTrace</key>
				<true/>
				<key>ProcessCheck</key>
				<dict>
					<key>Enabled</key>
					<true/>
				</dict>
			</dict>
			<key>24W52P9M7W.com.netskope.client.Netskope-Client.NetskopeClientMacAppProxy</key>
			<dict>
				<key>DenyTrace</key>
				<true/>
				<key>ProcessCheck</key>
				<dict>
					<key>Enabled</key>
					<true/>
				</dict>
			</dict>
			<key>24W52P9M7W.nsAuxiliarySvc</key>
			<dict>
				<key>DenyTrace</key>
				<true/>
				<key>ProcessCheck</key>
				<dict>
					<key>Enabled</key>
					<true/>
				</dict>
			</dict>
			<key>24W52P9M7W.nsdiag</key>
			<dict>
				<key>DenyTrace</key>
				<true/>
				<key>ProcessCheck</key>
				<dict>
					<key>Enabled</key>
					<true/>
				</dict>
			</dict>
		</dict>
	</dict>
</plist>
Requires user root and
-r–r–r–
or
-rw-r–r–
permissions. The API ignores the file if it does not match these criteria.
To prevent tamperproof of the Netskope Client processes, admin can use any mechanism to implement this file according to their requirement. For example, use MDM solutions such as Microsoft Intune to enforce policies that restrict users from modifying the processes and policies.
If you are implementing or pushing the configuration file after installing Netskope Client, you must perform either system reboot or Netskope process restart to implement the configurations effectively.
Microsoft Intune
Follow the steps to create a profile:
Sign in to Microsoft Intune Admin Center.
Navigate to
Devices
>
By Platform
>
macOS
>
Manage Devices
>
Scripts
.
Click
Add
.
In
Basics
, enter a
Name
and
Description
.
Click
Next
.
In
Script
Settings
, save and upload the following shell script file tamperproof.sh from your local storage in your computer.
#!/bin/bash
# Configuration
TARGET_DIR="/Library/Application Support/Netskope/STAgent"
FILE_PATH="$TARGET_DIR/tamperproof.plist"
# 1. Ensure target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
    chmod 755 "$TARGET_DIR"
fi
# 2. Attach the plist content
cat <<EOF > "$FILE_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadEnabled</key>
    <true/>
    <key>UpdateSettings</key>
    <string>Automatic</string>
</dict>
</plist>
EOF
# 3. Secure permissions (Root-owned, World-readable)
chmod 644 "$FILE_PATH"
chown root:wheel "$FILE_PATH"
exit 0
Before uploading the saved shell script, you must modify it. Incorporate the tamperproof.plist script (refer
prerequisites
) into the shell script by replacing the existing shell script between lines 14 and 24 with the content from tamperproof.plist.
Make the following changes:
Run script as signed in users
: NO
Hide script notifications on devices:
Yes
Script frequency:
Based on your requirement
Max number of times to retry if script fails:
3 times
Assign the script to groups, users, and/or devices.
Click
Next
to continue.
Under
Review+Add
, you can review the policy configurations.
Click
Add
.
The webUI now displays the newly created script details.
Tamperproof- Login and Background Items
Prior to macOS Ventura versions, the users had limited visibility to applications running in the background. With newer versions of macOS, background applications are available more prominently, making it easier for the end-users to view, enable, or disable them. To learn more, view
Login and Background items
.
When Netskope Client runs  in the background, disabling its Client services can impact the functionality and potentially expose users to security risks. To prevent this, you can use MDM solutions such as VMware Workspace ONE and JAMF to enforce policies that restrict users from enabling or disabling the Client.
VMware Workspace ONE
The following configuration steps restrict users from disabling the Client in login items.
Go to
Resources
>
Profiles&Baselines
>
Profiles
.
Click
Add
>
Add Profile
.
Select
Apple macOS
as the platform to start.
Select
Device Profile
in Select Context.
Enter profile name.
Go to the
Custom Settings
section and click
Add
at the right corner of this section. The fields get enabled now.
Provide the following custom payload information in the Custom Settings text-box:
<dict>
    <key>PayloadDisplayName</key>
    <string>Service Management - Managed Login Items</string>
    <key>PayloadIdentifier</key>
    <string>com.apple.servicemanagement.xxx</string>
    <key>PayloadType</key>
    <string>com.apple.servicemanagement</string>
    <key>PayloadUUID</key>
    <string>xxxxxxxx-xxxx-xxxx-xxxx-xxx</string>
    <key>PayloadVersion</key>
    <integer>1</integer><key>Rules</key>
    <array>
    <dict>
        <key>RuleType</key>
        <string>TeamIdentifier</string>
        <key>RuleValue</key>
        <string>24W52P9M7W</string>
    </dict>
    </array>
</dict>
Edit the Payload Identifier and UUID values.
Important
Currently, many MDM providers do not have the user interface (UI) option to disable this functionality. Hence, use Custom Settings to add the payload.
Click
Next
.
On the
Assignment
page, assign the profile to Smart Groups.
Click
Save and Publish
.
JAMF
Using JAMF Pro, you can restrict users disabling Netskope Client from background services. This requires you to upload the following configuration PLIST (netskope login items.mobileconfig).
Configuration file:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>PayloadContent</key>
        <array>
            <dict>
                <key>PayloadDescription</key>    
                <string>Allows for netskope to register a launch daemons and launch agents</string>
                <key>PayloadDisplayName</key>
                <string>Managed Login Items - Netskope Apps</string>
                <key>PayloadIdentifier</key>
                <string>com.netskope.servicemanagement.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.</string>
                <key>PayloadUUID</key>
                <string>xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</string>
                <key>PayloadType</key>
                <string>com.apple.servicemanagement</string>
                <key>PayloadOrganization</key>
                <string>Netskope</string>
                <key>Rules</key>
                <array>
                    <dict>
                        <key>RuleType</key>
                        <string>TeamIdentifier</string>
                        <key>RuleValue</key>
                        <string>24W52P9M7W</string>
                        <key>Comment</key>
                        <string>Allow login items for netskope apps</string>
                    </dict>
                </array>
            </dict>
        </array>
        <key>PayloadDisplayName</key>
        <string>Managed Login Items - Netskope Apps</string>
        <key>PayloadIdentifier</key>
        <string>com.netskope.servicemanagement.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</string>
        <key>PayloadUUID</key>
        <string>xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</string>
        <key>PayloadType</key>
        <string>Configuration</string>
        <key>PayloadScope</key>
        <string>System</string>
    </dict>
</plist>
To learn more, view
Uploading a Configuration Profile for Managed Login Items
.
Perform the following steps to upload PLIST file to JAMF:
Log into JAMF with admin credentials.
Go to
Computers
>
Configuration Profiles
.
Click
Upload
.
In
Upload OS X Configuration Profile
, click
Choose File
and select the file  (netskope login items.mobileconfig)  from your local machine.
Click
Upload
. This navigates to the New macOS Configuration Profile.
In the New macOS Configuration Profile, Name under General displays the Payload Display Name string provided in the PLIST file.
Click
Save
.
Click the Scope tab and configure the scope of the configuration profile.
Click
Save
.
The configuration profile is now pushed to the target devices in your scope and you can view the new profile from Configuration Profiles.
To check the configuration profile from your macOS device, go to System Settings > General Settings > Profiles. Here you can see Managed Login Items – Netskope Apps listed under Devices (Managed) section.
Approve Full Disk Access Permission For macOS Sonoma(v14) or Later
For Netskope Client deployments on macOS Sonoma and later, Netskope Client requires Full Disk Access Permissions. During installation, end-users can view a dialog box instructing them to approve these permissions in System Settings for Netskope’s NetskopeClientMacAppProxy.
After you receive the dialog box, you can perform the following instructions:
Select
System Settings
from the dialog box.
Selecting this option automatically navigates the user to Full Disk Access under
System Settings
>
Privacy & Security
>
Full Disk Access
.
On the
Full Disk Access
screen, enable
NetskopeClientMacAppProxy
using the toggle button.
To suppress these pop-ups, administrators can provide necessary pre-authorization to devices using MDM policies. Pre-authorization requires the push of MDM payload (com.apple.TCC.configuration-profile-policy) to grant the Netskope Client’s system extension Full Disk Access. To learn more about the full disk access for MDMs, view
Netskope Deployment Options
.
In this Topic
Netskope Client for macOS

---
## Using Netskope Client
**URL:** https://docs.netskope.com/en/using-netskope-client/
**Last Modified:** 2026-05-11T12:49:12+00:00
**Scraped:** 2026-06-26T09:39:34.783736+00:00

Using Netskope Client - Netskope Knowledge Portal
Using Netskope Client
The end-user client provides the following options:
Netskope Client UI Options
For macOS
For Windows
For Linux
Services
Displays the Netskope services enabled at your endpoint. Services displays the following options:
Windows and macOS
Internet Security
Private Access
Endpoint DLP (only Windows)
Endpoint SD-WAN
Linux
Internet Security
Endpoint SD-WAN
In Windows and macOS, you can find the services displayed in the tooltip when you hover your mouse over the Netskope Client icon in the toolbar.
Windows
macOS
Enabling or Disabling
Client Services
By default, for all AD users or devices the client is enabled. However, users can choose to disable the client by selecting the
Disable Netskope Client
option from the Netskope Client system tray icon. For Windows and macOS, it displays the option
Disable All Client Services
.
With version 125.0.0, if the admin disables a user in IDP, it does not disable the Netskope Client services in the end-user device. To disable Netskope Client, you need to manually disable it from the tenant webUI.
In Windows and macOS devices, if the administrator configures the
Master Password
for a tenant, the end-user needs to provide a password shared by the IT administrator to disable the Netskope Client services that includes Internet Security and Netskope Private Access(NPA).
To disable Netskope Client services using Master Password:
Click
Disable All Client Services
.
This prompts another dialog box with the option to enter the master password shared by the IT administrator.
Enter the password.
Click
Disable
.
The webUI displays
All Netskope Client Services are Disabled
pop-up.
The webUI displays a warning “
Error Message
” if the end-user enters a wrong master password in the text box.
The steps to disable Client using
Disable All Client Services
in macOS remains the same.
Netskope also provides two nsdiag options to disable Netskope Client in Windows and macOS devices:
nsdiag -t disable
nsdiag -t disable --password <master password in plain-text>
After you run the command:
nsdiag -t disable
, it asks you to provide the master password shared by your IT administrator. Once the password is entered, it displays the following successful message:
Enable/disable client successful
The CLI displays
Incorrect Password, Client cannot be disabled
message if you enter an incorrect password.
Disable Internet Security
Use this option to disable Internet Security services on Windows and macOS platforms. With this feature:
The end-users can now easily disable Client while doing any specific tasks that require them to disable Netskope Client for Internet Security services.
Avoids uninstallation of Client and the end-user can disable Netskope Client using a one-time password(OTP); if enabled in the
Client Configuration
.
The end-user must contact their IT administrator to know the OTP that they can use to disable Internet Security services.
Once the duration for the OTP expires, the Client re-enables automatically, eliminating the need for manual intervention by the admin.
To disable internet security services in Windows and macOS:
The following screenshots are according to the webUI displayed for Windows OS.
Click
Disable Internet Security
.
This prompts a dialog box with the option to enter the one-time password.
Enter the password.
Click
Disable
.
The webUI displays a pop-up Netskope Internet Security disabled for the configured time. For example, if it is configured to disable Internet Security for 10 hours, the pop-up displays a message as given in the following screenshot.
Post Disabling Internet Security:
After disabling Internet Security from the Netskope Client icon, the
Services
section displays the following:
The Netskope Client tooltip displays the following:
Enable/Disable Endpoint SD-WAN
Use this option to disable Endpoint SD-WAN on Windows, macOS, and Linux platforms. With this feature end-users can optimize VPN traffic to hub gateways.
Windows
To disable Endpoint SD-WAN in Windows, click
Disable Endpoint SD-WAN
.
Post Disabling Endpoint SD-WAN:
After disabling Endpoint SD-WAN from the Netskope Client icon, the
Services
section and
tooltip
displays the following:
Linux
To disable Endpoint SD-WAN in Windows, click Disable Endpoint SD-WAN.
Post Disabling Endpoint SD-WAN:
After disabling Endpoint SD-WAN from the Netskope Client icon, the Services section and tooltip displays the following:
Enable/Disable Private Access
You can allow users to enable or disable the Client for Private Apps Access. Select the option
Allow disabling of Private Apps Access
from
Client Configuration
to view this option in the Netskope Client system tray icon.
Re-authenticate Private Access
Re-authentication for Private Apps option to force Netskope client to re-authenticate the user. This will reset the time for the next  periodic re-authentication. Contact Support to enable this functionality in your tenant.
In Windows and macOS:
If Re-authentication is enabled with
Grace Period
configured under
Tunnel Settings
on the Client Configuration UI, the Client UI displays a message with the time remaining before the private access disconnects.The message displays the total time in Hours: Minutes: Seconds left to re-authenticate to Netskope Client.
For example, in Windows, you have configured 24 hours in the
Re-Authentication Interval
on the Client Configuration webUI and 30 minutes as Grace Period, then the Private Access section under Services on the Client UI displays a warning message for 24:0:0.
Once the 24 hour is completed, the webUI then displays another 30 minutes as the grace period.You can also notice the Warning icon beside the text displayed that indicates that the time left for re-authentication is going to expire soon.
Once the re-authentication window expires, the Private Access status gets disabled with a proper error message.
Private Access Tenants
You can now access Private Applications across multiple Netskope tenants such as from a managed service provider, partner or third-party organizations, without needing to un-enroll or uninstall Netskope Client. You can easily switch between primary and partner tenants in a single click.
Supported OS:
Windows, macOS
This option is available only for those tenants where Netskope Private Access is enabled.
Multi-tenant access:
Seamlessly switch between partner organizations to access authorized private resources.
Client UI enhancements:
View current tenant details and a sub-menu listing all available partner tenants.
No re-installation required:
Eliminates the need to unenroll/ reinstall the Netskope Client when switching tenants.
Refer to the following user interface (UI) terms displayed under the Private Access Tenants option:
Primary tenant – Your main Netskope tenant with the Internet Security policies.
Partner tenant – Netskope tenant used by your partner. This tenant also contains policies for all users that need access to private applications.
All partner tenants are enrolled only using the IDP enrollment method. UPN based enrollments with and without Secure Enrollment tokens (including prelogon and VDI tunnel users) are unsupported.
The number of partner accounts displayed in this section depends on the number of partners added by the administrator in
Client Configuration
, with a maximum up to 20.
Here are some key points to be noted while using this functionality:
When you switch to a partner account, the Client UI displays Private Access details of the selected partner tenant. For example, Reauthentication, Private Access status, and so on. However, the Internet Security services displays details of the primary tenant.
The Private Access section UI varies with the partner tenant.
You can save only one partner configuration in your endpoint. When you switch to a new partner account, it un-enrolls from the previous partner account and then enrolls to the new partner.
Once you select a new partner tenant, you need to enroll using the IDP enrollment method.
If the end-user disables Netskope Private Access while being in the Partner account, Netskope Client switches to the Primary tenant’s prelogon connectivity (if Prelogon is enabled at the Primary Tenant).
Separate NPA logs are created for each partner tenant in
%ProgramData%/Netskope/stagent/Logs
.
Here’s an example to describe the workflow of Partner Access Tenants:
Org A is an automobile supplier to large car manufacturers and with the presence of  Netskope Client in their environment. Org A works with more than 10 vendors who need access to applications used by Org A. Some of these vendors have already used services offered by Netskope and have Netskope Client installed in their environment. Now Org A can specify the group of users and the partner tenant information in the Client Configuration.
If Org B and Org C are partner users added to the Client Configuration, refer to the following to understand the different scenarios where the primary account user (for example User A) from Org A can switch between the partner users Org B and Org C.
User A Switch to Org C (Primary to Partner Switch)
User A Switch to Org B From Org C (Partner to Partner Switch)
User A switch to Primary Tenant Org A from Partner Tenant Org B ( Partner to Primary Switch)
Limitation
Dynamic Steering configuration in partner tenants is not supported, ensure to match partner tenant users to a steering configuration without Dynamic Steering in the partner tenant.
If the encryption token is enabled and enforced in
Secure Enrollment Services
, the end-user must provide the encryption token during partner switch. Upon entering the encryption token, branding file is downloaded again and decrypted successfully.
In Windows
In macOS
The tokens are stored in the registry key (Windows) and keychain (macOS).
Windows:
HLM\\Software\\Netskope\NPAPartnerTenants
macOS:
com.netskope.client.branding.encryptToken
Once these tokens are stored, the end-user is not prompted again to enter the token in the subsequent partner switches. However, once the token expires, the end-user must enter the new encryption token. When the partner tenant is deleted from the webUI, the registry entry is removed along with the partner configuration (if any) from the user machine.  Registry/keychain entries will be removed if:
Partner tenant is removed from WEBUI
Partner Tenant Access feature is disabled
Client unenrollment
Client uninstallation
Configuration
Configuration
: During a troubleshooting scenario, user can click the Configuration option to view and share the following configuration details about the installed client.
Organization
Gateway (in FQDN format)
Gateway IP (IP address and POP name)
User Email (of the device user)
Client Configuration (name of the
Client Configuration
)
Steering Configuration (name of the
steering configuration
)
Custom Device Classification (if the device is managed)
Tunnel Protocol
Private Access (status of private access)
Private Access Gateway
Tenant (Name of the Primary or Partner tenant if Partner Tenant Access is enabled)
User Email (This email address in the Private Access refers to the user email address of the Primary or Partner user)
On-Premise check (displayed when dynamic steering is used)
Traffic Steering Type (all traffic, web traffic or cloud-app traffic)
Config Updated (date when the client configuration was last updated)
Configuration status.
Users can update Client configuration if an update is available.
See also:
Netskope Client Command Reference
for more options.
Windows
macOS
Linux
Save Logs
Use this option to save client logs that can be shared with support team for troubleshooting.
Advanced Debugging
Use this option to allow the Client to collect detailed log files like kernel driver logs, Inner packet capture, external packet capture without the need of a third-party software.
This option is visible only if the
Enable advanced debug option
is enabled in the
Client configuration
. The logs collected by the Client will depend on the
log level
selected for the debug option.
Setting log level to
Debug
may impact the performance due to high disk operations.
Packet Capture:
Allows you to capture the packets traversing through Netskope data center and later use the logs for debugging purposes.
Inner packet capture:
This refers to the packets going through the Netskope data center. All packets captured are stored in the filename
nspktdump.pcap
in your local device.
Outer packet capture:
Refers to the packets going through the physical network.
The following table refers to the files available in the Netskope Client log bundle:
Operating System
Filename
Windows
nspktdump.pcap – Only after starting the  inner packet capture.
nsouterpktdump.etl – Only after starting the outer packet capture.
macOS
nspktdump.pcap – Only after starting the inner packet capture.
nsouterpktdump.pcap – Only after starting the outer packet capture.
Linux
nspktdump.pcap – Only after starting the  inner packet capture.
nsouterpktdump.pcap – Only after starting the outer packet capture.
Steps to perform inner and outer packet captures:
Click the Netskope Client icon in the system tray and choose
Advanced Debugging
. This displays the
Advanced Debugging
window.
Click the
Packet Capture
tab.
Click the
Start
buttons for
Inner Packet Capture
and
Outer Packet Capture
.
The buttons change to
Stop
with
In Progress
status displayed below.
After recreating the issue, it is necessary to click the
Stop
buttons for I
nner Packet Capture
and
Outer Packet Capture
.
The packet capture is mainly used to get the network packets for troubleshooting by replicating the issue. However, if you run the packet capture for a longer period, it can flood your machine disk space. As a workaround, ​​limit the size of the outer packet capture to a maximum of 99MB in the
Size
text box. However, the inner packet capture keeps on accumulating indefinitely. Stopping and restarting the packet captures causes the previously captured files to be overwritten( and not appended ).
As soon as the issue is replicated, the inner and outer packet capture stops and collects the Client log bundle.
With version 128.0.0, Outer Packet Capture feature is now available in iOS devices.
Packet Capture in iOS
Packet Capture includes the following:
Inner Packet Capture:
This refers to the packets going through the Netskope data center. All packets captured are stored in the filename nspktdump.pcap in your local device.
Outer Packet Capture:
This refers to the packets going through the Netskope app.
Outer Packet Capture in iOS differs from the Outer Packet Capture available on the desktop platform. The latter captures the entire system network traffic.
With the introduction of
Outer Packet Capture
feature in iOS, users can now capture both tunneled and LWIP bypassed traffic. Netskope Client excludes those network traffic not included in the Outer Packet Capture, through the excludeRoute or VPN Profile Settings. To capture the whole iOS system traffic, it still requires connecting to a Mac. To learn more, view
Set up iOS Packet Tracing
.
Log management:
Using Log Management, it helps end-users to gather better insights for troubleshooting, and monitoring.
Set Log Level:
You can set proper log levels to filter logs according to their severity. The default log level is
Info
. The Netskope Client uses log level received from the webUI.
Select any one of the following options in
Set Log Level
:
Dump
Debug
Info
Warning
Error
Critical
Setting to
Dump
level generates more logs to files. The Netskope Client keeps two log files (fixed file size 10M) for rotation. The
Dump
level can expedite the rotation that may incur useful logs being overwritten. The log files are stored by default in the following location:
Windows Devices:
%ProgramData%/Netskope/stagent/Logs/
nsdebuglog
.log
macOS Devices:
/Library/Logs/Netskope/
nsdebuglog
.log
Linux Devices:
/opt/netskope/stagent/logs/
nsdebuglog
.log
Android: Perform the following instructions:
Go to the
Netskope Client
app.
Click the three dots.
Select
Send Logs
.
You can download it to the desired location.
iOS Devices: Users cannot read Netskope logs on iOS devices, but you can download Netskope logs zip files and share them through AirDrop and email.
Save Driver Logs:
After you set the log level, click
Start
and
Stop
to collect the logs.
Reveal Logs
: Click
Reveal Logs
to view the downloaded logs in your local device.
In Windows, the
Reveal Logs
option in the
Advanced Debugging
window displays:
%appdata%/netskope/stagent/logs
folder if
Protect Client configuration and resources
is enabled in
Client Configuration
>
Tamperproof
.
%programData%/netskope/stagent/logs
folder if Protect Client configuration and resources is disabled in
Client Configuration
>
Tamperproof
.
The behavior is due to the access restriction on
%ProgramData%
folder when Protect Client configuration and resources is enabled.  This update is available only for Client versions from 113.0.0. Prior to 113.0.0, it displayed the
%PUBLIC%/netskope/log
folder.
Speed Test:
Use this option to test the
Upload
and
Download
speed of log files. Click
Start
to initiate the testing.
Wait until both packet capture stops before collecting Netskope Client Logs.
Blocked Events
To view the list of blocked events, right click on the client icon and select
View Blocked Events
. The resulting pop-up window displays the list of access attempts that are made to any certs pinned and which are configured as blocked by the admin. Use this option to view the list of blocked events relating to certificate pined apps. These are apps that are set to be blocked in the tenant.
Enabling or Disabling
The following table describes various Netskope Client status icons that are displayed on the user interface, according to the operating system that you use.
Netskope Client Icon Status And Notifications For Platforms Except Windows and macOS
Icon
Status
Description
Enabled
The client is successfully connected to the Netskope Gateway and the client icon is in full color.
Disabled
The Netskope client has failed to download the required configuration. The client will continue to be in this state until the configuration is downloaded. Possible causes are:
The client was disabled by the end user.
The client was disabled by the admin in the Netskope admin console.
The client automatically disables itself due to the presence of a secure Forwarder, a GRE Tunnel, or a Dataplane On-Premises configuration.
The client is disabled in a multi-user scenario for the local admin or users who are not provisioned in the tenant.
Disabled due to error
The Client is disabled and the icon is grayed out with an orange circle and an exclamation point. Possible causes are:
The client has connectivity issues to the Netskope Gateway.
The health check has failed.
The client service is stopped manually.
Disabled due to fail close.
The Client is disabled and the icon is in red color.
Possible causes:Tunnel connection could not be established.
Netskope Client Icon Status And Notifications For Windows and macOS
Icon
Status
Description
Enabled
The Client icon is in full color when either one of the following services or both are enabled:
Internet security
Private Access
Disabled
The Netskope client has failed to download the required configuration.
The color here denotes that if all services are disabled and there is no Client Configuration download failure. The client will continue to be in this state until the configuration is downloaded.
Possible causes are:
The Internet security and Private Access was disabled by the end user.
Internet Security and Netskope Private Access was disabled by the admin in the Netskope admin console.
Internet Security and Netskope Private Access automatically disables itself due to the presence of a secure Forwarder, a GRE Tunnel, or a Dataplane On-Premises configuration.
Internet security and Netskope Private Access is disabled in a multi-user scenario for the local admin or users who are not provisioned in the tenant.
Enabled with warning
The icon is orange in color which states at least one of the services is enabled but has a warning in at least one of the services.
Possible causes:
NPA re-auth is in grace period and other services are enabled.
Enabled with error
The icon is red in color which states at least one of the services is enabled but has an error with at least one of the services.
Possible causes:
NPA re-auth is in grace period and other services are enabled.
Tunnel is down.
Disabled with warning
All services are disabled and one of the services has a warning.
Disabled with error
All services are disabled and one of the services has an error.
The icon is grayed out with a red circle. The tooltip displays the following when both services are disabled and one of the services are disabled due to an error:
Internet Security disabled due to error.
Private Access disabled due to error.
Possible causes are:
Internet Security and Netskope Private Access have connectivity issues to the Netskope Gateway.
The health check has failed.
The client service is stopped manually.
Disabled due to fail close.
The icon is in red color when:
Internet security is disabled due to fail close, but Private Access is exempted from fail close.
Internet Security and Private Access is disabled due to fail close.
Possible cause: Tunnel connection could not be established.
Client Service Status And Notifications
The following table lists various client service statuses and their meaning. You can also query client status via the
Get Client Data
REST API.
Internet Security Service Status And Notifications
This represents the status of the tunnel that forwards traffic to Cloud Apps, Proxy, and Firewall.
Event
Actor
Status
Meaning
Installed
System
Disabled
Via email invitation, distribution tool (i.e. SCCM, Altiris, JAMF etc)
Tunnel Up
System
Enabled
‘Auto’ enabled just after install, upgrade or later
Tunnel Down
System
Disabled
disabled – default startup state of client i.e. after installation/upgrade/restart
Tunnel down due to secure forwarder
System
Backed Off
‘Auto’ disabled due to Netskope Secure Forwarder found
Tunnel down due to GRE
System
Backed Off
‘Auto’ Disabled due to GRE
Tunnel down due to IPSec
System
Backed Off
‘Auto’ Disabled due to IPSec
Tunnel down due to Data Plane on-premises
System
Backed Off
‘Auto’ Disabled due to on-premises DP
Tunnel down due to config error
System
Errored
‘Auto’ disabled due to config errors/missing config
Tunnel down due to error in Modern Standby mode
System
Disabled
Auto’ disabled due to device in modern standby mode (AOAC)
Tunnel down due to error
System
Disabled
‘Auto’ disabled due to (any other) error
Change in network
System
Disabled
‘Auto’ disabled due to change in network
System shutdown
System
Disabled
‘Auto’ disabled due to system restart/ power down
System powerup
System
Disabled/Enabled
‘Auto’ Tunnel status will be as per actual status
Enrollment Token Error
System
Errored
Displayed when an invalid enrollment authentication token is used
Enrolled
User
Disabled
Once the user enroll using IdP mode through the Netskope Client webUI.
User Disabled
User
Disabled
User disabled the client from the system tray
User Enabled
User
Enabled
User enabled the client from the system tray
Admin Disabled
Admin
Disabled
Tenant admin disabled the client from the system tray
Admin Disabled
(This event is available only for tenants with Dynamic Steering)
Admin
Backed Off
Tenant admin disabled the Client from the webUI.
Whenever the admin selects
None
steering option, the Netskope Client disables only traffic steering and sends “Admin Disabled” event to the Device info.
Admin Enabled
Admin
Enabled
Tenant admin enabled the client from the webUI
Installed
System
Disabled
Via email invitation, distribution tool (i.e. SCCM, Altiris, JAMF etc)
Uninstalled
System
Uninstalled
Uninstalled by end user, admin, SCCM admin etc
Installation Failure
System
Disabled
Installation failed
Uninstallation Failure
System
Disabled
Disabled  Failed to uninstall the Client
Upgrade Success
System
Disabled
Client upgraded successfully
Upgrade Failure
System
Disabled
Client failed to upgrade
Rollback Success
System
Enabled
Rolled back to client version ‘x’
Rollback Failure
System
Enabled
Failed to rollback to client version ‘x’
Device Posture Change
System
Managed
Whenever the Client is in compliance with the device classification rules configured for an OS platform, the Managed status is displayed in the Device Posture Change event.
Device Posture Change
System
Unmanaged
Whenever the Client is not in compliance with the device classification rules configured for an OS platform, the Unmanaged status is displayed in the Device Posture Change event.
Device Posture Change
System
Unknown
The Client sends Unknown status before the Client downloads the device classification rules.
CA Installation Change
System
Disabled/Enabled
CA rotation is detected and new CAs are installed to the system store.
When the CA rotation is detected (the new downloaded CA is different from the existing CA and the subject name is the same), Netskope Client  posts the “CA Installation Change” event for cert rotation monitoring.
CA Installation Failure
System
Enabled
CA installation failed. This event is posted when the first attempt fails. Consecutive installation failures are not posted onto the webUI until the CA installation succeeds. Once the CA installation succeeds, it resets the status.
CA Installation Success
System
Enabled
Successful CA installation after the failed CA installation attempts. No CA Installation Success event is posted on the webUI when there are no failed attempts.
– The CA Installation Change event is available only for Windows, macOS, and Linux. For Mobile applications(iOS, Android, and ChromeOS), use MDM to install the new CAs before cert rotation. You can download
Netskope Root CA and Tenant Intermediate CA
from the tenant UI Signing CA section.
– If the CA rotation is detected and CA installation in the system store fails, the Netskope Client falls back to the older CA and user cert.
Network Private Access Status And Notifications
This represents the status of the tunnel that forwards private application traffic to Netskope.
Event
Actor
Status
Meaning
Disabled
System
Disabled
NPA is not available for the customer. NPA status code is 0.
Disabled
System
Disabled
NPA is available for the tenant but tunnel is not yet established. It should be transient state. NPA status code is 0.
Disabled
System
Disabled
NPA is available, but not enabled from the tenant UI. NPA status code is 0.
Enabled
System
Enabled
NPA tunnel is connected. NPA status code is 2.
Disabled
System
Disabled
User disables the NPA Client. NPA status code is 0.
Disabled
System
Disabled
Admin disables the NPA Client from the tenant UI. NPA status code is 0.
Errored
System
Disabled
NPA tunnel is disconnected due to error. NPA status code is 11.
Endpoint DLP Status And Notifications
If Endpoint DLP is enabled, you can click
View Details
to see Endpoint DLP Service Details.
There are two Endpoint DLP statuses:
Config Status
: The configuration state for the endpoint, which comes from the Client configurations applying to the endpoint. It displays
Enabled
or
Disabled
indicating if the endpoint should have Endpoint DLP enabled or not based on the Client configurations.
Service Status
: The reported status of the Endpoint DLP software on the endpoint. This is the same status displayed in the
Services
table above, which is reported by epdlp.exe (Windows) on the endpoint. You can see one of the following states:
Enabled
: The service is running, communicating correctly, and working properly.
Disabled
: The service is not running.
Paused
: The service is paused by clicking
Pause Service
. This action lasts for 30 minutes.
Device Control Error
/
Device Control Disabled
: The driver for USB Device Control is unable to load correctly. This status might appear for machines that are turned off.
System Reboot Required
: The endpoint needs a reboot so the USB device control functions properly. This occurs when the system has a non-resettable USB controller and an Endpoint DLP upgrade occurs. The new driver can’t be loaded until the reboot occurs.
In this Topic
Using Netskope Client

---
## Netskope Client Interoperability
**URL:** https://docs.netskope.com/en/netskope-client-interoperability/
**Last Modified:** 2026-03-02T18:01:23+00:00
**Scraped:** 2026-06-26T09:40:19.620950+00:00

Netskope Client Interoperability - Netskope Knowledge Portal
Netskope Client Interoperability
By design, the Netskope Client establishes a tunnel to steer traffic, according to the steering configuration, to the Netskope cloud to perform all required security functions (example: DLP, threat protection, etc). To provide optimal performance, the Client must connect to the closest Netskope POP to steer traffic.
When third-party apps, for example, VPN clients are installed, they establish a full tunnel and steer all traffic from the user’s device to their enterprise security stack. In such a scenario, Netskope Client will tunnel over the VPN tunnel. This results in the following performance issues:
Traffic from the client is steered via a suboptimal path to connect to Netskope POP.
Since the third-party VPN Client has no visibility into the Netskope tunnel, it offers no additional security value to the tunnel traffic.
The complete benefits of Netskope security features are not available to the users.
Interoperability Validation
The best practices guide for various third-party applications ensures that the following Netskope features operate smoothly and as expected:
Netskope Client Features
Use case Description
Third-Party Applications
Deployment
As part of deployment validation, the client was deployed on the same device that had third-party applications using an email invite.
To learn more about the different deployment methods, see
Netskope Client Deployment Options
.
VMware Carbon Black, Symantec Endpoint Protection, Palo Alto GlobalProtect, Cisco AnyConnect, McAfee Endpoint Security, OpenVPN Cloud, TrendMicro, CrowdStrike, Microsoft Always-On VPN, Sophos, Squid Proxy, Fortigate VPN, PulseSecure VPN, Blackberry Cylance
Installation Status
Post-deployment, Netskope tenant WebUI received the Client installation status events from devices that had both Netskope Client and supported third-party applications.
To learn more about Client status, see
Client Status
.
VMware Carbon Black, Symantec Endpoint Protection, Palo Alto GlobalProtect, Cisco AnyConnect, McAfee Endpoint Security, OpenVPN Cloud, TrendMicro, CrowdStrike, Microsoft Always-On VPN, Sophos, Squid Proxy, Fortigate VPN, PulseSecure VPN, Blackberry Cylance
Traffic Steering
A series of traffic steering tests were conducted to confirm that the Client was able to steer traffic without any conflicts from third-party apps installed in the same device.
To learn more about traffic steering, see
Steering Configuration
.
VMware Carbon Black, Symantec Endpoint Protection, Palo Alto GlobalProtect, Cisco AnyConnect, McAfee Endpoint Security, OpenVPN Cloud, TrendMicro, CrowdStrike, Microsoft Always-On VPN, Sophos, Squid Proxy, Fortigate VPN, PulseSecure VPN, Blackberry Cylance
Log Collection
As part of  Client troubleshooting tasks, the log collection process was successfully executed from the tenant WebUI. Log files of the Client in a machine that was installed with the third-p party apps were successfully generated.
To learn more about Client logs, see
Netskope Client Configuration
.
VMware Carbon Black, Symantec Endpoint Protection, Palo Alto GlobalProtect, Cisco AnyConnect, McAfee Endpoint Security, OpenVPN Cloud, TrendMicro, CrowdStrike, Microsoft Always-On VPN, Sophos, Squid Proxy, Fortigate VPN, PulseSecure VPN, Blackberry Cylance
Client Upgrade
A client configuration with an upgrade option was able to upgrade the Client installed in devices with third-party apps.
To learn more about Client Configuration, see
Netskope Client Configuration
.
–
Client Enable/Disable
The tenant admin could enable or disable clients installed on devices that had third-party apps.
VMware Carbon Black, Symantec Endpoint Protection, Palo Alto GlobalProtect, Cisco AnyConnect, McAfee Endpoint Security, OpenVPN Cloud, TrendMicro, CrowdStrike, Microsoft Always-On VPN, Sophos, Squid Proxy, Fortigate VPN, PulseSecure VPN, Blackberry Cylance
Compatibility Matrix
This section list third-party software that is tested and qualified to work on the same devices with Netskope Client.
VPN Applications
Third-party VPN applications require steering configuration exceptions to ensure that the respective VPN application is able to reach their gateway.  To learn more about creating VPN exceptions, see
Exception Configuration for VPN Applications
. For detailed instruction on configuration best practices in the third-party, click on the interop best practices link for your third-party app in the Notes column of the following table.
Application Name
Version
Cisco AnyConnect
5.1.2.42 or higher
Palo Alto GlobalProtect
6.3.3-676 (macOS), 6.3.3-676 (Windows)
OpenVPN Cloud
3.3.1.2222
Microsoft Always-On VPN
Windows 10 Pro with OS build 19044.1586
FortiGate VPN
FortiOS v7.2.0-b1157 (Server),  7.4.5.1888 (Client)
PulseSecure VPN
9.1R14 (build 16847) (Server), 22.7.2 (29103) (Client)
Anti Virus Applications
To ensure Netskope Client traffic operates smoothly, follow the instructions in
Exceptions for Anti Virus Applications
.
Application Name
Version
Sophos
2.20.13
McAfee End Point Security
10.7
VMware Carbon Black
4.1.0.5463
Symantec Endpoint Protection
14.0.MP1 build 2332 (14.0.2332.100)
CrowdStrike
7.24.19607.0
TrendMicro Maximum Security
14.0.20225
Blackberry Cylance
2.1.1578.42
Web Security Agent
Application Name
Version
Cisco AnyConnect Web Security
5.1.2.42 or higher
Explicit Proxies
You can use any of the following proxy applications to steer traffic from any device to the Netskope Cloud. To learn more about how Netskope Client steers traffic via explicit proxies, see
Netskope Client in an Explicit Proxy Environment
.
Application
Version
Squid Proxy
3.5.12
Cisco Umbrella
3.0.466.0
Explicit Proxies
VPN Applications
Antivirus Applications
In this Topic
Netskope Client Interoperability

---
## Enforce Enrollment for Netskope Client
**URL:** https://docs.netskope.com/en/enforce-enrollment-for-netskope-client/
**Last Modified:** 2026-06-05T12:52:23+00:00
**Scraped:** 2026-06-26T09:40:24.228578+00:00

Enforce Enrollment for Netskope Client
Mandatory user enrollment is a crucial security enhancement that guarantees all end-user traffic is subject to your organization’s security policies, thereby ensuring policy enforcement. This immediately enforces security compliance following Netskope Client installation, particularly within a managed environment.
Supported OS:
Windows, macOS
By mandating enrollment, you prevent users from bypassing security controls by ignoring to enroll to the Netskope Client . This action eliminates the significant risk of un-enrolled end-users accessing the internet without any security enforcement. It closes a common loophole where users could bypass organizational policies and expose the network to threats.
Ultimately, mandatory enrollment guarantees policy enforcement, helping your organization maintain compliance and reduce risk by ensuring no unmanaged traffic escapes essential security controls. It supports configurable install parameters, exception handling, customizable notification frequency, and works across multiple OS platforms.
Supported Client Enrollment Modes
Refer to the following table to understand the supported enrollment mode in a single and multi-user environment.
Enrollment Mode
Single User
Multi-User
IDP
Yes
Yes
Enforce Enrollment Configuration
Administrators can deploy Netskope Client in the end-user devices using the
IDP
mode, requiring end-users to enroll with their login credentials. Previously, the end-users could indefinitely bypass Client enrollment, creating significant security risks and vulnerabilities. Use the following steps to mitigate the security threats and vulnerabilities:
Step 1: Setup Enforce Enrollment Under Steering Configuration Profile
The administrators can now mandate Netskope Client enrollment using the
Enforce Enrollment
option in the Steering Configuration web UI. This feature also allows administrators to specify certain destinations that end-users can access even without Client enrollment. To learn more, view
Steering Configuration
(Go to Steps 7).
Step 2: Installation Parameters
After setting up the steering configuration, the administrator can copy the Steering Profile ID and include the ID in the MSIEXEC command or MDM scripts used to install Netskope Client in Windows and macOS. For example:
In Windows, the administrator must modify the MSIEXEC command to install Netskope Client and include the following parameters:
enforceenrollsteeringprofileid
and
enforceenrollfrequency
to enforce enrollment for users. To learn more, view
Netskope Client for Windows
.
Deployment Option
Command
Single -user mode installation
msiexec /I NSClient.msi tenant=<tenant-name> domain=[region.]<tenant-domain> installmode=idp host=addon-<tenant-name>.[region.]<tenant-domain> token=<Organization ID>[enrollauthtoken=<Authentication Token>] [enrollencryptiontoken=<Encryption Token>] [enforceenrollsteering profileid=<steering profile ID>] [enforceenrollfrequency=<time in minutes>] [/l*v %PUBLIC%nscinstall.log]
Example:
msiexec /I NSClient.msi tenant=corp domain=goskope.com installmode=idp host=addon-corp.goskope.com token=XXX enrollencryptiontoken=XXX enforceenrollsteeringprofileid=XXX enforceenrollfrequency=1
Multi-user mode installation
msiexec /I NSClient.msi tenant=<tenant-name> domain=[region.]<tenant-domain> installmode=idp mode=peruserconfig host=addon-<tenant-name>.[region.]<tenant-domain> token=<Organization ID>[enrollauthtoken=<Authentication Token>] [enrollencryptiontoken=<Encryption Token>] [enforceenrollsteeringprofileid=<steering profile ID>] [enforceenrollfrequency=
] [/l*v %PUBLIC%nscinstall.log]
Example:
msiexec /I NSClient.msi tenant=corp domain=goskope.com installmode=idp enrollencryptiontoken=XXX mode=peruserconfig enforceenrollsteeringprofileid=XXX enforceenrollfrequency=1 host=addon-corp.goskope.com token=XXX [/qn]
In macOS, for MDM-specific instructions on deploying Netskope Client, view
Netskope Client Deployment Options
(The administrator must modify the
scripts
available to deploy Netskope Client using any MDM for macOS (IDP mode) to enable enforce enrollment for any user).
Netskope Client Enrollment Enforcement Using IDP
After the Netskope Client installation, the Netskope Client prompts the end-user to enroll to Netskope Client by providing their IDP login credentials using the Enroll Netskope Client pop-up.
If the end-user chooses to defer the enrollment, the Enforce  Enrollment feature ensures that they will continue to receive reminders to complete the enrollment. The time interval set by the administrator in the command determines the frequency of these reminders. The user can click on the Enroll button in the notification to complete the enrollment.
Use Template under Settings > Tools in the webUI to customize the company logo.
Until the end-user completes enrollment, the Netskope Client blocks all web traffic i.e. TCP ports 80 and 443. During this time, end-users receive a persistent “Access Denied” pop-up notification for blocked traffic.
The pop-up notification for blocked traffic re-appears after 30 secs of closing the previous notification.
Behavior After Disabling or Unenrolling Internet Security Tunnel
An end-user can disable or unenroll Netskope Client using one of the the following options:
Administrator can allow the user to disable Internet Security tunnel using
Allow disabling of all Client Services together
or
Allow disabling of Internet Security
. If the Internet Security tunnel is disabled using these options, then traffic is allowed to go direct to the destination.
Administrator can
Allow users to unenroll
from Netskope Client: In this scenario traffic is allowed to go direct to the destination until the device is rebooted or the client service stAgentSvc is  restarted. The following table refers to the the different types of traffic steering directly after the user un-enrolls from Netskope Client:
All Traffic
Web Traffic
Cloud Apps Only
Behavior after device restart or Client service (stAgentsvc) restart
Blocks all traffic until the user enrolls to Netskope Client.
Blocks web traffic until the user enrolls to Netskope Client.
Blocks cloud apps traffic until the user enrolls to Netskope Client.
In this Topic
Enforce Enrollment for Netskope Client

---
## Netskope Client Integration With Imprivata
**URL:** https://docs.netskope.com/en/netskope-client-integration-with-imprivata/
**Last Modified:** 2026-04-06T17:00:16+00:00
**Scraped:** 2026-06-26T09:41:12.328092+00:00

Netskope Client Integration With Imprivata - Netskope Knowledge Portal
Netskope Client Integration With Imprivata
Healthcare industries use Imprivata as their identity provider (IDP) to authenticate doctors and nurses granting them access to the patient records with appropriate privileges. Imprivata logins are abstract from the logins in the operating system and Netskope Client needs to integrate with Imprivata agent to learn the logged in user information to apply related Netskope policies.
To learn more about Imprivata, view
Imprivata
.
With version 134.0.0, Netskope Client now supports integration with Imprivata for new installations. With this enhancement, you can:
Seamlessly integrate with Imprivata agent to learn the logged-in user.
Enforce differentiated policies based on users logged into Imprivata.
– Imprivata integration works only with Netskope Client and is not supported with NPA, BWAN, or EPDLP.
– Currently, Imprivata integration provided in the documentation is qualified only in the AWS environment. Support for Microsoft Azure will be provided in the future releases.
Supported Environments
OS: Windows 10, Windows 11
Imprivata appliance version: 24.2 or higher
Netskope Client version: 134.0.0 or later
Prerequisites
A workstation with the Imprivata agent configured and running.
Import Imprivata users to AD and then to your tenant.
Group users into OU/User groups based on the needs so that different configurations and policies can be applied based on the groups.
Netskope Client Imprivata Integration
Here is an example to understand the seamless management of Netskope Client in Imprivata when multiple users with different access privileges log into Imprivata.
The head nurse from Building 1 at the General Hospital taps their ID to log into the shared workstation controlled by Imprivata EAM (Enterprise Asset Management) using SSO. He/She logs in to view a few patient records and locks the computer screen. The Netskope Client applies the security policies for the nurse and starts validating his/her activity. Here, the head nurse is not allowed to modify or edit the patient records. Next, the senior doctor logs into the same Imprivata EAM using SSO to check and modify the records. In this instance, Netskope Client un-enrolls the nurse from the Imprivata workstation and enrolls the doctor. Since the doctor has the edit privileges, he/she is allowed to modify or update the patient records.
The senior doctor and the head nurse can see the Netskope Client details using the Configuration details available in the Netskope Client icon in the system tray. For example, consider the following Client and Steering Configurations set for the doctor and the nurse respectively:
User One (Doctor):
User group: new_Group001
Email/UPN: userone@mynetskopedemo.com
Client Configuration: userone_client_config
Steering Configuration: userone_confg
Traffic mode: Web
The following image refers to the Client Configuration displayed when the doctor logs into the Imprivata EAM.
User Two (Head nurse):
User group: new_Group002
Email/UPN: usertwo@mynetskopedemo.com
Client configuration: usertwo_client_config
Steering Configuration: usertwo_config
Traffic mode: Web
The following image refers to the Client Configuration displayed when the head nurse logs into the Imprivata EAM:
User One and User Two should be part of different OU groups.
Installation Method
You can install Netskope Client on the shared workstation through MDM using the parameters: Host, Token, and installmode.
Add
installmode
=
EAM
.
msiexec /i NSClient.msi host=<addon-<tenant-name>.goskope.com> token=<orgID>
installmode=EAM
enrollauthtoken=<auth token> enrollencryptiontoken=<encryption token>
Parameter
Description
host
AddonHost
addon-<FQDN used to login to the Netskope tenan>
For example, if you login to the tenant with URL acme.goskope.com then addon URL is addon-acme.goskope.com.
tenant
If the tenant URL is acme.eu.goskope.com, tenant value is acme.
token
These parameters represent Organization ID available in the MDM Distribution webUI in your tenant.
Go to Settings > Security Cloud Platform > Netskope Client > MDM Distribution.
You can find Organization ID under Deployment Resources for iOS > Create VPN Configuration.
The Organization ID varies with each tenant.
Authentication token
Encryption token
These represent the Secure Enrollment tokens required to deploy Netskope Client.
Go to Settings > Security Cloud Platform > Netskope Client > MDM Distribution.
Go to Secure Enrollment Service.
– Do not support
mode
=
peruserconfig
.
– Installation modes not supported: Email Invite, IDP, UPN.
– Do not support Imprivata Integration through Netskope Client upgrade. Only new installations are supported.
In this Topic
Netskope Client Integration With Imprivata

---
## Deploy Client On Windows Using Intune
**URL:** https://docs.netskope.com/en/deploy-client-on-windows-using-intune/
**Last Modified:** 2026-05-04T17:00:14+00:00
**Scraped:** 2026-06-26T09:42:21.949340+00:00

Deploy Client On Windows Using Intune - Netskope Knowledge Portal
Deploy Client On Windows Using Intune
This article provides instructions to deploy Netskope Client on Windows devices (either joined to Active Directory or Microsoft Entra ID) using the Microsoft Intune.
Note
To learn more about supported OS and platform, see the
Netskope Client Supported OS and Platform
section.
The following steps are for deploying Netskope Client on Windows devices.
Prerequisites:
On-board or add users into Netskope using Directory Importer or SCIM integration.
Ensure the device is enrolled in Microsoft Intune.
Log in to the Azure Portal (portal.azure.com).
Click
More Services
.
From the left-pane, click
Intune
.
From the main pane, right-click the
Intune
option and open it in a new tab. This redirects you to endpoint.microsoft.com.
From
Microsoft Endpoint Manager admin center
, select
Apps
>
All Apps
.
Select
+ Add
.
For
App Type
, select
Line-of-business app
.
Upload the NSClient.msi to
App Package File
and select
OK
.
Under
App Information
:
Provide a description.
Publisher Name.
Set
Ignore App Version
to
Yes
if you intend to allow the Netskope client to auto-update.
Select the appropriate category.
Select
No
under
Display this as a featured app in the Company Portal
.
Information and Privacy URL are optional values.
Under Command-Line Arguments: Enter the command-line arguments to apply to the .msi file upon execution. For example,
installmode=idp tenant=<tenant-name> domain=[region.]<tenant-domain> enrollencryptiontoken=<Encryption Token> /qn
To learn more about other configuration options, view
Netskope Client for Windows
.
Click
Next
.
It navigates to the
Assignments
tab.
Under
Required
category, click
Add group
to add appropriate groups that need to be included.
Click
Next
.
It navigates to
Review + Create
. Click
Create
to review and complete the process.
You can monitor the installation process from Intune. Go to
Apps
>
Windows
>
Windows | Windows Apps
>Search for “
Netskope
” >
Device Install status
.
External Browser-based Authentication
External browser support is available for MS Edge, Google Chrome and Firefox when set as the default browser. When deploying the Netskope Client in IDP mode (for single or multi-user environments), you can enable this functionality by modifying the MSIEXEC command line with additional parameters.
idpmode=scheme
httpmethod=get|post (Optional)
The following parameters are mandatory if you include
idpmode=scheme
in the command line during installation. The installation will not be successful without them.
–
installmode
–
tenant
–
domain
For example, while deploying Netskope Client on Windows using Intune, you can configure these parameters in the
Command-line arguments
field as follows:
msiexec /I STAgent.msi installmode=idp|idpOnly tenant=nsclient domain=goskope.com [enrollauthtoken=<Authentication Token>] [enrollencryptiontoken=<Encryption Token>]
idpmode=scheme [httpmethod=post]
Uninstalling Clients
To set up un-installion script for Netskope client in Windows devices follow the procedure as described in this section:
Note
This procedure is applicable only for devices that are AD joined. Also, during subsequent installation, un-assign this app to avoid un-installation of the newly installed Clients.
Login to your Intune admin console and select
Devices
>
Scripts
and remediations
.
Click
Platform Scripts
.
To start adding the uninstallation script, click
+Add
and select
Windows 10 and later
.
Under
Add Powershell script
, enter a
Name
for the script configuration and click
Next
to continue.
Under
script settings
, from the Script location drop-down, select the powershell script from your computer. Enter the following commands in the powershell script.
$product_identifier= Get-WmiObject -Class Win32_Product | where Name -eq "Netskope Client" | select -expandproperty IdentifyingNumber
msiexec /uninstall $product_identifier /l*v C:\Users\Public\nsclient_uninstall.log /qn
Set the following options for the script:
Run this script using the logged on credentials –
YES
Enforce script signature check –
NO
Run script in 64 bit PowerShell Host –
YES
Modify the path for the log to be written to and failure to modify, results in the script failure. The logged in user must have the permission to run this script and write to the specified directory or change
Run this script using the logged on credentials
to
NO
to run this from the system context. If running from system context, the system user must have the permission to write to the specified directory.
Click
Next
to continue.
Under
Assignments
, assign the user groups for this script. This uninstalls Netskope Client in all devices of the assigned user group.
Under
Review + add
, review your selections and click
Add
to complete the procedure.
In this Topic
Deploy Client On Windows Using Intune

---
## Netskope Client for iOS
**URL:** https://docs.netskope.com/en/netskope-client-for-ios/
**Last Modified:** 2026-05-04T17:00:10+00:00
**Scraped:** 2026-06-26T09:42:23.056843+00:00

Netskope Client for iOS
This document describes the available deployment methods and user enrollment options when installing the Netskope Client on iOS devices.
Supported Versions
Refer to
Netskope Client Supported OS and Platform
for more details on the supported iOS versions.
Download Client Packages
You can download Netskope Client installers from
Download Netskope Client and Scripts
.
Client Installation Methods
You can install Netskope Client in iOS using one of the following methods:
Netskope Client for iOS does not coexist with any
third-party VPN
applications due to an iOS limitation that stops an existing service when a new service is started.
Email Invite
Deployments through an email invite is a two step process:
iOS Profile link:
This installs tenant certificates on the device. They are necessary for SSL Decrypt related functionality. This profile contains only certificates.
iOS Client link:
Helps to find the Client in the App Store and enroll it after installation.
– iOS Client in the email is a one time installation only link. You will receive an error message
Email Invitation Expired
the second time you attempt to use the link after installing Netskope Client.
– If you are unable to see the link to download Netskope Client for iOS in the email invite, use the default email template that includes the link to download Netskope Client for iOS.
After you receive the email:
Check your email from Netskope Onboarding and click
iOS Profile
to install the profile with certificates to your iOS device.
Click
Allow
for the pop-up
This website is trying to download a configuration profile. Do you want to allow this?
Close the pop-up after the profile is downloaded.
In your iOS device, go to
Settings
app >
General
and tap
Profile Downloaded
. The profile consists of the root and tenant certificates.
Tap
Install
in the upper-right corner. Follow the installation instructions displayed on the screen.
Go to
Settings
>
General
>
About
>
Certificate Trust Settings
.
Tap to enable the option
Enable Full Trust to Root Certificates
.
Click
Continue
to close the warning.
Click the
iOS Client
link in the email invite.
This opens a page with two links and perform the following steps:
Click
Install
to download Netskope Client from Apple Store to iOS devices. Perform the following instructions:
Click
Allow
to add VPN configurations.
Wait for the Client enrollment.
Click
Download iOS configurations
to complete the enrollment process.
Follow the enrollment steps as displayed on your screen.
After completing the enrollment steps, go to
VPN & Device Management
.
Check whether VPN displays the Connected status to ensure the successful installation of the iOS configuration profile.
MDM Deployment Methods
Netskope offers support for a wide range of MDM solutions. For MDM-specific instructions on deploying the Netskope Client, see
Netskope Client Deployment Options
.
Verify Client Enrollment
After Client deployment and user enrollment is complete, you can verify the iOS Client installation status on your iOS device and in the Netskope account.
On your iOS device
,
Verify the Netskope Client’s tunnel status on the Client app home page.
Verify the configuration details are correct on the Client app Configuration page.
In your Netskope Admin console
,
Log into your Netskope Admin Console with administrator credentials.
Go to
Settings
>
Security Cloud Platform
>
Devices
.
The Devices page displays device hostnames and user emails associated with completed Netskope Client deployments.
Netskope Client Uninstallation
To uninstall Netskope Client on an iOS device:
Tap and hold the Netskope Client icon.
A pop-up is displayed. Tap
Remove App
.
The Netskope Client application is removed successfully.
User Alerts for iOS
The Netskope Client for iOS includes user coaching capabilities, enabling administrators to provide real-time education to employees regarding security policies. This feature allows for timely alerts, such as notifying users when they attempt to access risky websites or utilize applications that are not approved.
Key Aspects of User Alerts
Netskope provides real-time coaching through a pop-up message to inform and educate users about policy violations. This occurs when a user attempts actions such as uploading data to an unsanctioned application or accessing prohibited websites.
Administrators have the capability to set up real-time policies requiring users to provide justification for their actions.
Coaching promotes compliance and lowers IT support inquiries by explaining the rationale behind a blocked site, thereby mitigating security risks.
Setting Up User Alert Policies
Policies are defined using a set of variables. These variables define the criteria for detecting policy violations. Use real-time policies to create rules for certain actions such as accessing prohibited websites or uploading data to an unsanctioned application, and so on. In the event of any such action, a notification appears immediately on the device alerting the user of the policy violation. The user can go to the Netskope Client app to provide  necessary justification within the app.
To learn more, view
Best Practices for User Alert Policies
.
User Notifications for End-User
Once the policy is set and the user perform the blocked actions, the user coaching notification is displayed on the screen.
SSL Inspection for iOS
SSL/TLS inspection is a foundational capability that enables Netskope  to perform efficient threat and data protection services. Netskope performs SSL inspection and serves as a Man-in-the-Middle. In order to establish trust between source applications and Netskope it is required to install CA certificates into appropriate OS stores. To learn more, view
Certificates for SSL/TLS Inspection
.
SSL decryption policies allow you to specify the traffic you want to leave encrypted and not further analyzed by Netskope via the Real-time Protection policies. To learn more, view
SSL Decryption
. You can also configure specific steering configurations required for SSL decryption. To learn more about the steering configurations, view
Certificate Pinned Applications
.
The administrator can enforce the following deployment modes for personal and corporate owned iOS devices:
Per App VPN
On Demand VPN
The Per App VPN is suitable for personal or BYOD devices. Netskope steers traffic only from the managed applications administered through MDMs in a device.
For corporate devices, Netskope recommends On Demand VPN as it steers all traffic from the device. However organizations can use Per App VPN for corporate devices for better navigation around SSL inspection challenges.
Best Practices For Per App And On demand VPN
It is a best practice in both Per App and On Demand VPN to control application inventory and test SSL inspection compatibility before introducing a new application. The ability to install arbitrary apps with personal Apple ID in corporate devices can significantly increase operational costs on maintaining SSL inspection exemption policies. Apps must be vetted beforehand and they can be used for deployment using MDM (optional) after making the required configurations.
Best Practices For Per App VPN With Safari
Disable Safari on corporate devices and rely on a managed browser associated with Per App VPN.
For BYOD – keep Safari in personal space, deploy a managed browser and associate it with Per App VPN. Enforce device restrictions policies on MDM that controls data movement from managed to unmanaged apps.
Share Logs From iOS App
This section explains how to collect logs for Netskope Client for iOS using an iOS app.
Log Collection Before Enrollment
The Netskope Client for iOS app now includes a diagnostic log sharing feature that lets end user or administrators export logs anytime, even during enrollment failures or configuration delays, without IT or MDM administrator assistance.
To share logs while the enrollment is in progress on your iOS device:
Tap the Share icon.
The screen displays the following message “Collecting logs. Please wait”.
Save logs to the desired location.
Log Collection After Enrollment
To share logs after the enrollment process on your iOS device:
On your iOS device, go to the Netskope Client app home page.
Tap the
Settings
icon.
On the Settings screen, tap
Share Log
.
You can now share logs to the desired location as displayed on your screen.
DNS Traffic Behavior with Netskope Client
If traffic steering is configured as:
All Traffic or Web Traffic: Netskope Client parses both DNS-over-TCP port 53 and DNS-over-UDP port 53.
Cloud Apps or Per-app VPN: Netskope Client parses DNS-over-UDP port 53. It resets DNS-over-TCP port 53 to enforce iOS to use DNS-over-DNS port 53.
Netskope Private Access (NPA): Netskope Client parses DNS-over-UDP port 53 only.
Drops specific DNS query type (TYPE_SVCB, DNS_RESOLVER_ARPA)
Drops IPv6 DNS queries.
Limitations
The following are expected limitations pertaining to the Netskope Client for iOS:
The VPN logo is visible on the status bar of your iOS device. This is an iOS limitation.
Per-app VPN and Global VPN coexistence is not supported.
NPA does not support UDP-based private apps, Secure DNS, DoH and DoT.
In this Topic
Netskope Client for iOS

---
## Data Center Pinning In Netskope Client
**URL:** https://docs.netskope.com/en/data-center-pinning-in-netskope-client/
**Last Modified:** 2026-05-04T17:00:06+00:00
**Scraped:** 2026-06-26T09:42:25.328742+00:00

Data Center Pinning In Netskope Client - Netskope Knowledge Portal
Data Center Pinning In Netskope Client
Netskope’s data center pinning refers to a method that allows administrators to choose a country and a preferred Point of Presence (POP) for Netskope Client connectivity. For example, your organization wants to run location-specific campaigns or targeted marketing for your end-users. The administrators can connect to a country POP that is specific to a location.
Key Capabilities:
POP Pinning:
Users remain connected to the pinned POP until the set timeout period expires or they manually choose to unpin.
Configuration:
Administrators can enable POP pinning for OUs or user groups.
Timeout Control:
A maximum timeout duration for the pinned POP connection can be specified.
Status Monitoring:
The current POP pinning status can be viewed in the Devices webUI.
Supported OS:
Windows, MacOS, Linux.
– This feature is available only for GSLB-enabled tenants.
– It works only for Internet Security Services.
When the localization zone is enabled for a tenant, the egress IP for outgoing traffic at the POP can be the user’s country IP, rather than the POP’s actual country IP. This can interfere with localized content validation, as the egress IP no longer represents the POP’s geographic location.
Enable Data Center Pinning
To activate data center/ POP pinning, navigate to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Client Configuration
>
Tunnel Settings
and enable
Allow users to select data center
.
The administrator can set the timeout period for the automatic unpinning and reversion to the optimal Point of Presence (POP). The minimum setting is 30 minutes (default time), and the maximum allowed duration is 24 hours.
– There is no impact to the Users on a Netskope Client version older than 134.0.0 and the data center pinning feature continues to function as it does today.
– For users upgrading to Netskope Client version 134.0.0 or above, it is mandatory to enable “Allow users to select data center” in the relevant Client Configuration profile to ensure the Data Center Pinning feature works as intended. The time duration to which users are pinned to a selected POP depends on the time scheduled in
Revert to optimal POP afte
r.
– If this setting is not enabled for users on Netskope Client version 134.0.0 or later, they can encounter an error when attempting to run the data center pinning command.
Pin Netskope Client To a Preferred POP
After enabling the
Allow users to select data center
option in the Client Configuration, use the
nsdiag
command
nsdiag --pin
to manually pin to a desired POP for connectivity. The introduction of
nsdiag
capability provides an interactive mode that helps administrators to pin to a POP. Use this option in one of the following ways:
Choose the country and then select the preferred POP name.
Specifying the country name and POP name directly in the command.
– The Netskope Client does not fail-over to another POP when manually pinned to a POP. For example, whenever a POP is taken down for maintenance or fixing any issues, a user must manually unpin to revert to the cloud-selected optimal POP.
– In a VDI environment, if one user changes the POP pinned to Netskope Client, it automatically affects the other logged-in and new users on the VDI. The POP gets updated for all users.
Display Pin Status
Use
– -pin status
to display the current pin status and the remaining time for which the user will remain pinned to the manually selected POP. The pin status also provides the Tunnel Status details that helps administrators understand the exact tunnel establishment status.
Options To Unpin And Revert Netskope Client To The Optimal POP
There are two options to manually unpin the Netskope Client and revert to automatic POP selection whereby the Netskope Cloud selects the most optimal POP for the user:
Option 1:
Use
nsdiag --unpin
to unpin the Netskope Client and revert to automatic POP selection.
Option 2:
Reboot machine or process restart.
In multi-user deployment setup, pinning is a global operation and not user-specific. When a user pins to a POP, it affects all users on the system. The pin remains effective until you explicitly remove it using the
--unpin
command or the system clears it automatically on a restart.
– Use the same
nsdiag
command to pin and unpin Netskope Client to a POP in Windows, macOS, and Linux. For
nsdiag
command location in Windows, macOS, and Linux refer to
Netskope Client Command Reference
.
– Netskope Client will automatically unpin according to the timer set in the
Revert to optimal POP after
option in Client Configuration.
Data Center Pinning Behavior in Restricted Regions
For tenants with the China geo-fence feature enabled, running the nsdiag –pin command displays only the Points of Presence (POPs) specific to China.
In this Topic
Data Center Pinning In Netskope Client

---
## Netskope Client Configuration
**URL:** https://docs.netskope.com/en/netskope-client-configuration/
**Last Modified:** 2026-06-08T17:01:12+00:00
**Scraped:** 2026-06-26T09:43:20.014584+00:00

Netskope Client Configuration
This topic describes the various options available for an administrator to configure Netskope Client. You can configure system-wide settings using the Client Configuration dialog box.
User Group and Organization Unit (OU) Selection
You must choose either the
Organizational Unit (OU)
or a
User Group
for a configuration. You cannot apply the configuration to both simultaneously. The group listed first in the configuration list applies if a user belongs to multiple groups.
Create Client Configuration
To create a Client Configuration:
Log in to your tenant with admin credentials.
Go to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Client Configuration
.
Click
New Client Configuration
to add a new global configuration.
Additional configurations can be created to obtain granular control over the behavior of the Netskope Client at a group or OU level by creating a new configuration. If these configurations are applied to groups, they must be prioritized to determine which configuration is applied to the Client when there is an overlap in group membership.
Note
Multiple configurations can be created and applied to different OUs or Groups. But when applying a configuration only one OU or User Group can be selected.
The Client configuration name cannot exceed 40 characters.
Tunnel Settings
Endpoint DLP
Private App  Segment
Install & Troubleshoot
Tamperproof
Enable DTLS (Data Transport Layer Security)
Enable DTLS (Data Transport Layer Security). Optionally, enter the MTU value.
– It is recommended that you enable this option, if you have users connected to a lossy network.
– This option is supported only for Internet Services.
– DTLS is not supported on Netskope Client for Android and ChromeOS.
Enabling DTLS option supersedes TLS (Transport Layer Security) tunnel for communication thereby improving the network process. TCP inherently slows the overall flow performance if the network has high latency and packet drops.  To overcome this issue, use DTLS tunnel (UDP tunnel). To know the current protocol, click the
Client icon > Configurations > Tunnel Protocol
.
The connection can fallback to TLS in the event of a DTLS connection issue. For example, the firewall blocking UDP traffic or data getting fragmented. To switch to DTLS, you can perform one of the following:
Manually disable and enable the Client.
Switch your network.
After enabling DTLS, you are prompted to enter the Maximum Transmission Unit (MTU) value. This value determines the maximum size of the IP packets sent by the Netskope Client to the next hop (router). The maximum configurable value is
1500
; however, it takes the value
1350
if you do not enter any value in the MTU text-box.
Supported TLS/DTLS version:
1.2
On-Premise Detection
For On-Premises Detection, choose one of the following:
Egress IP
DNS
HTTP
For Netskope Client versions from 131.0.0, the On-Premises Detection option is available from
Settings
>
Security Cloud Platform
>
Steering Configuration
on your tenant. To learn more, view
Enable Dynamic Steering
.
By enabling any one of these options, you can detect the location of an endpoint. If the endpoint is on-premises or off-premises, the Client tunnels the traffic based on the traffic mode configured for dynamic steering.
On-Premise Detection enables you to add multiple entries in the DNS and HTTP fields. This allows you to add multiple URLs in the steering configuration. The maximum number of hosts and configured IPs that you can add is 16.
Egress IP
This option provides the ability to detect location of users (On vs Off Premises) using egress public IP address of the user location. Netskope Client detects egress public IP of the user connecting to the Netskope cloud. If the egress IP matches the entry configured in Client Configuration created by the user, then the user is marked as On-Premises.
Maximum allowed IP address entries:
100
DNS
If the FQDN entered resolves to the provided IP Address, the Netskope client is considered to be on-premises. Ensure that this is a valid DNS record that is resolvable only when on your network
HTTP
If the Client looks for the HTTP response code 200, and if successful, the device is deemed to be on-premises. Also enter a connection timeout value. The default is 10 seconds, and the max is 60 seconds.
Don’t use a .local hostname for the DNS check because the mDNS responder on Mac OSX might interfere with the resolution of local hostnames.
Don’t use hostnames or IP addresses that are defined for Netskope Private Access in DNS or HTTP checks because they cause flapping in the On-Premises check. Netskope recommends you use a separate domain name that does not overlap with NPA app definitions. You can configure a dedicated forward lookup or separate entry in your enterprise DNS for the on-prem detection.
On-Premises/Off-Premises:
If the endpoint is On-Premises or Off-Premises, the Netskope Client tunnels the following types of traffic and this traffic is bypassed either at Netskope Cloud or Netskope Client depending on the bypass exception traffic in the
steering configuration
:
Cert pinned apps
Exception domains
Exception categories
Periodic Device Classification
Enable this option to run periodic device classification validations. You can set the time in minutes(between 1 and 120) while choosing this option.
Keeping shorter time intervals can affect your device performance.  Netskope recommends to keep five minutes or more.
After enabling, the Client:
Monitors the processes, files, or other criteria configured in the
Device Classification
.
Classifies that device as unmanaged in the event of any change in the criteria.
You can view the event details in
Settings
>
Security Cloud Platform
>
Device details
>
Event History
tab. In this section, check for the event
Device Posture Change
to understand the events in your device. The following events trigger a recheck of the device posture:
Network joined
Wi-Fi network joined
System wake up
For example, when a device connects to Wi-Fi, it triggers the Device Classification scan and checks if the current status of the device matches with the rule. The status is updated only when:
There is a change in the device status.
The current status does not match the previous status. If the previous status is unmanaged and after the device classification scan, the current status changes to managed, the New Status column in the device details user interface displays the updated status.
Allow users to select POP
This feature allows administrators to grant permission to the user group or organizational unit (OU) to pin to a particular Point of Presence (POP).
To learn more about Data Center Pinning, view
Data Center Pinning in Netskope Client
.
Supported Operating Systems:
Windows, macOS, and Linux.
This is currently a Beta feature. Contact Netskope Support or your Sales Representative to enable this feature for your tenant.
The administrator can set the timeout period for the automatic unpinning and reversion to the optimal Point of Presence (POP). The minimum setting is 30 minutes (the default time), and the maximum allowed duration is 24 hours.
Advanced Options
Toggle the
Advanced
link to see the following options:
Interoperate with Proxy
Using this feature, the administrator can now configure proxies irrespective of their location in Netskope Client Configuration. By default, Netskope Client automatically detects the configured proxy by connecting to
addon-<tenant> <MP>.<tenant-domain>
, where MP = eu|de|au. If the PAC(Proxy Auto-Configuration) file redirects some traffic to other proxies, it is mandatory to declare them in the
Interoperate with Proxy
settings.
Netskope Client always detect and intercept traffic that is sent to proxies declared in
Interoperate with Proxy
. Even though it is not mandatory to select this feature, you can use it whenever multiple proxies are deployed in the Network. Netskope Client always analyze requests sent to proxies defined in the
Interoperate with Proxy
settings based on the steering configuration to decide if the requests should be intercepted or bypassed.
The Netskope Client also conducts an availability check to select the proxy to use to contact Netskope Cloud services. The Netskope Client performs this check when:
The Client service starts.
Updates in the Client configuration.
Modifications in the proxy settings.
Change in the network.
Availability check is performed by contacting
addon-<tenant> <MP>.<tenant-domain>
. The auto detected proxy is always the preferred proxy to contact Netskope Cloud services.After you configure the proxies along with the Port, Netskope Client checks for the system proxy along with the configured proxies and verifies if any proxy is reachable:
If the system proxy is reachable, the Client connects to the local proxy.
If the system proxy is unreachable, the Client checks with the other proxy IP addresses configured on the UI.
Supported platforms:
Windows and macOS.
Select the option
Interoperate with Proxy
to enable this feature and add multiple proxy IP addresses.
Interoperate with Proxy Workflow
The following steps describe working of Netskope Client when an administrator selects Interoperate with Proxy:
Netskope Client downloads the Client configuration that consists of all Client configurations. By default Netskope Client checks the configuration every hour and can be forced with manual update.
The Client checks if the Interoperate with proxy feature is enabled and checks if the proxy IP addresses are configured in the Client Configuration WebUI.
Afterwards, Client checks if any system proxy is configured. If yes, then the client uses that system proxy along with the configured and available proxies.
Preference is given to the system proxy rather than the configured IP address.
The Client then performs health check to all proxies to identify the ones that provide access to
addon-<tenant><MP>.goskope.com
. The first active proxy is used to contact Netskope Cloud services.
Traffic send to all proxies will be analyzed by the Client to determine if it should be intercepted and forwarded to Netskope Security Cloud.
Enable device classification and client-based end user notifications when the client is not tunneling traffic
This disables the Client when GRE, IPSec, Secure Forwarder and Data Plane On-Premises steering methods are detected.
Even when the Client disables itself, the user justification rules will continue to be active.
Perform SNI (Server Name Indication) check
In scenarios where multiple domains use single IP address, it is recommended to use SNI in addition to DNS to make a steering decision.The Netskope Client tunnels or bypasses the traffic whenever there is an overlap between the IP addresses of different domain names. Use the option
Perform SNI check
to get the domain name from SNI and for the Client to validate the traffic based on the SNI check. If this option is enabled, the domain name  is obtained from SNI for lookup.For example, YouTube, drive.google.com, and plus.google.com are resolved with the same IP address. In such scenarios, the unmanaged YouTube traffic is allowed to the Netskope proxy because the client steers the SaaS traffic based on the IP address. To eliminate the IP address overlapping, you can configure the Client to steer the SaaS traffic based on SNI instead of IP address. The SNI feature supports the following operating systems:
Windows
macOS
When SNI-based steering is enabled, the initial TCP three-way handshake is not steered inside the Netskope tunnel. The Client steers the traffic only after it retrieves SNI hostname from the SSL Client Hello packet. All applications with source IP restrictions fail as this happens outside the Netskope tunnel and is sourced from a non-Netskope IP.
Zone Selection
Zone Selection enables customers to selectively provide access to specialized infrastructure, such as China Elite POPs or Special Access POPs, based on the user identity such as Users Groups or Organization Units (OUs).
The administrator can select one of the two options available in Zone Selection:
China Elite: Returns an ordered list of Elite POPs followed by Premium POPs.
China Elite Extended: Returns China Elite Extended POPs (for example, HKG2), followed by Elite POPs and then Premium POPs.
If an administrator chooses
China Elite
or
China Elite Extended
in at least one Client Configuration profile, users associated with other Client Configurations that do not have a
Zone Selection
specified will no longer receive China elite POPs.
To learn more about implementation, view
GSLB Zone Selection based on User Identity
.
Contact your Sales Representative to enable this feature for your account.
Select
Enable Endpoint DLP
to enable
Endpoint Data Loss Prevention
for the client configuration and apply Content and Device Control policies to the devices. You can enable Endpoint DLP for the
Default Tenant Config
to apply policies to all client users or for custom client configurations to apply policies to specific users.
For non “Default tenant config” settings, the admin can override the default settings by checking a checkbox and changing the default settings:
Prelogon for Private App Segments
Enable this option to allow the device to connect to the private apps. In the pre-login state, the device can authenticate to the Netskope cloud and access limited resources. After you enable the prelogon option:
Prelogon is only supported on Windows devices.
Enter a prelogon username.
The email address always end in “@prelogon.netskope.com”. This is used to create a local user for pre-logon in the next section.
To use a device certification authority, click Select File to upload the certificates in PEM format.
To validate the device certificate against a Certificate Revocation List, enable Validate CRL. The CRL used to validate the device comes from the CA certificate.
Enable Start Prelogon tunnel when user tunnel disconnects. This enables the Client to always try to re-establish the prelogon tunnel when the user tunnel switches from connected to disconnected, even when the user disables the Client.
If you enable this option, users cannot fully disable the Client while using prelogon.  To allow users to fully disable the client, do not select this checkbox.
VDI Support for Private App Segments
In Virtual Desktop Infrastructure (VDI) environments, private application traffic originates from both interactive user sessions and system processes (Session ID 0). To address this, NPA introduces a dedicated
VDI User
that creates its own dedicated tunnel to steer traffic from the Netskope Client from processes that can’t be attributed to a user. This design ensures that private app packets, whether from user-initiated or system processes, are securely handled and routed based on defined policies.
Learn more
.
Periodic re-authentication for Private App Segments
Enable the Periodic re-authentication for Private App Segments option to force a user to re-authenticate into the Netskope Client if the user’s device restarts, or logs out of the PC and logs back into the device. Contact Support to enable this functionality in your tenant.
Select a time period from the
Re-Authentication Interval
dropdown list for how often you want re-authentication to occur. To allow a user time to re-authenticate after the specified interval time has expired, enable the
Grace Period
checkbox and enter the minutes. The grace period must be less than the interval.
Partner Tenant Access
Use this option to allow your users to access their partner’s private app resources without the need to unenrolling the Netskope Client.
Supported OS:
Windows, macOS
You can add partner details as shared by the partner organization administrator. Apply this configuration only in the tenant from where the users are connecting to the other tenant and not bi-directional. Select the checkbox to enable
Partner Tenant Access
for your end-users. For a user to access the partner tenant, the partner need to have a Forward SAML proxy configured for Client enrollment and the partner needs to supply appropriate credentials to the partner that receives access.
After you select
Partner Tenant Access
, perform the following to add partner to Netskope Client:
Enter the tenant name in the first text-box. For example, Partner 1.
Enter the tenant URL. For example, Partner1.goskope.com.
Click
+ADD
to include another tenant partner account.
Click
Save
.
You can only add up to 20 partner details here.
Use the delete icon to remove the existing tenant partner details from the webUI.
Upgrade Client automatically to a specific release version
For a tenant with automatic Client Upgrade option enabled, Netskope Client is set to upgrade automatically every 240 minutes or four hours.
Netskope Client checks for an update at regular intervals and in the event of an update, Netskope Client downloads the installation package and performs the update silently when one of the following conditions are met:
The idle time for the tunnel between Netskope Client  and Netskope Cloud is greater than or equal to 25 seconds (no traffic flowing through the tunnel).
Tunnel getting re-established (this occurs upon network change, user location change and so on).
Netskope Client is starting (this occurs when the machine is rebooted by the user).
Once an update is complete, a pop-up is displayed to inform the user that the Client update was done automatically.
You can choose from the following upgrade options:
If an administrator selects the
Upgrade Client Automatically
to
Specific Golden Release
option, Netskope Client will not automatically upgrade past the chosen version; even if that version later becomes unsupported.
For example, consider a scenario where an administrator configures the Client Configuration to use
Specific Golden Release
selecting version 129.0.0 which is one of the currently supported golden versions (for example 129.0.0, 132.0.0, and 135.0.0). In this scenario, all end-users will have Client version 129.0.0 on their devices. Usually, when a new golden version ( for example, 138.0.0) becomes available, 129.0.0 automatically goes out-of-support. However, since the administrator explicitly selected
Specific Golden Release
, the Client versions for end-users will remain on 129.0.0 and will not automatically upgrade to the new golden version (138.0.0).
Latest Release
: All Clients are upgraded to the latest released version.
Latest Golden Release
: All Clients are upgraded to the latest golden release. The golden release version includes dot/hotfix release updates and automatically updates to the latest available. To know more about golden releases, view Client
Downloads
page.
Specific Golden Release
: You can set all Clients to be upgraded to a specific golden release. After selecting this option, you can select the golden release from the list of available versions. In addition, you can select Opt-in Upgrade to ensure the Clients are upgraded to the latest minor or hotfix version of the selected golden release. To know more about golden releases, view Client
Downloads
.
The following options are available only as Beta from version 138.0.0:
Contact Netskope Support or your Sales Representative to enable the following options for your tenant.
Golden Release:
You can upgrade to any of the supported golden release versions of Netskope Client.The options include up to latest (current golden release version), latest-1, and latest-2 golden release versions. To know more about golden releases, view the Client
Downloads
page. Select
Opt-in dot upgrade
, if you want to automatically upgrade to the latest hotfix or minor version of the golden version of Netskope Client. When unchecked, clients remain on the exact selected version.
Monthly Release:
This displays the monthly release versions. The options include up to n-2 release versions. Select Opt-in upgrade, if you want to automatically upgrade to the latest minor or hotfix versions of the golden releases of Netskope Client. When unchecked, clients remain on exact selected version.
Specific Golden Release:
You can set all clients to be upgraded to a specific golden release. After selecting this option, you can select the golden release from the list of available versions. In addition, you can select Opt-in Upgrade to ensure the clients are upgraded to the latest minor or hot fix version of the selected golden release. For example, available Specific Golden Release versions might include 132.0.0, 132.0.7, 132.0.13, 132.0.23, 135.0.0, and 135.1.0. If you choose version 135.1.0 and enable the Opt-in Upgrade setting to allow automatic minor version updates, the Netskope Client will transition to version 135.1.10 once it becomes available. To know more about golden releases, view Client
Downloads
page.
Specific Monthly Release:
You can set all clients to be upgraded to a specific monthly release version. This includes the hotfix or minor versions available in that specific monthly release.
Show upgrade notification to end users
: Select this option to send notification to end-users after an upgrade is completed. This option is visible only if an upgrade option is selected.
Set time and frequency for the upgrade:
Allows you to schedule automatic upgrades and define the time and day for the upgrade. The main benefit of this feature is you can schedule upgrades during critical business hours. Using this feature you can:
Set a day and time on a Daily, Weekly, or Monthly basis and the time depends on your device timezone.
Choose the order in which you want to schedule the upgrade after selecting the Monthly option.
For example, you want to schedule automatic upgrades to the latest release on the first Monday of every month. You can choose the following options on the webUI:
Repeat: Monthly
Order: First
Day: Monday
Time: 10:00 AM
With this selection, the device can start upgrading anytime after 10:00 AM. The time that you set denotes the starting time to check for a latest upgrade.
The Netskope client currently waits for an idle tunnel to initiate schedule upgrade and to ensure smooth auto upgrade experience. This behavior continues and might not explicitly see the system getting updated exactly at the scheduled time.
Another set of  examples to elucidate this feature:
Example 1:
You configure Monthly – First – Monday – 10:00 AM in
Set time and frequency for the upgrade
option on Jan 15, 2024  and the current Netskope Client is in version 111.1.0. Netskope releases 112.0.0 on Feb 1, 2024.  The Client cannot start upgrading until Feb 5, 2024 10:00 AM according to the scheduled upgrade setting. Feb 5 is the first Monday after the 112.0.0 release.
Example 2:
One device out of many is offline for a few days from Jan 19 to Feb 6, 2024(Tuesday) 7:00 AM. Here, the Netskope client  auto upgrades on Tuesday 7:00 AM as schedule upgrade check already elapsed on Feb 5 10:00 AM.
Example 3:
Netskope releases 112.1.0 on Feb 20, 2024, Netskope Client upgrades to 112.1.0 only on Mar 4, 2024; the first Monday of the next month after releasing 112.1.0.
If a lower version is selected, then the endpoint with the higher version of Netskope Client will need manual uninstall and reinstall of the lower version of Netskope Client. Netskope Client checks for newer versions every 4 hours and if a new version is available, the Client will silently auto-upgrade.
32 bit and 64 bit for Windows:
You can choose to upgrade Client to the latest golden release version or latest release for 32 bit and 64 bit Windows architecture. This option is not applicable to any release version older than 131.0.0.
Uninstall clients automatically when users are removed from Netskope
The Netskope Client is uninstalled automatically whenever a user is removed from the Netskope tenant. The user need not manually uninstall Client from the endpoint.
Supported OS:
Windows and macOS
For macOS devices, whenever this option is selected, the administrator must ensure to select
Removable System Extension
option under the
System Extension Type
in the MDM profile used to deploy Netskope Client. Otherwise, the uninstallation fails due to the OS restriction. No configurations required for Windows in the MDM profile.
Allow users to unenroll
If the Netskope client is provisioned via IdP, selecting this option allows users to unenroll from Netskope. When unenrolled the user is logged out from client and the Client is disabled, the user will be required to enter their IdP credentials to enroll again to enable Client.
Advanced Options
Enable advanced debug option
Enable this option to view the debugging options. To view the debugging options, click the Client icon > Advanced Debugging option.
Log Level
This option provides the flexibility for the administrator to control and choose the log level and the default log level is
Info
. The Netskope Client uses log level received from the webUI. The log levels in nsdebug.log are displayed as
Dump
,
Debug
,
Info
,
Warning
,
Error
, and
Critical
. Setting to Dump level generates more logs to files. The Netskope Client keeps two log files (fixed file size 10M) for rotation. The Dump level can expedite the rotation that may incur useful logs being overwritten.  The log files are stored by default in the following location:
Windows Devices:
%ProgramData%/Netskope/stagent/Logs/nsdebug.log
macOS Devices:
/Library/Logs/Netskope/nsdebug.log
Linux Devices:
/opt/netskope/stagent/logs/nsdebug.log
Setting log level to Debug may impact the performance due to high disk operations.
Allow disabling of all Client services together
This option was earlier displayed as
Allow disabling of Client
on the webUI.
The new option
Allow disabling of all Client Services together
serves as a business continuity plan in the event of a disaster that provides an easy way to disable Netskope Client across the user base without reaching out to Netskope Support. Select the checkbox
Allow disabling of all Client Services together
to enable this option. After you enable it, the webUI displays a Master Password text box(optional) that allows you to configure a password that the end-user can use while disabling the Netskope Client.
For disabling Netskope Client services such as CASB, SWG, or NPA, Netskope plans to provide a separate option in the future releases. You can leverage these options based on your requirements.
– Master Password is currently optional and this works only with Netskope Client for Windows(from version 114.0.0) and macOS(from version 118.0.0). For all other operating systems, it works as before without the Master Password. Netskope plans to extend this functionality to all other operating systems in the future releases.
– The hide/view icon is displayed on the webUI only when the administrator configures a new Client Configuration profile and enables master password. The icon is not available in the edit mode.
After the administrator enables or selects this option, it facilitates the end-users to disable Netskope Client with or without password, based on the password configured or excluded in the Client Configuration. The password configured is not dynamic and remains static until the administrator decides to change.  To learn more about the working of Master Password, view
Using Netskope Client
.
Ensure to configure a password beforehand if you decide to configure a master password in the Client Configuration.  For example, in the event of a disaster in an organization, if the master password is already configured in advance in the Netskope Client Configuration, then, you as an administrator can share the configured password to multiple users at the same time. The end-users can use the same password shared by the administrator to disable Netskope Client from their devices.
Allow disabling of Internet Security
You can disable Netskope Client for Internet Security services using
Allow disabling of Internet Security.
For example, you want to test a critical application in your organization without Netskope Client being enabled. This option eliminates the need to uninstall Netskope Client and at the same time maintain business continuity.
– This option is currently available only on Windows (from version 118.0.0) and macOS (from version 130.0.0) platforms for internet security services. Other platforms/OSes will be added in the future releases.
– Netskope Private Access is currently
not supported
and will be available in the future releases.
– Upgrade your Netskope Client to version 118.0.0 or higher for Windows and version 130.0.0 or higher for macOS to enable this feature in your tenant.
Enable One-Time Password
: After choosing
Allow disabling of Internet Security
, you can also optionally select
Allow One-Time Disable with Password
to enable a one-time password(OTP) for the enrolled devices. The end-users can later use the OTP while disabling Netskope Client for Internet Security. To enable OTP:
Select the checkbox for
Allow One-Time-Disable with password
.
In
Default Time Duration
, enter the duration you want to disable Netskope Client in minutes.
After the timer expires the Netskope Client is enabled again automatically.
The minimum and maximum values allowed here are five minutes and 24 hours respectively.
After you select the
Allow One-Time Disable with password
option and configure the duration, it generates a dynamic password for each device that you can access or view from the
Devices
page.
The OTP is auto-generated and cannot be set by the administrator. Once the admin selects the OTP option in the Client Configuration, it triggers or generates an OTP for each enrolled device. You can share this OTP to each end-users that has the permission to disable internet security. Once the user successfully uses the password, a new OTP is fetched on subsequent tunnel establishment and stored for future use. To learn more about disabling Internet Security from the system tray, view
Using Netskope Client
.
Allow disabling of Private Apps access
Allow users to disable the Client for Private Apps Access. After enabling this option, you can view
Enable/Disable Private Apps Access
in the Netskope Client system tray icon. To learn more, view
Allow Users to Disable Private Apps
.
This feature is supported only on Windows and macOS devices.
Hide Client Icon on System Tray
Hides the Client icon from end users devices system tray. This will also prevent Client notifications from being displayed to the user.
Password protection for Client uninstallation
Enable this option to prevent unauthorized uninstallation of the Client from end user devices. The end users need to enter the admin password for uninstalling the Client. Password protected uninstallation is supported in both Windows, macOS, and Linux devices. Service stop option is available only to Windows devices.
The hide/view icon is displayed on the webUI only when the administrator configures a new Client Configuration profile and enables Password protection for Client uninstallation. The icon is not available in the edit mode.
Protect Client configuration and resources
After you select this option, users with elevated permissions are prevented from altering any sub-part (files, folders, and process) of the Netskope Client installation. It prevents users from modifying, renaming, or deleting Netskope processes, folders, files, and registry keys.
– Supported Platforms: Windows 10 or higher versions.
– Netskope recommends you to enable the Password protect Client uninstallation option to restrict users from uninstalling or stopping the Netskope Client services.
– With this feature enabled, there are access restrictions to the default Netskope folders. If you have any processes that utilize the default Netskope folder, change the path to another folder that your process can access. For example, refer
Configuring CLI-based Tools and Development Frameworks to work with Netskope SSL Interception
to perform such configurations where CLI tools have access to Netskope folder.
– Contact Netskope Support to allow READ permissions when the
Protect Client configuration and resources
option is enabled on Windows devices. By default, the READ permissions are denied when the
Protect Client configuration and resources
option is enabled.
With version 125.0.0, Netskope recommends enabling
Password protection for Client uninstallation
and
Protect Client configuration and resources
to prevent admins from tampering with the Netskope Client.
Fail Close
Blocks all traffic when a tunnel to Netskope is not established.  Domain-based, IP-based, and Cert-pinned exceptions will be applied, but category-based exceptions will be blocked.
– Starting with version 136.0.0, Fail Close is available under
Security Cloud Platform
>
Steering Configuration
. This transition is in a beta phase. Contact Netskope Support or your sales representative to enable this enhanced Fail Close option for your tenant.
– Older Netskope Client will continue to use Fail Close settings from Client configuration
In a multi-user environment, Fail-Close blocks all traffic for a non-provisioned user; only if at least one user has enrolled successfully to the multi-user device and mapped to a Client Configuration with the Fail-Close option enabled.
If a Netskope Internet Services tunnel fails to come up we recommend that you block the steered traffic from that device.
When Fail Close is enabled, the
Password Protection for Client Uninstallation and Service Stop
become enabled and
Allow Disabling of Clients
options becomes disabled. With Fail Close, you can Exclude Private Apps Traffic, so Private Access is not affected, and also Show Notifications.
The Netskope Client bypasses RFC-1918 IP addresses/subnets by default when in Fail-Close mode.
– Reach out to Netskope Support to enable “Block Private IP address in Fail Close”. This is supported from Netskope Client version 130.0.0.
– Remove the steering exception for
Local IP address range
in
Destination Location
from all Steering Configurations to be used with Fail-Close.
This configuration does not apply to the Private Access traffic. It is applicable only for Internet Security.
To enable Fail Close:
Select the checkbox.
This prompts a warning pop-up
Enabling “Fail Close” will also enable “Password protection for client uninstallation and service stop” and disable “Allow disabling of clients”
. Click
Proceed
.
Upon selecting Proceed, the following options are displayed:
Exclude Private App Traffic
Use this option to exempt private access traffic while fail close is enabled.
Show Notification
A fail-close pop-up is displayed whenever the tunneling to Netskope is blocked. You can select the checkbox for Show Notification to alert users why they are unable to access web applications.NoteNetskope recommends to enable the Show Notification option to get notifications.
Captive Portal Detection Timeout (Minutes)
A captive portal is a web page displayed, whenever a user tries to access the network where captive portal is enabled, to let the users authenticate prior to accessing the network. For example, if you are trying to connect to the free Wi-Fi or hotspot in an airport or restaurant where captive portals are enabled, you need to complete a set of actions to access the network.
This option enables the administrator to define captive portal grace period. If the tunnel is disconnected or cannot be established and fail close is enabled, this triggers captive portal detection. If Netskope Client is detecting or detects a captive portal, it does not enforce fail close for the configured duration to enable captive portal detection to complete. If captive portal is not detected after the detection completes, it enforces fail close again. This supports Windows OS native captive portal detection and allows user to perform captive portal authentication.
Netskope Client performs captive portal detection on Windows and macOS platforms. Admin can enter a value between 1-10 (minutes) in the
Captive Portal Detection Timeout
input box.
Captive Portal With WebView2 Browser:
With version 130.0.0, Netskope Client provides embedded mini-browser support for captive portal authentication in Windows.
When the Netskope Client detects a captive portal, it automatically displays a Captive Portal dialog box that uses a WebView2 mini browser. The dialog box closes automatically when the Netskope Client establishes its tunnel or if the current network no longer detects a captive portal.
Captive portal authentication might at times access the MAC address to track devices. When one user authenticates a device with valid credentials, it can grant network access to other users logging into the same device.
Fail Close transition from Client Configuration to Steering Configuration
The enhanced Fail Close setting, now managed in
Steering Configuration
, is currently limited to Windows devices in version 136.0.0. The Client Configuration web UI now displays a pop-up prompting administrators to manage Fail Close through Steering Configuration.
If the Fail Close option is enabled in Steering Configuration, the setting in Client Configuration will be greyed out.
To enable Fail Close for iOS and macOS devices in this scenario, the administrator must first configure the Fail Close settings within
Client Configuration
. Following this, they should contact the Netskope Support team to enable the enhanced Fail Close setting in Steering Configuration.
With the new Fail Close setting in Steering Configuration, Netskope removed previous dependencies; enabling independent management of options such as password-protected uninstallation and service disabling, regardless of Fail-Close status.
Client Configuration Encryption
Client configuration files generated in the admin config and downloaded by the client can be encrypted via the
encryptClientConfig
feature flag. This flag is disabled by default. To enable encryption reach out to Netskope Support.
The encryption is performed on all files except the nsbranding file. The nsbranding file is encrypted via the
encryptbranding
feature flag. This can be enabled via a support ticket. Also, files generated by the user device are not encrypted. This option is not available in the Netskope Tenant Admin console and can be enabled only via a support ticket.
Log files sent for debugging are decrypted before creating a zip bundle of all the log file
Audit Logs for Client Configuration
Use
Audit Logs
to check logs for all intentional or accidental changes such as create, modify, or delete. Navigate to
Settings
>
Administration
>
Audit Logs
to view
Audit Logs
.
On the Audit Log page, click the
View Details
option and it displays
Audit Log Details
.
A few examples:
Suppose you edit a few details in
Netskope Client Configuration
, the
Audit Log Details
window displays:
When you create a new
Netskope Client Configuration
:
When you delete an existing
Netskope Client Configuration
:
In this Topic
Netskope Client Configuration

---
## Netskope Client Golden Release Updates
**URL:** https://docs.netskope.com/en/netskope-client-golden-release-updates/
**Last Modified:** 2026-06-08T17:00:59+00:00
**Scraped:** 2026-06-26T09:43:22.305877+00:00

Netskope Client Golden Release Updates - Netskope Knowledge Portal
Netskope Client Golden Release Updates
Current Golden Release:
138
This document provides a summary of the latest features, fixed issues, and other updates published between two golden releases.
To learn more:
About Golden Release
.
Golden Release Updates Between 135.0.0 and 138.0.0
Golden Release Updates Between 132.0.0 and 135.0.0
Golden Release Updates Between 129.0.0 and 132.0.0
Golden Release Updates Between 126.0.0 and 129.0.0
Golden Release Updates Between 123.0.0 and 126.0.0
Golden Release Updates Between 120.0.0 and 123.0.0
Golden Release Updates Between 117.0.0 and 120.0.0
In this Topic
Netskope Client Golden Release Updates

---
## Netskope Client
**URL:** https://docs.netskope.com/en/netskope-client/
**Last Modified:** 2025-09-02T16:32:58+00:00
**Scraped:** 2026-06-26T09:44:14.376685+00:00

Netskope Client - Netskope Knowledge Portal
Netskope Client
Clients and VPN profiles provide the most comprehensive coverage as they can be installed on managed or unmanaged devices to provide visibility and policy enforcement for devices that are both on-premises and off-premises.
Netskope also provides Device Classification feature that allows you to define rules that function like posture checks on the device and allows you to create and apply policies based on these rules. To learn more, view
Device Classification
.
Netskope Client Overview
Netskope Client Supported OS and Platform
Netskope Client Network Configuration
Netskope Client Resource Utilization
Provisioning Users for Netskope Client
Netskope Client Configuration
Netskope Client Hardening
Netskope Client Interoperability
Devices
Netskope Client Deployment Options
Netskope Client Command Reference
Netskope Client Enforcement
Using Netskope Client
Deprovisioning Users
Data Center Pinning In Netskope Client
Zone Selection Based on User Identity
Netskope Client Debug Mode
Netskope Client Troubleshooting Guide
Uninstalling the Netskope Client
iOS VPN Fail Open
SAML Client Profile
Device Classification
Netskope Client Golden Release Updates
In this Topic
Netskope Client

---
## Streaming Client
**URL:** https://docs.netskope.com/en/streaming-client/
**Last Modified:** 2026-04-22T19:31:30+00:00
**Scraped:** 2026-06-26T09:44:52.857017+00:00

Streaming Client - Netskope Knowledge Portal
Streaming Client
In this Topic
Streaming Client

---
## Netskope Golden Client Release Notes Version 90.2.0
**URL:** https://docs.netskope.com/en/netskope-golden-client-release-notes-version-90-2-0/
**Last Modified:** 2025-08-31T09:59:51+00:00
**Scraped:** 2026-06-26T09:47:44.425191+00:00

Netskope Golden Client Release Notes Version 90.2.0 - Netskope Knowledge Portal
Netskope Golden Client Release Notes Version 90.2.0
Netskope release 90.2.0 is a hotfix release comprising of a couple of Netskope golden client fixes.
Release Notes Subscription
Would you like to subscribe to our release notes? To learn more:
Release Notes Subscription
.
Fixed Issues

---
## Streaming Client Release Notes April 1, 2026
**URL:** https://docs.netskope.com/en/streaming-client-release-notes-april-1-2026/
**Last Modified:** 2026-04-02T11:43:22+00:00
**Scraped:** 2026-06-26T10:03:51.106571+00:00

Streaming Client Release Notes April 1, 2026 - Netskope Knowledge Portal
Streaming Client Release Notes April 1, 2026
What's New
Fixed Issues

---
## Streaming Client Release Notes April 1, 2026
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-streaming-client-april-1-2026/
**Last Modified:** 2026-04-02T03:31:35+00:00
**Scraped:** 2026-06-26T10:03:52.437683+00:00

Streaming Client Release Notes April 1, 2026
What's New
Fixed Issues
Streaming Client Release Notes April 1, 2026 - Netskope Knowledge Portal

---
## Streaming Client Release Notes April 1, 2026
**URL:** https://docs.netskope.com/en/fixed-issues-in-streaming-client-april-1-2026/
**Last Modified:** 2026-04-02T03:31:47+00:00
**Scraped:** 2026-06-26T10:03:53.770066+00:00

Streaming Client Release Notes April 1, 2026
What's New
Fixed Issues
Streaming Client Release Notes April 1, 2026 - Netskope Knowledge Portal

---
## Streaming Client Release Notes May 7, 2026
**URL:** https://docs.netskope.com/en/fixed-issues-in-streaming-client-may-7-2026/
**Last Modified:** 2026-05-07T06:21:47+00:00
**Scraped:** 2026-06-26T10:04:50.714199+00:00

Streaming Client Release Notes May 7, 2026
What's New
Fixed Issues
Streaming Client Release Notes May 7, 2026 - Netskope Knowledge Portal

---
## Streaming Client Release Notes May 7, 2026
**URL:** https://docs.netskope.com/en/new-features-and-enhancements-in-streaming-client-may-7-2026/
**Last Modified:** 2026-05-07T06:21:59+00:00
**Scraped:** 2026-06-26T10:04:52.045968+00:00

Streaming Client Release Notes May 7, 2026
What's New
Fixed Issues
Streaming Client Release Notes May 7, 2026 - Netskope Knowledge Portal

---
## Streaming Client Release Notes May 7, 2026
**URL:** https://docs.netskope.com/en/streaming-client-release-notes-may-7-2026/
**Last Modified:** 2026-05-07T06:22:13+00:00
**Scraped:** 2026-06-26T10:04:53.181623+00:00

Streaming Client Release Notes May 7, 2026 - Netskope Knowledge Portal
Streaming Client Release Notes May 7, 2026
What's New
Fixed Issues

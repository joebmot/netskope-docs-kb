# Netskope Docs — Identity
_Generated: 2026-08-03 10:45 UTC_
_Pages: 48_

---
## Integrate an Identity Provider (IdP)
**URL:** https://docs.netskope.com/en/integrate-an-identity-provider-idp/
**Last Modified:** 2025-08-31T01:50:48+00:00
**Scraped:** 2026-08-03T09:37:42.665265+00:00

Integrate an Identity Provider (IdP)
Integrating with an IdP (like Azure AD, Okta, etc.) is a crucial part in configuring your Netskope tenant. Users and Groups that are within your IdP’s directory will be synchronized to Netskope for use in security policies and access controls.
For example, block SSH has a protocol for every user except those in the IT, CloudOps, and SecOps teams.
This allows your IdP to become the single-source-of-truth from a security perspective once you have all of your policies defined within the Netskope portal.
See
User Provisioning and Authentication
section for more details.
User Provisioning
When you onboard a new employee, you will add them to the company directory and appropriate AD/Security Groups. This information is immediately synchronized to Netskope where your security policies (based on identity attributes) are instantly enforced for that user.
These are the main methods available for synchronizing your users and groups:
SCIM Provisioning (recommended): This API link between your IdP and Netskope that automatically synchronizes user and group information.
Directory Importer Tool: Directory Importer is a tool, run locally, that synchronizes your directory information from your on-premises Active Directory Domain Controller to Netskope. This is only recommended if you don’t have a cloud-based identity service like Entra ID or Okta.
Manual Import: If you don’t operate or have a user directory or identity provider, users and groups can also be manually created within the Netskope Admin Console.
This method should only be used if you do not have an IdP that supports SCIM.
SCIM User Provisioning
A best practice is to use the SCIM protocol (an API link between the IdP and Netskope) to synchronize users to your Netskope tenant.
System for Cross-domain Identity Management (SCIM) is a standard for automating the exchange of user identity information between identity domains, or IT systems.
SCIM is supported by all major cloud IdPs, including Entra ID and Okta. Click the link below to your corresponding IdP for a guide on how to integrate it with Netskope:
Entra ID
Okta
OneLogin
When completed, you can verify if your users are being synchronized to Netskope correctly by navigating to
Settings > Security Cloud Platform
, and clicking
Users
under the Netskope Client heading.
You can validate that group membership has also successfully synchronized by clicking on the username of a user to see which groups they belong to.
Directory Importer
If your organization does not use a cloud IdP, you can use Netskope’s
Directory Importer
tool to synchronize users from your on-premise Active Directory Domain Controllers. To learn more:
Configure Directory Importer
Manual Import
If you operate a smaller organization that does not have a cloud IdP or operate Active Directory server, Netskope also supports manual user creation via the Admin Console UI or CSV Import.
Adding Users via Manual Entry or Bulk Upload
In this Topic
Integrate an Identity Provider (IdP)

---
## Configure the 3rd-Party Identity Service Provider Proxy Settings
**URL:** https://docs.netskope.com/en/configure-the-3rd-party-identity-service-provider-proxy-settings/
**Last Modified:** 2025-09-04T02:27:26+00:00
**Scraped:** 2026-08-03T09:50:10.266768+00:00

Configure the 3rd-Party Identity Service Provider Proxy Settings - Netskope Knowledge Portal
Configure the 3rd-Party Identity Service Provider Proxy Settings
You need to have the SAML Proxy Settings dialog box open in the Netskope tenant UI to complete these steps.
Login to the SSO Identify Provider Administration UI.
Modify the settings for the managed SAAS app.
From the Netskope Settings dialog box, copy the SAML Proxy ACS URL and configure it at as the login URL for the SaaS App in the ACS field.
Note
The same ACS URL needs to be configured in the Recipient and Destination fields, just in case they are to be separately configured on the third party Identity provider side.
In this Topic
Configure the 3rd-Party Identity Service Provider Proxy Settings

---
## Configure the SAML Proxy in the Netskope UI
**URL:** https://docs.netskope.com/en/configure-the-saml-proxy-in-the-netskope-ui/
**Last Modified:** 2025-09-04T02:26:57+00:00
**Scraped:** 2026-08-03T09:50:13.285019+00:00

Configure the SAML Proxy in the Netskope UI - Netskope Knowledge Portal
Configure the SAML Proxy in the Netskope UI
The SAML Proxy must be configured with the Assertion Consumer Service (ACS) URL, Identity Provider (IdP) URL, and IdP Certificate by following these procedures.
To configure the SAML Reverse Proxy in the Netskope UI:
Go to
Settings > Security Cloud Platform > Reverse Proxy > SAML
.
Click
Add Account
.
In the Add Account dialog, configure these parameters under Setup:
App: Select an app from the dropdown list. This is the app for which you want to set up the SAML proxy.
Name: Enter a name identifying the account.
ACS (Assertion Consumer Service) URL: Contact your SaaS app Service Provider (SP) vendor to get the SAML ACS URL and enter it in this field.
IdP (Identity Provider) URL: Contact your 3rd-party SSO IdP and add the per app unique Identity Provider Login URL in this field.
IdP (Identity Provider) Certificate: Copy and paste the PEM format certificate of the 3rd-party SSO IdP (This is required by Netskope to validate the signature of the SAML Assertion).
Alternate User ID: Netskope looks at the NameID field in the SAML Assertion to get the user identity. If you would like to use another field for user identification, then type the name of the SAML attribute in this field.
Redirect authentication to Netskope (optional): Enable this if you want Netskope Auth Proxy to monitor user login so that Multi-factor Authentication step-up policies can be enforced.
Click on the Options tab to configure these settings:
Emergency Bypass (optional): Enable this option to bypass the chosen app (above) from Netskope post authentication. When bypass is chosen, Yes appears in the Bypass column for this app on the main page.
Note
When enabling the emergency bypass option, users might not able to access the SaaS application if there’s a conditional access policy setup to block users from untrusted networks on the SaaS application.
Bypass Auth checks for Mobile (optional): Use to bypass auth checks for all mobile devices.
Match SAML Assertion Key Value Pair (optional:) Use to perform a Key/Value pattern match against the assertions the SAML/AuthProxy receives from the original IdP. Specific Block/Bypass actions are performed directly on matching authentication flows while all other authentication flows continue to be steered according to the default redirection policies.
Enable SAML assertion key-value pairs matching: Specify up to three pairs. The SAML/AuthProxy perform key-value pattern match against the assertions received from the original IdP. The specified action will be performed directly on matching authentication flows, while all other authentication flows continue to be steered according to the default redirection policies. Use the full SAML authentication method value if you would like to match based on password, certificate, or token auth methods.
IP Address Access (optional): To use an IP address for access enter the address, range, or CIDR netmask.
Client Certificate Check (optional): The certificates used to issue Client certificates must be uploaded before using the certificate check options. Copy and paste the intermediate CA first, and then the Root CA, into one file before uploading.
For Client Certificate Check, choose one of these options:
Not Required: Client certificate check is not required.
Required: Client certificate check is required for authentication to succeed. Choose one of these actions:
Block if failure
Bypass if success
Use result for device classification only.
To exclude IPs from the Client Certificate Check, enter them in the Exceptions text field.
To also exclude the Netskope Source IP address/ranges listed at the bottom of this page, enable the checkbox.
For the Block and Device Classification options, you can also choose to verify the user’s email address based on the Client certificate CN.
Bypass Customer IP Address/Range (optional): Enter your IP addresses and ranges to bypass. Entries need to be in CIDR format.
Click
Save
. After the proxy setting have been added, click
OK
.
After saving the configuration, click the settings icon next to your instance name to preview your configuration.
The Settings window provides the information you will need to complete the set up for your SSO identity provider and cloud app service provider:
Netskope Organization ID
Netskope SAML Proxy IdP URL
Netskope SAML Proxy ACS URL
Netskope SAML Proxy Issuer Certificate
After copying this information, close the Settings window.
To configure these SAML proxy options, click on the Tools icon in the top right of the page:
Enable Device Classification: Select to restrict access to cloud apps from corporate devices based on the device classifications set in the tenant UI.
Re-Sign SAML Assertions: Select to re-sign your SAML assertions.
Emergency Bypass: Select to allow all apps to pass through the SAML proxy.
Note
When enabling the emergency bypass option, users might not able to access the SaaS application if there’s a conditional access policy setup to block users from untrusted networks on the SaaS application.
Custom Block Page: Select from the dropdown list the block page to be shown when an application is blocked.
Tip
To update your CA, click the Replace link at the bottom of this window.
In this Topic
Configure the SAML Proxy in the Netskope UI

---
## SAML Reverse Proxy Global Settings
**URL:** https://docs.netskope.com/en/saml-reverse-proxy-global-settings/
**Last Modified:** 2025-09-04T02:25:24+00:00
**Scraped:** 2026-08-03T09:50:48.606209+00:00

SAML Reverse Proxy Global Settings - Netskope Knowledge Portal
SAML Reverse Proxy Global Settings
Netskope SAML Reverse Proxy has a global settings feature. Go to
Settings > Security Cloud Platform > Reverse Proxy > SAML
and click
Settings
.
The Global Settings options are:
Enable device classification: Device Classification allows you to define rules that function like posture checks, and then evaluate devices based on these rules. The rules vary based on the OS Platform being applied to. Once evaluated, the devices are classified as “Managed” by default. Go to
Device Classification
for more details.
Re-sign SAML assertions: A SAML assertion tells a service provider that a user is signed in. SAML assertions contain the information necessary for a service provider to confirm user identity.
Emergency bypass: Enable this option to bypass the chosen app (above) from Netskope post authentication.
Note
When enabling the emergency bypass option, users might not able to access the SaaS application if there’s a conditional access policy setup to block users from untrusted networks on the SaaS application.
Custom block page: Select the block message to display when an application is blocked.
Trusted CA for certificate authentication: Displays the current trusted CA used for SAML reverse proxy. Click the links to view or replace a file.
After changing any global settings, click
Save
.
In this Topic
SAML Reverse Proxy Global Settings

---
## SAML Reverse Proxy
**URL:** https://docs.netskope.com/en/saml-reverse-proxy/
**Last Modified:** 2025-09-04T02:24:46+00:00
**Scraped:** 2026-08-03T09:50:50.805848+00:00

SAML Reverse Proxy - Netskope Knowledge Portal
SAML Reverse Proxy
Netskope SAML proxy is required to direct the cloud app by your company to the reverse proxy running in your tenant in the Netskope cloud. If you use Netskope Client,  the traffic is redirected directly to the Netskope Cloud,
When an end user goes to a SaaS application, the traffic to an SSO system like Okta, Ping Identity, OneLogin, etc. is directed via SAML  for user authentication. Once the user is authenticated, traffic from the Netskope reverse proxy engine is used for deep analysis.
This document provides detailed instructions to set up the Netskope  SAML Proxy to integrate with a third party provider and sanctioned  SaaS app provider. Admins must configure the SAML proxy with the Assertion  Consumer Service (ACS) URL, Identity Provider (IdP) URL, and IdP Certificate.
SAML Reverse Proxy Global Settings
Configure the SAML Proxy in the Netskope UI
Configure the 3rd-Party Identity Service Provider Proxy Settings
Configure the SaaS App Service Provider Proxy Settings
In this Topic
SAML Reverse Proxy

---
## User Identity Methods for IPSec and GRE Tunnels
**URL:** https://docs.netskope.com/en/user-identity-methods-for-ipsec-and-gre-tunnels-432170/
**Last Modified:** 2026-05-26T19:48:17+00:00
**Scraped:** 2026-08-03T09:50:54.140701+00:00

User Identity Methods for IPSec and GRE Tunnels - Netskope Knowledge Portal
User Identity Methods for IPSec and GRE Tunnels
To steer tunnel traffic and identify users, you can use one of the following methods:
Configuring the Netskope Client
Netskope strongly recommends installing and configuring the
Netskope Client
to facilitate certificate distribution on devices and provide coverage for remote users. The Netskope Client provides user identification directly to Netskope so you don’t have to implement authentication on the IPSec or GRE tunnel. If you install the Netskope Client, it can send device and user info to the Netskope Cloud and show user-facing notifications that occur from policy violations.
To enable user notifications:
Go to
Settings
>
Security Cloud Platform
>
Devices
.
Click
Client Configurations
.
Click the Netskope Client Configuration with the users you want to send notifications to when they trigger a policy violation.
In the
Client Configuration
window, under
Tunnel Settings
, select
Enable device classification and client-based end user notifications when the client is not tunneling traffic
.
Note
Netskope Client supports multi-user concurrent log in. However, it doesn’t support multi-user concurrent login if you select
Enable device classification and client-based end user notifications when the client is not tunneling traffic
.
When the Netskope Client detects an IPSec or GRE tunnel, it disables the data tunnel (i.e., TLS tunnel) to the Netskope cloud but continues sending user identity to Netskope and facilitates user notifications on the endpoint. However, you can only view one user’s login information. If you installed the Netskope Client in multi-user mode on a multi-user device (e.g., terminal server), then when multiple users log in to the device at the same time, Netskope only logs and reports the first user as the one associated with the device.
Also, If you have Netskope Cloud Firewall and are using the Netskope Client, you can leverage user- and group-based policies.
Provisioning Certificates on Devices
You only need to provision
certificates
on user devices that don’t have the Netskope Client.
To download the Netskope root CA certificate and provision it on your user’s device:
Go to
Settings
>
Manage
>
Certificates
to download the certificates.
Click the
Signing CA
tab.
In
Netskope Certificate
, for
Root CA
, click
.
Provision the certificate on your user’s device. See the product documentation of their device to learn more.
Manage the certificate error settings
.
Using SAML Authentication
If you don’t use the Netskope Client, you can use SAML to authenticate a user with your Identity Provider (IdP) before their traffic is tunneled via IPSec or GRE. You must integrate Netskope as an authentication mode for an IdP. This method acts as an authentication module taking Netskope’s framework and an IdP’s auth assertion after authentication. To learn more:
Forward Proxy Authentication
.
Watch a video about forward proxy SAML authentication configuration for IPSec:
Enabling SAML Authentication
To enable SAML authentication for your tunnels:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
Authentication
.
In
Authentication
, click
Enable Authentication
.
In the
Enable Authentication
window, select
Enabled
.
Under
SAML Account
, click
Create New
.
In the
New Account
window:
Name
: Enter a name identifying the SAML account.
In the
Setup
tab:
IdP SSO URL
: Contact your third-party IdP and enter the unique IdP login URL.
IdP Entity ID
: Enter the globally unique ID for your SAML entity.
IdP Certificate
: Copy and paste the PEM format certificate of the third-party IdP. Netskope needs this information to validate the signature of the SAML assertion.
In the
Options
tab:
Alternate User ID Field
: Netskope looks at the
NameID
field in the SAML assertion to get the user identity. If you want to use another field for user identification, enter the name of the SAML attribute.
Group Attribute
: Enter your name:value pair to identify and describe your entities user group and role memberships.
Click
Save
.
Configuring the Authentication Bypass Settings
After enabling SAML authentication for your tunnels, you can specify domains, web categories, and network IP addresses that don’t require user authentication.
Adding a Domain Bypass
To add a domain bypass:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
Authentication
.
In
Bypass Settings
, under
Domain Bypass
, click
Edit
.
In the
Domain Bypass
window, add the URLs you want to bypass from the tunnels. Separate each URL entry with a comma or by adding it to a new line.
Tip
Netskope recommends adding your IdP domains.
Click
Save
.
Adding a Web Category Bypass
To add a web category bypass:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
Authentication
.
In
Bypass Settings
, under
Web Category Bypass
, click
Edit
.
In the
Web Category Bypass
window, select any
default
or
custom
web categories you want to bypass from the tunnels.
Click
Save
.
Adding a Source IP Address Bypass
To add a source IP address bypass:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
Authentication
.
In
Bypass Settings
, under
Source IP Address Bypass
, click
Edit
.
In the
Source IP Address Bypass
window, select the network locations you want to bypass from the tunnels. You can choose to bypass either the
User IP
or
Egress IP
of the network.
If you want to add a network location, click
+New
. See
Network Location Profile
.
Click
Save
.
In this Topic
User Identity Methods for IPSec and GRE Tunnels

---
## User Identity Methods for IPSec and GRE Tunnels
**URL:** https://docs.netskope.com/en/user-identity-methods-for-ipsec-and-gre-tunnels/
**Last Modified:** 2026-05-28T18:12:35+00:00
**Scraped:** 2026-08-03T09:50:55.270264+00:00

User Identity Methods for IPSec and GRE Tunnels
To steer tunnel traffic and identify users, you can use one of the following methods:
Configuring the Netskope Client
Netskope strongly recommends installing and configuring the
Netskope Client
to facilitate certificate distribution on devices and provide coverage for remote users. The Netskope Client provides user identification directly to Netskope so you don’t have to implement authentication on the IPSec or GRE tunnel. If you install the Netskope Client, it can send device and user info to the Netskope Cloud and show user-facing notifications that occur from policy violations.
To enable user notifications:
Go to
Settings
>
Security Cloud Platform
>
Devices
.
Click
Client Configurations
.
Click the Netskope Client Configuration with the users you want to send notifications to when they trigger a policy violation.
In the
Client Configuration
window, under
Tunnel Settings
, select
Enable device classification and client-based end user notifications when the client is not tunneling traffic
.
Note
Netskope Client supports multi-user concurrent log in. However, it doesn’t support multi-user concurrent login if you select
Enable device classification and client-based end user notifications when the client is not tunneling traffic
.
When the Netskope Client detects an IPSec or GRE tunnel, it disables the data tunnel (i.e., TLS tunnel) to the Netskope cloud but continues sending user identity to Netskope and facilitates user notifications on the endpoint. However, you can only view one user’s login information. If you installed the Netskope Client in multi-user mode on a multi-user device (e.g., terminal server), then when multiple users log in to the device at the same time, Netskope only logs and reports the first user as the one associated with the device.
Also, If you have Netskope Cloud Firewall and are using the Netskope Client, you can leverage user- and group-based policies.
Provisioning Certificates on Devices
You only need to provision
certificates
on user devices that don’t have the Netskope Client.
To download the Netskope root CA certificate and provision it on your user’s device:
Go to
Settings
>
Manage
>
Certificates
to download the certificates.
Click the
Signing CA
tab.
In
Netskope Certificate
, for
Root CA
, click
.
Provision the certificate on your user’s device. See the product documentation of their device to learn more.
Manage the certificate error settings
.
Using SAML Authentication
If you don’t use the Netskope Client, you can use SAML to authenticate a user with your Identity Provider (IdP) before their traffic is tunneled via IPSec or GRE. You must integrate Netskope as an authentication mode for an IdP. This method acts as an authentication module taking Netskope’s framework and an IdP’s auth assertion after authentication. To learn more:
Forward Proxy Authentication
.
Watch a video about forward proxy SAML authentication configuration for IPSec:
Enabling SAML Authentication
To enable SAML authentication for your tunnels:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
Authentication
.
In
Authentication
, click
Enable Authentication
.
In the
Enable Authentication
window, select
Enabled
.
Under
SAML Account
, click
Create New
.
In the
New Account
window:
Name
: Enter a name identifying the SAML account.
In the
Setup
tab:
IdP SSO URL
: Contact your third-party IdP and enter the unique IdP login URL.
IdP Entity ID
: Enter the globally unique ID for your SAML entity.
IdP Certificate
: Copy and paste the PEM format certificate of the third-party IdP. Netskope needs this information to validate the signature of the SAML assertion.
In the
Options
tab:
Alternate User ID Field
: Netskope looks at the
NameID
field in the SAML assertion to get the user identity. If you want to use another field for user identification, enter the name of the SAML attribute.
Group Attribute
: Enter your name:value pair to identify and describe your entities user group and role memberships.
Click
Save
.
Configuring the Authentication Bypass Settings
After enabling SAML authentication for your tunnels, you can specify domains, web categories, and network IP addresses that don’t require user authentication.
Adding a Domain Bypass
To add a domain bypass:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
Authentication
.
In
Bypass Settings
, under
Domain Bypass
, click
Edit
.
In the
Domain Bypass
window, add the URLs you want to bypass from the tunnels. Separate each URL entry with a comma or by adding it to a new line.
Tip
Netskope recommends adding your IdP domains.
Click
Save
.
Adding a Web Category Bypass
To add a web category bypass:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
Authentication
.
In
Bypass Settings
, under
Web Category Bypass
, click
Edit
.
In the
Web Category Bypass
window, select any
default
or
custom
web categories you want to bypass from the tunnels.
Click
Save
.
Adding a Source IP Address Bypass
To add a source IP address bypass:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
Authentication
.
In
Bypass Settings
, under
Source IP Address Bypass
, click
Edit
.
In the
Source IP Address Bypass
window, select the network locations you want to bypass from the tunnels. You can choose to bypass either the
User IP
or
Egress IP
of the network.
If you want to add a network location, click
+New
. See
Network Location Profile
.
Click
Save
.
In this Topic
User Identity Methods for IPSec and GRE Tunnels

---
## Add an Azure AD Account in Netskope SAML – Forward Proxy
**URL:** https://docs.netskope.com/en/add-an-azure-ad-account-in-netskope-saml-forward-proxy/
**Last Modified:** 2025-09-01T13:15:50+00:00
**Scraped:** 2026-08-03T09:51:02.974019+00:00

Add an Azure AD Account in Netskope SAML – Forward Proxy - Netskope Knowledge Portal
Add an Azure AD Account in Netskope SAML – Forward Proxy
Log in to the Netskope UI.
Go to
Settings > Security Cloud Platform > Forward Proxy > SAML
and click
Add Account
.
Enter these parameters:
Name: Enter a name for the SAML account.IDP URL: Enter the
IDP URL
from the Azure portal.IDP Entity ID: Enter the
IDP Entity ID
from the Azure portalIDP Certificate: Paste the contents of the Certificate Base64 into the IDP Certificate section.
Click
Save
.
Click
OK
The account is added.
In this Topic
Add an Azure AD Account in Netskope SAML – Forward Proxy

---
## Bypass SAML Forward Proxy Authentication Methods
**URL:** https://docs.netskope.com/en/bypass-saml-forward-proxy-authentication-methods/
**Last Modified:** 2025-08-31T01:55:21+00:00
**Scraped:** 2026-08-03T09:51:16.916613+00:00

Bypass SAML Forward Proxy Authentication Methods - Netskope Knowledge Portal
Bypass SAML Forward Proxy Authentication Methods
There are use cases where SAML Auth will need to be bypassed for traffic steered via the IPSec or GRE tunnel.
Netskope has three methods of bypass:
Domain Bypass: Like
www.<finance website>.com
and
www.<finance website>.com
. Wildcards (like *.tld) are not valid.
Web Category Bypass: Like
Finance/Accounting
.
Source IP Address – User IP / Egress IP: Like
Guest Wi-Fi, Server Subnets
The three options can be configured from the tenant under
Settings > Security Cloud Platform > Forward Proxy > SAML
.
In this Topic
Bypass SAML Forward Proxy Authentication Methods

---
## Cloud Exchange SSO with Entra ID
**URL:** https://docs.netskope.com/en/cloud-exchange-sso-with-entra-id/
**Last Modified:** 2026-03-21T01:16:51+00:00
**Scraped:** 2026-08-03T09:51:23.648657+00:00

Cloud Exchange SSO with Entra ID - Netskope Knowledge Portal
Cloud Exchange SSO with Entra ID
This article explains how to configure Single-Sign-On (SSO) for the Netskope Cloud Exchange (CE) platform, specifically for Entra ID. This will allow you to manage administrator access to CE from within your existing Identity Provider (IdP) rather than configuring administrators within the platform manually.
Cloud Exchange is different from the standard Netskope tenant you would have access to as a customer and facilitates the exchange of information between your various security and operations platforms.
Click play to watch a video.
Create a New Enterprise Application
Go to the Entra ID
portal
and sign in using your Entra ID account with sufficient permissions, like an Application Developer role.
Go to
Enterprise applications
.
Go to
Manage > All applications
and click
New application
.
The Browse Microsoft Entra Gallery pane opens and displays tiles for cloud platforms, on-premises applications, and featured applications. Applications listed in the Featured Applications section have icons indicating whether they support federated single sign-on (SSO) and provisioning. Search for
Netskope Cloud Exchange Administration Console
and select the application.
Enter a name that you want to use to recognize the instance of the application. For example,
Netskope Cloud Exchange Administration Console – SSO
.
Click
Create
. Note that the gallery can sometimes have a quirk where it returns an error when you click the
Create
button. Your application should have been created, even if you get this error. If you encounter this issue, return to the Enterprise Applications view and click the Refresh button. You should see your
Netskope Cloud Exchange
app appear in the list.
Copy the Cloud Exchange SSO Information
Log in to Cloud Exchange using the admin (super administrator) account, go to
Settings > Users
(this settings area will only be visible to the admin user).
Select the
SSO Configuration
tab and toggle the
SSO
toggle
ON
(make sure you save this configuration).
Note the Service Provider fields at the bottom of the screen. The image below shows which URL should be used for which SAML configuration field in Entra ID.
Create Roles in Entra ID
Users can be assigned Read/Write or just Read access to the Cloud Exchange UI based on the roles assigned to them: Admin (read/write access), Read-Only, or the custom admin with module-specific rights. You need to create these roles in Entra ID so that they can be assigned to users who use Cloud Exchange.
Note
If you don’t create and map these roles, SSO will fail.
Return to the main Entra ID page (ensure you are NOT within the
Enterprise Applications
page). Select
App registrations
from the left-side menu, click
All applications
, and then select the
Netskope Cloud Exchange
app from the list.
Click
App Roles
in the left panel, and then click
Create app role
. You need to create two roles: One for the Admin user role and one for the Read-Only user role.
Create the Admin role as follows:
For Display name, enter CE-Admin (this can be whatever you like).
For Allowed member types, select the first option: Users/Groups.
For Value, enter
netskope-ce-write;netskope-ce-read
. Ensure you copy/paste this exactly.
For Description, enter
Provide the user with read/write access to Cloud Exchange
. Ensure that the
Do you want to enable this app role?
option is checked.
Create the Read-Only role as follows:
For Display name, enter CE-ReadOnly (this can be whatever you like).
For Allowed member types, select the first option: Users/Groups.
For Value, enter
netskope-ce-read
. Ensure you copy/paste this exactly.
For Description, enter
Provide the user with read-only access to Cloud Exchange
. Ensure that the
Do you want to enable this app role?
option is checked.
Click
Save
. You’re finished configuring the App Roles.
Configure the Cloud Exchange Enterprise App in Entra ID
From the Entra ID main menu, return to the Enterprise Applications list and select
Netskope Cloud Exchange
.
In the left panel, click
Single sign-on
, and then select
SAML
when prompted.
Provide the SAML Configuration
Under Basic SAML Configuration, click
Edit
. Enter the Service Provider URLs from the Cloud Exchange SSO Configuration page to the appropriate Entra ID SAML configuration fields. See the tables below for mappings.
Entra ID SAML Field
Cloud Exchange Field
Identifier (Entity ID)
Service Provider Entity ID
Reply URL (Assertion Consumer Service URL)
Service Provider ACS URL
Sign on URL
Service Provider ACS URL
Relay State
N/A – Leave Blank
Logout URL
Service Provider SLS URL
The
Reply URL
and
Sign-on URL
in Entra ID both use the Service Provider ACS URL from the Cloud Exchange portal. The
Relay State
field in Entra ID should be left blank.
Click
Save
.
Add Claims for Roles and Username
Click
Edit
, and in the
Attributes & Claims
, click
Add new claim
.
Add a new claim as follows:
For Name, enter
roles
. Enter this exactly. Leave
Namespace
blank.
For Source, ensure Attribute is selected (default).
For Source attribute, select user.assignedroles from the dropdown list.
Click
Save
to add the claim.
Repeat the process to add a second role:
For Name, enter
username
. Enter this exactly, Leave
Namespace
blank.
For Source, ensure Attribute is selected (default).
For Source attribute, select user.mail from the dropdown list. Click
Save
to add the claim.
Once you’ve added the two new claims, your Attributes & Roles should look as follows:
Download the SAML Signing Certificate
Back on the SAML configuration page, scroll down to SAML Signing Certificate, and click to download the Base certificate.
Copy the Entra ID Application URLs
Under Set up Netskope Cloud Exchange, copy the Login URL, Logout URL, and Entra ID Identifier URL. You will need to paste these into the Cloud Exchange UI in the next section.
The last step to perform in Entra ID is to assign users and/or groups to the Cloud Exchange app to provide them with access. We will also assign either the
Read-Only
or
Admin
roles we created earlier to these users/groups to grant them the appropriate permissions within Cloud Exchange.
From the left panel in the Cloud Exchange Enterprise Application, select
Users and groups
, and then click
Add user/group
.
Select the users and/or groups that are permitted to use the Cloud Exchange application. You must also assign a role to the selected users/groups, like CE-Admin (read/write), or CE-ReadOnly (read-only).
Caution
If you do not assign a role, SSO will fail when the user attempts to sign in. Also, DO NOT assign the default role you see in the list; this will also cause SSO to fail. You must only use the roles that you explicitly created in Entra ID.
After assigning users/groups and applicable roles, your user/group list should look similar to this:
Finish the SSO Configuration in Cloud Exchange
Return to Cloud Exchange and go to
Settings > Users > SSO Configuration
.
Enter the app URLs for the Identity Provider URL fields in the Cloud Exchange SSO configuration. Paste the corresponding Entra ID Application URLs you copied when configuring SAML on the Entra ID side. See the table below for mappings:
Cloud Exchange Field
Entra ID SAML Config Field
Identity Provider Issuer URL
Entra ID Identifier URL
Identity provider SSO URL
Login URL
Identity provider SLO URL
Logout URL
Enter the SAML Signing Certificate. Open the Base SAML Signing Certificate you downloaded from Entra ID earlier in a text editor, such as Notepad or TextEdit. Don’t use MS Word. The certificate will have a .cer extension.
Copy the contents of the certificate file into the Public x509 Certificate field in the Cloud Exchange SSO config (see the image above).
Click
Save
.
Test the SSO Configuration
Open a new Incognito window (to avoid any potential issues with caching) and point your browser to the URL of your Cloud Exchange deployment.
If you enabled the SSO checkbox as instructed earlier this guide, you will two options when connecting to Cloud Exchange:
Log in with SSO.
Log in with Username/Password.
The SSO option is used for local login (like a default admin user, or any user manually added to the user list in CE).
Select
Login with SSO
. You should be redirected to Entra ID to sign in.
Upon entering your user credentials, you should be authenticated and redirected to the Cloud Exchange interface. In the example below, the Adele user was assigned the
CE-ReadOnly
role, so almost all of the
Settings
menu is hidden.
Troubleshooting SSO for Cloud Exchange with Entra ID
If you are having issues signing in, first look at which platform is giving you an error: Entra ID, or Cloud Exchange? If the error you see is from Entra ID, then there is likely an issue with your configuration on the Entra ID side. Double-check your URLs and/or whether the user you are attempting to sign in as is assigned to the application (or present in the group assigned to the app).
In the image below, my
nathan@lightwave.cloud
user was unable to sign in, as they were not assigned to the application in Entra ID.
If you are getting an error from Cloud Exchange, then you likely have incorrect URLs entered into either CE or Entra ID, not added the custom username and roles claims in Entra ID, or not assigned any roles to the user you are signing in as.
If you get the error {“detail”:”Method Not Allowed”}, check that the URLs copied into both Entra ID and Cloud Exchange are correct and in the right place.
If you get the error {“detail”:”Could not authenticate. username/roles attribute not set.”}, then check that you added the username and roles claims in the SAML config, AND assigned roles correctly to users when you added them to the Enterprise Application in Entra ID.
If you pass SSO fine but receive a red Error while fetching data message in CE, then there is a problem with the role you have assigned to the user. Ensure you entered
netskope-ce-write;netskope-ce-read
as the attribute for the Admin role (CE-Admin) and
netskope-ce-read
as the attribute for the Read-Only role (CE-ReadOnly). Additionally, check that you have assigned one of these roles to your impacted user. You may also get this error if the default User role is assigned.
In this Topic
Cloud Exchange SSO with Entra ID

---
## Cloud Exchange SSO with Okta
**URL:** https://docs.netskope.com/en/cloud-exchange-sso-with-okta/
**Last Modified:** 2025-10-31T02:26:43+00:00
**Scraped:** 2026-08-03T09:51:24.761551+00:00

Cloud Exchange SSO with Okta - Netskope Knowledge Portal
Cloud Exchange SSO with Okta
This article explains how to configure Single-Sign-On (SSO) for the Netskope Cloud Exchange (CE) platform, specifically for Okta. This allows you to manage administrator access to CE from within your existing Identity Provider (IdP) rather than configuring administrators within the platform manually.
Cloud Exchange is different from the standard Netskope tenant you would have access to as a customer and facilitates the exchange of information between your various security and operations platforms.
Watch a Video
Click play to watch a video.
Copy the Cloud Exchange SSO Information
Log in to Cloud Exchange using the admin (super administrator) user and go to
Settings > Users
(this settings area will only be visible to the admin user).
Select the
SSO Configuration
tab and toggle the
SSO
toggle
ON
(make sure you save this configuration). Copy the Service Provider Entity ID and Service Provider ACS URL fields. The image below shows which URL should be used for which configuration field in Okta.
Configure an Okta SAML Integration
Go back to your Okta console and configure these settings.
For the first two Service Provider URL fields in the Cloud Exchange SSO configuration, paste the corresponding URL into the appropriate field in Okta. Refer the table below for mapping:
Service Provider Entity ID
Audience URL (SP Entity ID)
Service Provider ACS URL
Single sign-on URL
Service Provider SLS URL
N/A – Not used
Set the Name ID Format
Ensure you change the Name ID Format in Okta from
Unspecified
to
EmailAddress
.
Finish the SAML Configuration
When you are done, scroll to the bottom of the page and click
Next
. Check the box
This is an internal app that we have created
and click
Finish
.
On the next page, click
View SAML Setup Instructions
inside the yellow box under the
Sign On
tab.
A new tab opens containing the IdP SSO URL, IdP Issuer, and certificate that you need to copy to later enter into the Cloud Exchange console.
Leave this tab open for now as we still have some configuration left to do in Okta.
Add Additional Attributes
Go to
Sign On
, and under the
Attribute Statements
section, click
Show legacy configuration
, then select
Edit
for
Profile attribute statements
.
Add two additional attribute statements to the Okta configuration:
username
: Set the value to
user.email
.
roles
: Set the value to
appuser.roles
(you’ll need to type this manually, as it won’t appear in the dropdown list)
Create the Roles Attribute in Okta
Users can be assigned Read/Write or just Read access to the Cloud Exchange UI based on one of three roles assigned to them: Admin (read/write access), Read-Only, and Custom admin. You need to create the roles attribute in Okta so that it can be used and assigned to the groups of IT admins who will use Cloud Exchange.
Go to
Directory > Profile Editor
from the left panel and select the
Netskope Cloud Exchange User
profile.
Here you’ll see the username attribute added when you completed the SAML configuration, but the roles attribute is nowhere to be found, so we need to create it manually.
Click
Add Attribute
.
For
Data type
, select
string
.
For
Display name
, enter
Roles
.
For
Variable name
, enter
roles
(This is case-sensitive).
For
Description
, enter
Netskope Cloud Exchange Admin Roles
.
Enable the
Attribute Required
and
Group
options.
Click
Save
.
Configure User Groups for Cloud Exchange Access
In your Okta console, create two groups: One for the users that will have read/write access to CE, and another for users that will have read-only access.
Go to
Directory > Groups
from the left panel and select
Add Group
.
Create the Read-Only and Admin Groups
Create two groups called
Netskope CE Read-Only
and
Netskope CE Admin
.
Assign People to the Read-Only Role
Click the
Netskope Cloud Exchange Read-Only
group you created from the group list to edit the group.
Under the People tab, click
Assign People
, and assign the users who will have read-only access to the CE platform. When finished, click
Save
.
Select the
Applications
tab and click
Assign applications
.
Assign the
Netskope Cloud Exchange
application.
You will then be prompted to specify a role. Enter netskope-ce-read
WARNING: You must enter this exactly or SSO will fail! This is case-sensitive.
Select
Save and Go Back
to complete the configuration of the read-only groupî
Assign People to the Admin Role
Click the
Netskope CE Admin
group you created from the group list to edit the groupî
Repeat the steps above except this time select the people who will have read/write access to the CE platform. When finished, click
Save
.
When prompted to specify a role, enter
netskope-ce-write;netskope-ce-read
.
WARNING: You must enter this exactly or SSO will fail! It is case sensitiveî
Select
Save and Go Back
to complete the configuration of the Admin group.
Finish the SSO Configuration in Cloud Exchange
Return to the
SSO Configuration
section of the Cloud Exchange UI (
Settings > Users > SSO Configuration
). Here you enter the details from the Setup Instructions that you opened (in a separate tab) previously).
For these fields in the Cloud Exchange SSO configuration, paste the corresponding information from the Okta Setup Instructions. See the table below for mapping:
Cloud Exchange Field
Okta Setup Instructions Field
Identity Provider Issuer URL
Identity Provider Issuer
Identity provider SSO URL
Identity Provider Single Sign-On URL
Cloud Exchange Field
Okta Setup Instructions Field
Identity provider SLO URL
Identity Provider Single Sign-On URL
Public Certificate
Certificate
The SLO URL field is not needed, but cannot be blank. Copy the same URL used for the Identity provider SSO URL for this field.
Click
Save
.
Testing the SSO Configuration
Open a new Incognito window (to avoid any potential issues with caching) and point your browser to the URL of your Cloud Exchange deployment.
If you enabled the SSO checkbox as instructed at the beginning of this guide, you will two options when reaching Cloud Exchange:
Log in with SSO.
Option 2 is used for local login (the default admin user, or any user manually added to the user list in Cloud Exchange).
Select
Login with SSO
. You should be redirected to Okta to sign in.
Upon entering your user credentials you should be authenticated and redirected to the Cloud Exchange interface. In the example below, the Ben user was assigned to the
Netskope CE Read-Only
group, so almost all of the
Settings
menu is hidden.
Troubleshooting SSO for Cloud Exchange with Okta
If you are having issues signing in, first look at which platform is giving you an error: Okta or Cloud Exchange? If the error you are presented with is from Okta, then the issue is likely with your config on the Okta side. Double-check your URLs and/or whether the user you are attempting to sign in as is assigned to either the
Netskope CE Read-Only
or
Netskope CE Admin
groups.
If you are getting an error from Cloud Exchange, then you have likely messed up the URLs entered into either CE or Okta, and not added the custom username and roles attributes, or not typed the name of the role correctly (ie: netskope-ce-read and netskope-ce- write;netskope-ce-read).
If you get the error {“detail”:”Method Not Allowed”}, check that the URLs copied into both Okta and Cloud Exchange are correct and in the right place.
If you get the error {“detail”:”Could not authenticate. username/roles attribute not set.”}, then check that you have added the username and roles claims in the SAML configî
If you pass SSO fine, but receive a red Error while fetching data message in CE, then there is a problem with the role you have assigned to the user. Ensure you entered
netskope-ce-write;netskope-ce-read
as the attribute for the Admin group (Netskope CE Admin) and
netskope-ce-read
as the attribute for the Read-Only role (Netskope CE Read-Only)
Additionally, check that you have assigned one of these groups to your impacted user: You may also get this error if anything else has been entered into the role field apart from the above two accepted strings
In this Topic
Cloud Exchange SSO with Okta

---
## Configure ADFS for Netskope SAML
**URL:** https://docs.netskope.com/en/configure-adfs-for-netskope-saml/
**Last Modified:** 2025-08-31T01:55:40+00:00
**Scraped:** 2026-08-03T09:51:34.654018+00:00

Configure ADFS for Netskope SAML - Netskope Knowledge Portal
Configure ADFS for Netskope SAML
Add the Netskope Secure Web Gateway service as a relying party trust. Open the ADFS Management window and select the Relying Party Trusts folder. Right click the Relying Party Trusts folder to add a Relying Part Trust.
When the Add Relying Party Trust wizard appears, click
Start
.
In Select Data Source, select
Enter Data about the relying part trust manually
and click
Next
.
For Display name, enter a display name for the Netskope Secure Web Gateway service, such as Netskope-SAML, and then click
Next
.
For Configure Certificate, click
Next
and proceed to the next step.
For Configure URL, select
Enable support for the SAML 2.0 WebSSO protocol
and enter the Netskope SSO URL. Log in to the Netskope UI and go to:
Settings > Security Cloud Platform > Forward Proxy > SAML > SAML Settings
. Copy the SAML ACS URL into ADFS, and then click
Next
.
For Configure Identifiers, enter the Netskope SAML Entity ID. Log in to the Netskope UI and go to:
Settings > Security Cloud Platform > Forward Proxy > SAML > SAML Settings
. Copy the SAML Entity ID into ADFS, and then click
Add
and
Next
.
For Choose Access Control Policy, select
Permit everyone
and click
Next
.
For Ready to Add Trust, the wizard displays the configured settings. Click
Next
.
Click
Finish
to add the relying party trust to the database. Clear the option to open the Edit Claim Rules dialog.
Log in to the Netskope UI and go to:
Settings > Security Cloud Platform > Forward Proxy > SAML > SAML Settings
. Click
Download Certificate
. Rename the file with a
.crt
file extension. In ADFS, right click the relying party trust that was created above and open its Properties. In the Signature tab, click
Add
, navigate to the Netskope certificate, and then click
Open
. In the Advanced tab, select
SHA-1
from the Secure Hash algorithm dropdown list, and then click
OK
.
Tip
ADFS may reject the certificate as part of the signing certificate revocation checks; see the error message in the image below. If you get signature errors, then check if you have disabled Signing and Encryption checks for the Relying Party Trust.
Netskope Certificates are self-signed and cannot be validated via the public internet. Also, the certificates do not have any public facing CRL Distribution Points or AIA values configured within the certificate. You need to set the certificate checks to
None
.
In the ADFS Management Window, open the Trust Relationships > Relying Party Trusts folder. Right-click the relying party trust created earlier and select
Edit Claim Issuance Policy
. When the Edit Claim Issuance Policy appears, click
Add Rule
. In Choose Rule Type of the Add Transform Claim Rule Wizard, select
Send LDAP attributes as Claims
as the claim rule template so claims contain LDAP attribute values from the attribute store, AD. Then click
Next
. For Claim Rule, do the following and click
Next
.
Enter a name for the claim rule.
From the Attribute Store menu, choose Active Directory.
Map the LDAP attributes that represent the user’s login name to a field in the outgoing claim.
From the LDAP attribute column, select the attribute for the login name. For example: User-Principal-Name. From the Outgoing Claim Type column, select
Name ID
. (Note that Name ID is entered as two words, with a space between them). Click
Finish
.
In this Topic
Configure ADFS for Netskope SAML

---
## Configure ADFS for Netskope SSO Manually
**URL:** https://docs.netskope.com/en/configure-adfs-for-netskope-sso-manually/
**Last Modified:** 2025-08-31T01:38:38+00:00
**Scraped:** 2026-08-03T09:51:35.758481+00:00

Configure ADFS for Netskope SSO Manually - Netskope Knowledge Portal
Configure ADFS for Netskope SSO Manually
To complete these steps, you need the Netskope Assertion Consumer Service URL, Service Provider Entity ID, and SAML certificate. Go to
Settings > Administration > SSO
, and under Netskope Settings, copy the Assertion Consumer Service URL and Service Provider Entity ID, and then download the SAML certificate.
Add the Netskope admin console as a relying party trust. Open the ADFS Management window and right click the
Relying Party Trusts
folder, and then click
Add Relying Party Trust
.
Enable
Claims aware
and click
Start
.
For Select Data Source, select
Enter Data about the relying party trust manually
and click
Next
.
For Display name, enter a meaningful name, like
Netskope Management Console
, and then click
Next
.
For Configure Certificate, click
Next
and proceed to the next step.
For Configure URL, select
Enable support for the SAML 2.0 WebSSO protocol
and enter the Netskope Assertion Consumer Service URL into ADFS, and then click
Next
.
For Configure Identifiers, enter the Netskope Service Provider Entity ID into ADFS, and then click
Add
and
Next
.
For Choose Access Control Policy, select
Permit everyone
and click
Next
.
For Ready to Add Trust, the wizard displays the configured settings. Click
Next
.
Click
Finish
to add the relying party trust to the database.
Enable the
Configure claims issuance policy for this application
checkbox and click
Close
.
In the ADFS Management Window, open the Trust Relationships > Relying Party Trusts folder. Right-click the relying party trust created earlier and select
Edit Claim Issuance Policy
. When the Edit Claim Issuance Policy appears, click
Add Rule
. For Choose Rule Type in the Add Transform Claim Rule Wizard, select
Send LDAP attributes as Claims
as the Claim Rule Template so claims contain LDAP attribute values from the AD attribute store. Click
Next
.
For Configure Claim Rule, enter and select the following:
Enter a name for the claim rule.
For Attribute Store, select
Active Directory
.
Map the LDAP attributes that represent the user’s login name to a field in the outgoing claim. In the LDAP attribute column, select
E-Mail-Address
. In the Outgoing Claim Type column, select or enter
Name ID
. (Note that Name ID is entered as two words, with a space between them).
Click
Finish
.
Add another Claim Issuance Policy rule. For Choose Rule Type, select
Send Group Membership as a Claim
, as the Claim Rule Template, and then click
Next
.
For Configure Claim Rule, enter and select the following:
Enter a name for the claim rule, like
Tenant Admins
.
For User’s Group, browse and select the AD group that will be mapped to the Tenant Admin role in the Netskope UI.
For Outgoing Claim Type, select
admin-role
.
For Outgoing Claim Value, enter
Tenant Admin
.
In this rule, users in the
NS-Tenant-Admins
group are mapped to the pre-defined
Tenant Admin
role on the Netskope UI. Click
Finish
.
Add another Claim Issuance Policy rule. For Choose Rule Type, select
Send Group Membership as a Claim
, as the Claim Rule Template, and then click
Next
.
For Configure Claim Rule, enter and select the following:
Enter a name for the claim rule, like
Restricted Admins
.
For User’s Group, browse and select the AD group that will be mapped to the Restricted Admin role in the Netskope UI.
For Outgoing Claim Type, select
admin-role
.
For Outgoing Claim Value, enter
Restricted Admin
.
In this rule, users in the
NS-Restricted-Admins
group are mapped to the pre-defined
Restricted Admin
role on the Netskope UI. Click
Finish
.
Note
Configure further roles as needed.
In the Claim Issuance Policy dialog, click
OK
.
Open
Properties
for the newly created Netskope management console Relying Party Trust object in ADFS. Select the
Signature
tab, click
Add
, locate and select the Netskope SAML Certificate file, and then click
OK
.
Run the below PowerShell commands to disable the CRL Check:
PS C:UsersAdministrator> Set-ADFSRelyingPartyTrust -TargetIdentifier <org_key> -SigningCertificateRevocationCheck None
PS C:UsersAdministrator> Set-ADFSRelyingPartyTrust -TargetIdentifier <org_key> -EncryptionCertificateRevocationCheck None
ADFS is now configured for Netskope SSO. Proceed to the
Configure Netskope SSO for ADFS
section to complete the integration.
In this Topic
Configure ADFS for Netskope SSO Manually

---
## Configure ADFS for Netskope SSO using the Metadata File
**URL:** https://docs.netskope.com/en/configure-adfs-for-netskope-sso-using-the-metadata-file/
**Last Modified:** 2025-08-31T01:38:37+00:00
**Scraped:** 2026-08-03T09:51:36.874328+00:00

Configure ADFS for Netskope SSO using the Metadata File - Netskope Knowledge Portal
Configure ADFS for Netskope SSO using the Metadata File
To complete these steps, you need the Netskope Metadata file. Go to
Settings > Administration > SSO
, and under Netskope Settings, click
Download Netskope Metadata
. Save the file for later reference.
Add the Netskope admin console as a relying party trust. Open the ADFS Management window and right click the
Relying Party Trusts
folder, and then click
Add Relying Party Trust
.
Enable
Claims aware
and click
Start
.
For Select Data Source, select
Import data about the relying party from a file
and browse to select the file. When finished , click
Next
.
For Display name, enter a meaningful name, like
Netskope_SSO
, and then click
Next
.
For Configure Multi-factor Authentication Now, enable the
I do not want to configure….
option, and then click
Next
.
For Choose Insurance Authorization Rules, enable the
Permit all users to access…
, option, and then click
Next
.
For Ready to Add Trust, the wizard displays the configured settings. Click
Next
.
Enable the
Open the Edit Claims dialog …
checkbox and click
Close
.
In the Edit Claim Rules dialog, click
Add Rule
.
For Choose Rule Type in the Add Transform Claim Rule Wizard, select
Send LDAP attributes as Claims
as the Claim Rule Template so claims contain LDAP attribute values from the AD attribute store. Click
Next
.
For Configure Claim Rule, enter and select the following:
Enter a name for the claim rule.
For Attribute Store, select
Active Directory
.
Map the LDAP attributes that represent the user’s login name to a field in the outgoing claim. In the LDAP attribute column, select
User-Principal-Name
. In the Outgoing Claim Type column, select or enter
Name ID
. (Note that Name ID is entered as two words, with a space between them).
Click
Finish
.
Click Add Rule and add another Claim Issuance Policy rule.
For Choose Rule Type, select
Send Group Membership as a Claim
, as the Claim Rule Template, and then click
Next
.
For Configure Claim Rule, enter and select the following:
Enter a name for the claim rule, like
Tenant_Admin
.
For User’s Group, browse and select the AD group that will be mapped to the Tenant Admin role in the Netskope UI.
For Outgoing Claim Type, select
Group
.
For Outgoing Claim Value, enter
Tenant Admin
.
In this rule, users in the
Tenant_admin
group are mapped to the predefined
Tenant Admin
role on the Netskope UI.
Note
Create a group claim role for each role present in the Netskope UI under Administration, both predefined and custom, if those roles are being used.
Click
Finish
.
Add another Claim Issuance Policy rule. For Choose Rule Type, select
Transform an Incoming Claim
, as the Claim Rule Template, and then click
Next
.
For Configure Claim Rule, enter and select the following:
Enter a name for the claim rule, like
admin role
.
For Incoming Claim Type, select
Group
.
For Outgoing Claim Type, select
admin-role
.
Enable
Pass through all class values
.
In this rule, users in the
admin role
group are mapped to the pre-defined
Tenant Admin
role on the Netskope UI. Click
Finish
.
In the Edit Claim Rules dialog, the Transform incoming rule should be the last rule. When so, click
OK
.
Note
Configure further roles as needed.
Run the below PowerShell commands to disable the CRL Check:
PS C:UsersAdministrator> Set-ADFSRelyingPartyTrust -TargetIdentifier <org_key> -SigningCertificateRevocationCheck None
PS C:UsersAdministrator> Set-ADFSRelyingPartyTrust -TargetIdentifier <org_key> -EncryptionCertificateRevocationCheck None
ADFS is now configured for Netskope SSO. Proceed to the
Configure Netskope SSO for ADFS
section to complete the integration.
In this Topic
Configure ADFS for Netskope SSO using the Metadata File

---
## Configure an Enterprise Application in Microsoft Azure Active Directory for SAML Auth
**URL:** https://docs.netskope.com/en/configure-an-enterprise-application-in-microsoft-azure-active-directory-for-saml-auth/
**Last Modified:** 2025-09-01T13:15:49+00:00
**Scraped:** 2026-08-03T09:51:40.241067+00:00

Configure an Enterprise Application in Microsoft Azure Active Directory for SAML Auth - Netskope Knowledge Portal
Configure an Enterprise Application in Microsoft Azure Active Directory for SAML Auth
Log in to the Microsoft Azure portal
https://portal.azure.com
Go to
Azure Active Directory > Enterprise Applications > All Applications
and click
New application
.
Enter
Netskope
in the search bar. Select
Netskope User Authentication
. Enter a name, like
Netskope FP SAML Auth
, (for example). Click
Create
.
Note
If you are still using the old app gallery experience, then:
Select
Netskope User Authentication
.
Enter a name, like
Netskope FP SAML Auth
, (for example).
Click
Add
.
Select
Single sign-on > SAML
.
Click
Edit
to enter the Basic SAML Configuration parameters.
Enter
Netskope Entity ID
and
Netskope ACS URL
copied from the Netskope UI in the required fields, and then click
Save
.
Click on the
x
icon to close SAML section.
You will be prompted to test SSO. Select
No, I’ll test later
.
Go to and edit User Attributes & Claims section.
Delete all the default Additional claims. You only need the Required Claim.
Select the value to edit the Unique User Identifier (Name ID) field.
Set the Source attribute as
user.mail
and click
Save
.
user.mail
is set as the claim value for Name ID. Click on the
x
to close this section.
Download the certificate in
Certificate (Base64)
format, and copy the
Login URL
and
Azure AD Identifier
values. These need to be entered into the Netskope Forward Proxy – SAML settings page later on.
Next assign users who will log in using the Azure SAML Auth.
Go to
Users and groups > Add user/group
.
Select
Users and groups
.
Select the users, and then click
Select
.
Click
Assign
.
If you want to use Group assignments, then you need at least a Microsoft P2 license or above. This may not apply in the future if Microsoft updates their software licensing models.
The User has been successfully assigned to the SAML Auth application.
Log off the Azure portal.
In this Topic
Configure an Enterprise Application in Microsoft Azure Active Directory for SAML Auth

---
## Configure Google IdP for Netskope SAML Forward Proxy
**URL:** https://docs.netskope.com/en/configure-google-idp-for-netskope-saml-forward-proxy/
**Last Modified:** 2025-08-31T01:55:36+00:00
**Scraped:** 2026-08-03T09:51:42.438708+00:00

Configure Google IdP for Netskope SAML Forward Proxy - Netskope Knowledge Portal
Configure Google IdP for Netskope SAML Forward Proxy
This procedure involves using the Netskope UI and Google Console simultaneously, so use separate browser tabs to change between them between some of the steps. Also have a text editor handy with the Netskope SAML settings you copied previously; you’ll be copying and pasting some Google settings during this process as well.
Log in to the Google Workspace Admin Console as a Super Administrator.
Click
Apps
.
Click
SAML Apps
.
Select
Add App > Add custom SAML app
Enter a unique name.
Optionally you can upload a logo. When finished, click
Continue
.
Copy the SSO URL and paste in a text editor.
Copy the Entity ID and paste in a text editor.
Copy the Certificate and paste in a text editor.
In the Netskope tenant, go to
Settings > Security Cloud Platform > Forward Proxy > SAML
Select
Add Account
and enter these parameters:
Name: Enter a descriptive name.
IDP URL: Paste the SSO URL copied from Google.
IDP Entity ID: Paste the Entity ID copied from Google.
IDP Certificate: Paste the Certificate copied from Google.
When finished, click
Save
.
In the Google console, click
Continue
and enter these parameters:
ACS URL: Paste the SAML ACS URL copied from the Netskope UI (in the first section).
Entity ID: Paste the SAML Entity ID copied from the Netskope UI.
Leave everything else as default and select
Continue
.
On the Attributes page, select
Finish
.
Ensure Service Status is
On for Everyone
.
In the Netskope tenant, go to
Settings > Security Cloud Platform > Forward Proxy > Authentication
and click
Enable Authentication
.
Activate the Enable toggle, select the SAML Account created in step 10, and then click
Save
.
In this Topic
Configure Google IdP for Netskope SAML Forward Proxy

---
## Configure Netskope SAML for ADFS
**URL:** https://docs.netskope.com/en/configure-netskope-saml-for-adfs/
**Last Modified:** 2025-08-31T01:55:40+00:00
**Scraped:** 2026-08-03T09:51:48.191734+00:00

Configure Netskope SAML for ADFS - Netskope Knowledge Portal
Configure Netskope SAML for ADFS
Log in to the Netskope UI (
https://
<tenant_hostname>
.goskope.com
) and go to:
Settings > Security Cloud Platform > Forward Proxy > Add Account
. Add a new account with these settings:
Name: ADFS (for example)
IDP URL: The URL can be found from the meta data of the IDP. For example, for ADFS you can obtain it from the line:
SingleSignOnServiceBinding=…..HTTP-POST* Location=”https://adfs.test.com/adfs/ls/”
IDP Entity ID: The IDP Entity ID can also be found from the meta data of the IDP. For example, for ADFS you can obtain it from the line:
entityID=”https://adfs.test.com/adfs/services/trust”
IDP Certificate: Download the IDP certificate from the ADFS 2.0 Management window under
Certificates > Token Signing > Export in Base 64 encoded format
. Copy the certificate contents using a text editor into Netskope.
When finished, click
Save
.
Go to
Settings > Security Cloud Platform > Forward Proxy >Authentication
. Click
Enable Authentication
. Enable and select the SAML account created earlier. When finished, click
Save
.
In this Topic
Configure Netskope SAML for ADFS

---
## Configure Netskope SSO for ADFS
**URL:** https://docs.netskope.com/en/configure-netskope-sso-for-adfs/
**Last Modified:** 2025-08-31T01:38:39+00:00
**Scraped:** 2026-08-03T09:51:51.500826+00:00

Configure Netskope SSO for ADFS - Netskope Knowledge Portal
Configure Netskope SSO for ADFS
To complete these steps, you need the IdP URL, the IdP Entity ID, and the IdP certificate from ADFS. The IdP URL and IdP Entity ID can be found by browsing the federation metadata URL on the ADFS server (ex.
https://
<adfs domain>
/FederationMetadata/2007-06/FederationMetadata.xml
). The URL can be found from the meta data of the IdP. Copy the value of the EndpointReference (ex.
https://
<adfs domain>
/adfs/ls
). For example, for ADFS you can obtain it from the line:
SingleSignOnServiceBinding=…..HTTP-POST* Location=”https://adfs.test.com/adfs/ls/”
The IdP Entity ID can also be found from the ADFS metadata. For example, for ADFS you can obtain it from the line:
entityID=”https://adfs.test.com/adfs/services/trust”
Download the IdP certificate from the ADFS 2.0 Management window under
Certificates > Token Signing > Export in Base 64 encoded format
.
Log in to the Netskope UI and go to:
Settings > Administration > SSO
. Scroll down the page and click
Edit Settings
.
Enter and select the following:
Enable SSO: Enable this checkbox.
Sign SSO Authentication Request: Enable this checkbox.
Note
Do not disable this option. If you do not want to sign the authentication request, disable this in ADFS and run this command in the PowerShell:
PS C:UsersAdministrator> Set-ADFSRelyingPartyTrust -TargetIdentifier <org_key> -SignedSamlRequestsRequired$false
IdP URL: Enter the IdP URL from ADFS.
IdP Entity ID: Enter the IdP Entity ID from ADFS.
IdP Certificate: Paste the certificate contents from ADFS.
Click
Submit
.
Admin User Experience
When admin users go to the Netskope tenant URL, they will be redirected to the ADFS log in page for authentication. Once they authenticate using ADFS, they will be single signed on from ADFS to the Netskope UI and be mapped automatically to their assigned admin roles.
To Disable SSO
Once this feature is turned on, the Netskope UI no longer allows ANY local authentication. You have to go to a specific URL (
https://
<tenant_URL>
/locallogin
) and log in as tenant admin to turn this feature off.
In this Topic
Configure Netskope SSO for ADFS

---
## Configure the Netskope Plugin with SailPoint IdentityIQ
**URL:** https://docs.netskope.com/en/configure-the-netskope-plugin-with-sailpoint-identityiq/
**Last Modified:** 2025-08-31T01:55:39+00:00
**Scraped:** 2026-08-03T09:51:58.128608+00:00

Configure the Netskope Plugin with SailPoint IdentityIQ
The Netskope Plugin provides an easy way to generate alerts for use in IdentityIQ. When installed, Identity administrators can specify which information Netskope sends to IdentityIQ in order to create alerts, as well as what actions IdentityIQ should take based on the content of those alerts. In addition to creating Netskope policy alerts, the plugin also provides an interface to view all the upstream ‘sources’ that generated the initial alert in Netskope.
To watch a video about how to integrate the Netskope plugin with Identity IQ, click play:
For installation instructions, go to:
Netskope Plugin – Installation and User Guide
.
In this Topic
Configure the Netskope Plugin with SailPoint IdentityIQ

---
## CrowdStrike Falcon Identity Protection Plugin for User Risk Exchange
**URL:** https://docs.netskope.com/en/crowdstrike-falcon-identity-protection-plugin-for-user-risk-exchange/
**Last Modified:** 2026-05-28T00:23:50+00:00
**Scraped:** 2026-08-03T09:52:20.852310+00:00

CrowdStrike Falcon Identity Protection Plugin for User Risk Exchange - Netskope Knowledge Portal
CrowdStrike Falcon Identity Protection Plugin for User Risk Exchange
This document explains how to configure the CrowdStrike Identity Protect URE integration with the User Cloud Risk Exchange module of the Netskope Cloud Exchange platform. This integration collects user email and their scores from CrowdStrike’s Identity Protection platform to Netskope.
Prerequisites
To complete this configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Risk Exchange
plugin already configured.
Your CrowdStrike instance credentials (Base URI, Client ID, Client Secret) for the API Token.
Permissions for the plugin.
Connectivity to the following hosts:
https://api.crowdstrike.com (Commercial cloud
api.crowdstrike.com
)https://api.us-2.crowdstrike.com (US 2
api.us-2.crowdstrike.com
)https://api.laggar.gcw.crowdstrike.com (Falcon on GovCloud
api.laggar.gcw.crowdstrike.com
)https://api.eu-1.crowdstrike.com ( EU cloud
api.eu-1.crowdstrike.com
)
Note
You need any one of the URLs as mentioned above for the plugin.
Actions
Fetched record types
Users
Actions
No Actions
Mappings
Score Pull
CrowdStrike Fields
Netskope CE Fields
emailAddresses
uid (Email)
riskScore
score
Note:
The user score you’ll see will be different from what you see in the CrowdStrike Identity Protection Platform.
Formula to convert CrowdStrike’s Identity Protection Risk Score to Netskope Cloud Exchange Risk score
Netskope Risk Score scale: 0 – 1000 (0-maximum risk 1000- minimum risk)
CrowdStrike Risk score scale: 0 – 1 ( 0 -> minimum risk 1 -> maximum risk)
Formula: |(1 – (CrowdStrike Identity Protection Risk Score))| *1000
Permissions
Here are the permissions needed for the URE CrowdStrike Falcon Identity Protection plugin.
Scope
Read
Write
Identity Protection GraphQL
–
Yes
Identity Protection Timeline
Yes
–
Identity Protection Entities
Yes
No
Performance Matrix
Here is the performance reading conducted on a Large CE Stack by pulling 50K User scores from CrowdStrike to Netskope CE.
Stack details
Size: Large RAM: 32 GB CPU: 16 Cores
Users fetched from third-party product
~10K per minute
User Agent
netskope-ce-4.1.0-ure-crowdstrike_identity_protect-v1.0.0
Workflow
Create your CrowdStrike API credentials.
Configure the Crowdstrike Plugin for User Risk Exchange.
Configure Business Rules for the CrowdStrike plugin.
Configure Actions for the CrowdStrike plugin.
Validate the CrowdStrike plugin.
Click play to watch a video.
Create CrowdStrike API Credentials
Log in into your Crowdstrike platform. Go to the
Menu Icon > Support
and then
Resources > API Clients and Keys
.
Click
Add New API Client
.
Add the following scopes while adding the API Client:
Scope
Read
Write
Identity Protection GraphQL
–
Yes
Identity Protection Timeline
Yes
–
Copy the Base URL, Client ID, and Client Secret.
Save your changes.
Configure the CrowdStrike Falcon Identity Protection Plugin
In Cloud Exchange, go to
Settings > Plugins
. Search for and click on the CrowdStrike Falcon Identity Protection (URE) plugin box.
Add a Configuration Name, Sync Interval, and Use System Proxy (if needed) for configuring the plugin.
Click
Next
and enter the Base URL, Client ID, Client Secret, and an Initial Range.
Click
Next
and set the score range from the Select Range page (recommend that you keep the default).
Your plugin configuration will be seen in
User Risk Exchange > Plugins
.
Configure a User Risk Exchange Business Rule for CrowdStrike Falcon Identity Protection
Go to
User Risk Exchange > Business Rule
.
Click
Create New Rule
.
Enter the Rule Name and configure the query based on your requirements. The below example fetches all the users/hosts fetched by the CrowdStrike Identity Protection configuration.
Click
Save
.
Configure Actions for CrowdStrike Falcon Identity Protection
The User Risk Exchange CrowdStrike plugin supports the following action types:
No Action: This action does not perform any action on the host but can generate alerts in CTO if generate Alerts is enabled.
To configure this action:
Go to
User Risk Exchange > Actions
.
Click
Add Action Configuration
.
Select a Business Rule, a plugin configuration, and leave the default action.
To generate Alerts in the Ticket Orchestrator module, enable
Generate Alert
, and similarly, enable
Perform Action during Maintenance Window
if you wish to perform this action during the Maintenance Window.
Click
Save
.
Validate the CloudStrike Falcon Identity Protection Plugin
Validate Pull in Cloud Exchange
Go to the
User Risk Exchange > Users
.
You’ll see users similar to what is shown below.
Verify the same from plugin logs. Go to
Logging
and search for logs from the CrowStrike Falcon Identity Protection plugin.
Note
The user score you’ll see will be different from what you see in the CrowdStrike Identity Protection Platform.
Formula to Convert CrowdStrike’s Identity Protection Risk Score to Netskope Cloud Exchange Risk Score
Netskope Risk Score scale: 0 – 1000 (0-maximum risk 1000- minimum risk)
CrowdStrike Risk score scale: 0 – 1 ( 0 -> minimum risk 1 -> maximum risk)
Formula: |(1 – (CrowdStrike Identity Protection Risk Score))| *1000
Validate Pull in CrowdStrike Identity
Log in to CrowdStrike Falcon platform.
Go to
Identity Protection > Users
.
Here you’ll see the users. As shown in the below screenshot.
Troubleshooting
Unable to pull user score from the CrowdStrike platform.
If you are unable to pull any user scores, it could be one of the following.
No Users are available to be pulled.
Insufficient plugin permission was provided to the Client ID and Client Secret.
The API response has no value in the “emailAddresses” field.
The API response has multiple email addresses in the “email-addresses” field.
What to do:
No Users are available to be pulled.
Check the CrowdStrike platform to see if the users are available to be pulled from the steps provided in the Crowdstrike validation. Only Unarchived users are pulled from the CrowdStrike platform.
Insufficient plugin permission was provided to the Client ID and Client Secret.
Verify the permissions required for the plugin.
In this Topic
CrowdStrike Falcon Identity Protection Plugin for User Risk Exchange

---
## Disable the Re-Sign SAML Assertion
**URL:** https://docs.netskope.com/en/disable-the-re-sign-saml-assertion/
**Last Modified:** 2025-08-31T01:55:01+00:00
**Scraped:** 2026-08-03T09:52:21.969467+00:00

Disable the Re-Sign SAML Assertion - Netskope Knowledge Portal
Disable the Re-Sign SAML Assertion
If you are working within a new Okta environment, log into your Netskope tenant to disable the Re-Sign SAML Assertion setting following the steps below.
Go to
Settings > Security Cloud Platform > Reverse Proxy > SAML
.  Select the configuration icon (circled below).
Disable the Re-Sign SAML Assertion.
Click
Save
.
In this Topic
Disable the Re-Sign SAML Assertion

---
## Enable Authentication and Configure SSO Domain Bypass Settings
**URL:** https://docs.netskope.com/en/enable-authentication-and-configure-sso-domain-bypass-settings/
**Last Modified:** 2025-08-31T01:55:19+00:00
**Scraped:** 2026-08-03T09:52:25.357609+00:00

Enable Authentication and Configure SSO Domain Bypass Settings - Netskope Knowledge Portal
Enable Authentication and Configure SSO Domain Bypass Settings
Go to
Settings > Security Cloud Platform > Forward Proxy > Authentication
and click
Enable Authentication
.
Activate
Enabled
, select the account, and then click
Save
.
Click
OK
.
Authentication is enabled.
Go to the
Domain Bypass
section and click
Edit
.
Enter these URLs in comma-separated format.
login.microsoftonline.com,nsauth-
<tenant-URL>
,aadcdn.msauth.net
Click
Save
.
Important
These URLs need to be bypassed from authentication; otherwise, the services that perform the SAML Auth itself will get prompted for auth, go into a continuous loop, and the auth page will not load. Wildcards (like *.tld) are not valid.
Click
OK
.
Review the settings.
Log out of the Netskope tenant.
In this Topic
Enable Authentication and Configure SSO Domain Bypass Settings

---
## Get Netskope SAML Settings
**URL:** https://docs.netskope.com/en/get-netskope-saml-settings/
**Last Modified:** 2025-09-01T13:15:49+00:00
**Scraped:** 2026-08-03T09:52:30.871409+00:00

Get Netskope SAML Settings - Netskope Knowledge Portal
Get Netskope SAML Settings
Log in to your tenant WebUI
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
.
Click the
Netskope Settings
button to view and copy the
Entity ID
,
Proxy ACS URL
and
SAML Certificate
details of the IdP account.
In this Topic
Get Netskope SAML Settings

---
## Get the Netskope SAML Settings
**URL:** https://docs.netskope.com/en/get-the-netskope-saml-settings/
**Last Modified:** 2025-08-31T01:55:36+00:00
**Scraped:** 2026-08-03T09:52:33.076572+00:00

Get the Netskope SAML Settings - Netskope Knowledge Portal
Get the Netskope SAML Settings
Log in to the Netskope UI.
Go to
Settings > Security Cloud Platform > Forward Proxy > SAML
. Copy the SAML Entity ID and SAML ACS URL to a text editor. These will be used to configure Google SAML Auth later in the integration.
In this Topic
Get the Netskope SAML Settings

---
## Netskope Explicit Proxy for Chromebooks with Google SAML Forward Proxy
**URL:** https://docs.netskope.com/en/netskope-explicit-proxy-for-chromebooks-with-google-saml-forward-proxy/
**Last Modified:** 2026-06-12T06:02:12+00:00
**Scraped:** 2026-08-03T09:53:22.417917+00:00

Netskope Explicit Proxy for Chromebooks with Google SAML Forward Proxy - Netskope Knowledge Portal
Netskope Explicit Proxy for Chromebooks with Google SAML Forward Proxy
This document explains how to configure Google SAML forward proxy and Chromebook for protection using explicit proxy. SAML forward proxy is required to provide identity to traffic reaching our edge from the Cloud explicit proxy.
Refer the
Mutiple and Concurrent IdP
section for for detailed information on .
Prerequisites
To perform these instructions you first need:
A Google G Suite Account with a license that includes access to the admin console (Business, Enterprise, Education)
A domain name.
Access to
admin.google.com
to your G Suite account.
At least one Chromebook that is managed by your G Suite account.
A Netskope tenant with a web license and explicit proxy enabled.
Steps to Integrating Proxy with Chromebooks
Configure SAML Forward Proxy for Google
Configure Explicit Proxy for Managed Chromebook Devices
Configure SAML Forward Proxy for Google
Log in to the Netskope UI and go to
Settings
>
Security Cloud Platform
>
Traffic Steering
>
Explicit Proxy
(
will only display if you have Explicit Proxy enabled
).
Add the IP address(es) traffic will egress the network from Public IP.
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
and click
New Account
. Configure your IdP account by following the steps mentioned in
Mutiple and Concurrent IdP
section.
In another browser tab, log in to the Google management console admin.google.com, go to
Apps
>
SAML Apps
,and then click
Add App
and select
Add custom SAML app
.
Enter Netskope for the name, optionally add a logo, and then click
Continue
.
A window with the Google IdP information opens. Copy the
SSO URL
and
Entity ID
, and then download the certificate.
Return to the Netskope Add SAML Account window and do the following:
Enter the the following when creating a new IdP Account:
Name
: IdP Name
Access Method
:  Select Cloud Explicity Proxy or All (as per your requirement)
SSO URL
(IdP URL in the Netskope Console)
Entity Id
Upload
IdP certificate
. To get the certificate you downloaded, open it in your favorite text editor to copy and paste it here.
Leave the other fields blank, and then click
Save
.
Next, go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
. To get the service provider details (specific to the IdP account) needed in the next step, click Netskope Settings to view the
SAML Entity ID
and
ACS URL
.
Return to the Google admin console and click
Continue
, which opens the Service Provider Details screen. Enter the
ACS URL
and
Entity ID
, and then click
Continue
.
The ACS URL is the 2nd item in the Netskope console, but the 1st item in the Google Admin Console.
Leave the Attribute Mapping screen blank and click
Finish
.
In the Netskope UI, go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
.
Under
Settings
>
BYPASS
>
Domain Bypass
add
accounts.google.com
. Go to the IDP Account in previous step, click on more options (3 dots) >
Enable
. . At this point SAML forward proxy is ready to go.
In order to test, you need an endpoint that is pointing to the explicit proxy. You can test with a device, or proceed to to the next section to configure explicit proxy on your Chromebook devices.
Configure Explicit Proxy for Managed Chromebook Devices
Install the Netskope certificates in Google, then choose method 1 or 2 to configure your proxy settings.
Install Certificates
Regardless of the method you choose you will need the Netskope root cert on end user devices. Luckily
admin.google.com
allows us to mass install this for managed devices.
In the Netskope UI, go to
Settings
>
Manage
>
Certificates
>
Signing CA
and download all 3 certificates (this will ensure decryption works whether or not you have an IP whitelisted in the tenant).
In admin.google.com , go to
Devices
>
Networks
and click
Certificates
>
Add Certificate
to add each cert one at a time.
Upload the Netskope Root Certificate, enable
Chromebook
in the Certificate Authority section, and then click
Save
. This certificate is automatically pushed to all managed ChromeOS devices.
Method 1: Configure Proxy Settings in the Google Admin Console
This method will work regardless of the Wifi Network/Browser a user tries to use on the ChromeOS device, but will ONLY work for Managed ChromeOS devices and not any other OS.
In admin.google.com, go to
Devices > Chrome > Settings > User
, and in browser settings, select
Network
.
Under Proxy mode, changet to Always use the proxy specified below. For Proxy Server URL, copy the URL from your Netskope tennant under
Settings
>
Security Cloud Platform
>
Traffic Steering
>
Explicit Proxy
. Be sure to remove
https://
(
Leave everything else default
.)
If any URLs need to be bypassed from being sent to the proxy, add them here. IP addresses and CIDR blocks also work. You’ll also need to add bypasses for the SSO of your choice, accounts.google.com works for Google SSO. These are the suggested bypasses for ChromeOS:
client1.google.com client2.google.com client3.google.com client4.google.com client5.google.com client6.google.com commondatastorage.googleapis.com cros-omahaproxy.appspot.com dl-ssl.google.com dl.google.com gweb-gettingstartedguide.appspot.com m.google.com hangouts.google.com omahaproxy.appspot.com pack.google.com safebrowsing-cache.google.com safebrowsing.google.com ssl.gstatic.com storage.googleapis.com tools.google.com www.googleapis.com ww.gstatic.com play.google.com mtalk.google.com accounts.google.com connectivitycheck.gstatic.com
When done adding bypasses, wait a few minutes, then on your ChromeOS device, check under
Settings
>
Network
. Click on your Wifi Network and you should see the proxy settings.
Visit some Google cloud apps, and then you should see the Access Method as Explicit Proxy in Skope IT details in your Netskope tenant.
Method 2: Configure a Hosted PAC File
The Google Admin console only supports hosted PAC files. Netskope plans to support this option in the tenant in a later release. For now you can host it on a 3rd-party site.
In your Netskope tenant, go to
Settings
>
Security Cloud Platform
>
Traffic Steering
>
Explicit Proxy
and click
Download Sample PAC File
.
A file called
sample.pac
will be downloaded.  Open this file in a text editor of your choice, and use this file as a template to create a new PAC file that will steer traffic.
Substitute
domain-example1.com
and
domain-example2.com
with the exceptions (bypassed sites) you need. This will allow the endpoint to reach Okta for authentication directly and not be sent via Cloud Explicit Proxy. This is not a requirement, but is done to illustrate how a PAC file is used to send some traffic directly and other traffic to the Cloud Explicit Proxy.
Substitute
proxy-
<tenant-URL>
with your tenant name and save your changes.
In this Topic
Netskope Explicit Proxy for Chromebooks with Google SAML Forward Proxy

---
## Netskope Forward Proxy over IPSec/GRE with Azure AD SAML Auth
**URL:** https://docs.netskope.com/en/netskope-forward-proxy-over-ipsec-gre-with-azure-ad-saml-auth/
**Last Modified:** 2025-08-31T01:55:17+00:00
**Scraped:** 2026-08-03T09:53:23.533099+00:00

Netskope Forward Proxy over IPSec/GRE with Azure AD SAML Auth - Netskope Knowledge Portal
Netskope Forward Proxy over IPSec/GRE with Azure AD SAML Auth
Netskope integrates with identity providers to gather user identity information for traffic steered through an IPSec or GRE tunnel. This guide explains how to configure Azure AD SAML Auth with Netskope Forward Proxy over IPSec or GRE tunnels. This guide does not cover how to configure an IPSec or GRE tunnel and installing Netskope certificates onto the devices connecting to the web via the tunnel. Refer to
IPSec
and
GRE
to configure your tunnels and install certificates on devices before proceeding with these instructions.
Workflow
The integration requires the following steps in the order specified.
Get Netskope SAML settings.
Configuring an Enterprise Application in Microsoft Azure Active Directory for SAML Auth.
Add account in Netskope SAML – Forward Proxy.
Enable authentication and configure SAML Auth domain bypass settings.
Test SAML Auth via IPSec or GRE tunnel
Check Skope IT events
Bypass SAML Auth Authentication
Get Netskope SAML Settings
Configure an Enterprise Application in Microsoft Azure Active Directory for SAML Auth
Add an Azure AD Account in Netskope SAML – Forward Proxy
Enable Authentication and Configure SSO Domain Bypass Settings
Test SSO via the IPSec or GRE Tunnel
Check Skope IT Events
Bypass SAML Forward Proxy Authentication Methods
Tips and FAQs
In this Topic
Netskope Forward Proxy over IPSec/GRE with Azure AD SAML Auth

---
## Single Sign On with Okta
**URL:** https://docs.netskope.com/en/sso-with-okta/
**Last Modified:** 2025-08-31T01:38:36+00:00
**Scraped:** 2026-08-03T09:53:39.128891+00:00

Single Sign On with Okta - Netskope Knowledge Portal
Single Sign On with Okta
Netskope integrates with multiple third-party applications to provide a wide range of solutions. You can configure single sign-on (SSO) on the Netskope Admin Console to connect to these applications with or without authentication. Using the SSO Enabled feature in the Netskope Admin Console, you can set up forced authentication when connecting to third-party applications through Okta.
In these instructions,
Netskope Admin Console
refers to the app in the Okta Applications Dashboard.
Netskope UI
refers to the Netskope tenant.
Click play to watch a video.
Locate the SSO Settings in Netskope UI
To access SSO/SLO Settings in your tenant, go to
Settings > Administration > SSO
.
To view and edit IdP settings, click
Edit Settings
.
Here are the IdP URL, IdP Entity ID, IdP Certificate. Copy the IdP Entity ID to use when generating new IdP information in Okta.
Generate New IdP Information in Okta
In the Okta Dashboard, go to
Applications > Browse App Catalog
.
Search for
Netskope
and select
Netskope Admin Console
.
Click
Add
.
Enter your subdomain in the subdomain field and click
Next
.
Scroll down to the Service Provider Entity ID field and enter the Service Provider EntityID from the Netskope UI, and then click
Done
.
Go to the Sign On tab.
Scroll down to SAML Signing Certificates and click
View SAML setup instructions
.
Here are the IdP URL, IdP Entity ID, IdP Certificate to be copied into Netskope UI.
Copy the new IdP information from Okta and enter them into the Netskope IdP fields.
In the Netskope UI, go to
Settings > Administration > SSO
and under SSO/SLO click
Edit Settings
. Enter your Okta information and click
Save
.
Go to the Assignments tab and click
Assign > Add People/Group
, and then add users/groups who need access to the Netskope Admin Console.
Deactivate any old instances of Netskope Admin Console from Okta Applications Dashboard.
Provision Custom Roles with Okta using the Netskope Admin Console
Integrate Okta with Netskope so that Admins can access the Netskope Admin Console. The integration uses the Netskope Admin Console App (available in Okta), to provision users based on Custom Groups defined in Okta.
Provisioning Custom Admin Roles
This remaining sections explain how to assign custom roles to Netskope Admins that are provisioned via Okta. This does not work for local admin accounts. Using a predefined role like “Tenant Admin” will only allow you to provision admins with this role, so you need to have a more scalable way to assign different roles to admins that are provisioned through Okta.
Prerequisites
In order to complete this section, you must first:
Have existing Okta and Netskope Admin accounts
Enable SSO for your Netskope tenant
Deploy the Netskope Admin Console App in Okta
Create Custom Roles in Netskope
First confirm you have created your custom roles within Netskope. These roles need to have a similar naming convention as shown for this integration to work. Because you will use a contains statement within the Okta App, it’s important to prefix each custom role with an identical value. For example:
ns
tenant admin
ns
delegated admin
The prefix
ns
should be there for all custom roles. Assign whatever attributes you like for each custom role.
Create Custom Groups within Okta
Now create the custom Groups inside Okta. These groups should match what you just created within Netskope.
Go to
Directory > Groups > Add Group
.
Check to ensure the prefix
ns
is there for all custom Groups that you will assign Admins to.
Assign admins to their respective group based on the roles you assigned for each group within Netskope.
Define the Admin Role Attribute in the Netskope Admin Console
Now set the admin-role attribute to
ns
in the Netskope Admin Console App withing Okta.
Open the Netskope Admin Console, go to the Sign On tab and click
Edit
.
Set the admin-role attribute under SAML 2.0 to:
Starts with
and
ns
,and then click
Save
.
The integration to assign custom roles for Netskope admins via Okta is complete.
In this Topic
Single Sign On with Okta

---
## Single Sign On with Entra ID
**URL:** https://docs.netskope.com/en/sso-with-entra-id/
**Last Modified:** 2026-05-06T13:54:39+00:00
**Scraped:** 2026-08-03T09:53:40.243370+00:00

Single Sign On with Entra ID
Single Sign On with Microsoft Entra ID
This document explains how to configure Microsoft Entra ID for Single Sign On (SSO) to the Netskope tenant. Netskope now offers a gallery application in Microsoft Entra ID for both admin SSO and user provisioning via SCIM.
This document covers configuring the Microsoft Entra ID gallery application for Admin SSO.
Prerequisites
You will need the following:
An Microsoft Entra ID subscription that supports Enterprise Applications.
A Netskope tenant.
An Microsoft Entra ID user with which to test functionality.
Workflow
Create an Enterprise Application and configure SSO in Azure AD.
Configure SSO parameters between Netskope and Azure AD.
Assign Users and/or Groups to the Netskope application in Azure AD.
Configuring SSO in Microsoft Entra ID admin center and Netskope
Login to Microsoft Entra admin center
Select
Enterprise Applications
>
New Application
Search for
Netskope
and select
Netskope Administrator Console
In the
Netskope Administrator Console
page, select
Set up single sign on
In the SAML Sign on page, click the pencil icon to add
Basic SAML Configuration
details.
You can get these details from your tenant WebUI. In your tenant WebUI go to
Settings
>
Administration
>
SSO
page.
Identifier (Entity ID)
–
Service Provider Entity Id
from your tenant WebUI
Reply URL (Assertion Consumer Service URL)
–
Reply URL
from your tenant WebUI
Logout URL
–
Netskope Single Logout Service Request URL
from your tenant WebUI
Configure SSO Parameters between Netskope and Azure AD
If you want to map specific Netskope administrator roles to Entra ID users or groups during the SSO process, you must first ensure those roles exist in Netskope.
This step is optional if you are not using dynamic role mapping.
To create a custom role, go to
Settings
>
Administration
>
Roles
and click
New Role
. Create a new Role with no blank spaces in the name, like
DelegatedAdmin
, and then add a description and select the desired settings (
Privileges, Scopes, etc.
). Save the Role, and then use this role name for the Users/Groups value.
For more details about Netskope Roles, go
here
. For Microsoft documentation and best practices, go
here for Graph API
and
here for GUI
information.
In the
Netskope Administrator Console
page in Microsoft Entra ID, go to
Permissions
>
App Registration
.
Create app role. In the
Netskope Administrator Console API permissions
page, go to
App Roles
>
Create app role
.
In the
Create App Role
pop-up, enter the
Display Name
, select
Allowed member types
, enter
Value
, and provide a
Description
:
When creating an app role, enter the role
Value
that was created in your tenant WebUI.
Go to
Users and Groups
and click
Add user/group
. Select
users or groups
and then select a
role
. This role will be passed in the SAML assertion. When finished, click
Assign
.
Refresh the assignment page, if the newly created Role is not visible.
Go to
Single Sign-On
>
SAML-based Sign-on
, download the SAML Signing Certificate in Base64 format, and copy the Login URL, Azure AD Identifier, and the Logout URL.
In your Netskope WebUI, go to
Settings
>
Administration
>
SSO
>
SSO/SLO Settings
and select
Edit Settings
.
Check the boxes to
Enable SSO
and
Sign SSO Authentication Request
and copy the following from the Azure Portal Netskope Administrator Console to your Netskope tenant
From Azure
To Netskope
Login URL
IDP URL
Azure AD Identifier
IDP Entity ID
Certificate from the
SAML Sign On
Popup window.
Step 4 from the Configure SSO Parameters between Netskope and Azure AD
section.
IDP Certificate
Logout URL
IDP SLO URL
Assign Users and/or Groups to the Netskope Application in Azure AD
Go back to the Netskope Administrator Console Overview and select Users and groups.
In the
Add Assignment
page, under
Users and groups
click
None Selected
to search and add a user and then under
Select a role
click
None Selected
to select a role. Once selected, click
Assign
.
This completes the setup. You can test by logging in to your Netskope tenant and verifying that SSO works. You can also try an Azure AD initated login as both should work.
In this Topic
Single Sign On with Entra ID

---
## Single Sign On with ADFS
**URL:** https://docs.netskope.com/en/netskope-sso-with-adfs/
**Last Modified:** 2025-08-31T01:38:37+00:00
**Scraped:** 2026-08-03T09:53:41.338663+00:00

Single Sign On with ADFS - Netskope Knowledge Portal
Single Sign On with ADFS
Netskope SSO integration allows organizations to use an Identity Provider (IdP) for authentication and authorization purposes. Strong authentication mechanisms like multi-factor authentication, etc., may be used by the organization with their IdP. This results in a stronger authentication before an administrator can get access to the Netskope UI.
Integrating Netskope SSO with ADFS includes these steps:
Configure new AD groups or use existing groups based on the administrator role they will be mapped to in the Netskope UI. There will be a one-to-one mapping between the AD group and the Netskope administration role. Ensure administrators are assigned to only one of the designated AD groups being used.
Add a new relying party trust in ADFS for the Netskope admin console and configure a claim issuance policy in ADFS. There are two methods for this,
Configure ADFS for Netskope SSO using the Metadata File
or
Configure ADFS for Netskope SSO Manually
. Using the metadata file is recommended.
Configure the Admin SSO feature using the Netskope UI. This configuration guide uses ADFS as the identity and single sign on provider.
In this Topic
Single Sign On with ADFS

---
## Reverse Proxy for Atlassian with Azure AD SSO
**URL:** https://docs.netskope.com/en/reverse-proxy-for-atlassian-with-azure-ad-sso/
**Last Modified:** 2025-08-31T01:54:54+00:00
**Scraped:** 2026-08-03T09:53:58.469964+00:00

Reverse Proxy for Atlassian with Azure AD SSO - Netskope Knowledge Portal
Reverse Proxy for Atlassian with Azure AD SSO
Before using these instructions, go to
Configure Azure AD with Atlassian Cloud SSO
and configure SSO between Azure AD and Atlassian. You will need your ACS from Atlassian, IDP SSO URL from Azure AD, and your Azure certificate to complete these instructions.
After the SSO between Azure AD and Atlassian is successfully created, log in to your Netskope tenant. Go to
Settings > Security Cloud Platform > Reverse Proxy > SAML
, then click
Add Account
.
Add a name, select
Atlassian Accounts
, and then enter your ACS from Atlassian, IDP SSO URL from AzureAD, and Azure certificate. When finished, click
Save
.
Click
Netskope Settings
and copy the Organization ID, SAML Proxy IDP URL, SAML Proxy ACS URL, and SAML Proxy Issuer Certificate.
Open Atlassian on AzureAD, and replace the Reply URL (Assertion Customer Service URL) with the Netskope SAML Proxy ACS URL.
In Atlassian, go to
Administration > Security > Identity providers
, open the SSO configuration, and then click
View SAML Configuration
.
Replace the Identity Provider Entity ID with the Netskope Oganization ID.
Replace the Identity Provider SSO URL with the Netskope SAML Proxy IDP URL.
Replace the Public x509 Certificate with the Netskope SAML Proxy Issuer Certificate.
Click
Save
.
Now, when accessing Atlassian with the Netskope Client Disabled (or uninstalled – otherwise we will bypass the ACS), you will see the following:
In this Topic
Reverse Proxy for Atlassian with Azure AD SSO

---
## Reverse Proxy for ServiceNow with Azure AD SSO
**URL:** https://docs.netskope.com/en/reverse-proxy-for-servicenow-with-azure-ad-sso/
**Last Modified:** 2025-08-31T01:54:59+00:00
**Scraped:** 2026-08-03T09:54:03.487374+00:00

Reverse Proxy for ServiceNow with Azure AD SSO - Netskope Knowledge Portal
Reverse Proxy for ServiceNow with Azure AD SSO
If you don’t already have a ServiceNow instance, create one following the instructions
here
to integrate it with Azure AD.
For testing purposes, you can create a developer account and request an instance
here.
Important
When creating the instance, select
Yes
for IDE.
Configure SSO
After your instance has been created, you can access the ServiceNow UI by clicking
Start Building
.
Go to
All > System Definition
, click
Plugins
, and search for
Multiple Provider Single Sign-On Enhanced UI
.
After you press install, click
Activate
.
Note
Wait for the plugin to be installed. This may take a few minutes.
Click
Close & Reload Form
.
Go to
All > Multiple-Provider SSO > Administrator
and click
Properties
, and then enable ACR.
Set up
Multi-factor Authentication’
in Step 2, click
Save
, and then go back to Properties by pressing the link in Step 4.
Select
‘Enable multiple provider SSO’
&
‘Enable Auto importing of users from all identity providers into the user table’
then press
‘Save’
Note
After enabling SSO, you can disable ACR. Otherwise, you will be logged by AR user when the session expires.
Log in to Azure AD, go to
All Applications > New Application
, search for
ServiceNow
, and then create the new app.
Once the application is created, go to
Single Sign-On
, select
SAML
, and add your instance information.
Click
View step-by-step instructions
in Step 4.
Add your Admin credentials and click
Configure Now
.
If successful, this will create an SSO entry for Azure in ServiceNow that can be seenon
All > Multi-Provider SSO > Providers
.
If not, follow the manual configuration steps (in Step 5).
Important
The above SSO with Azure must be successful before continuing with Netskope configuration.
Configure Netskope Reverse Proxy ServiceNow
Go to Settings > Security Cloud Platform > Reverse Proxy SAML and click Add Account, and enter your ACS URL (instance information), IdP SSO (URL Azure), and Azure Certificate
Note
Your Azure certificate can be found here:
Enable
Emergency Bypass
while testing the connection.
Click
Netskope Settings
from your new SAML – Reverse Proxy,
Copy all the information in order to enter it in your ServiceNow instance.
The
Organization ID
is used for your ServiceNow
Identity Provider URL
.
The
SAML Proxy IDP URL
is used for your ServiceNow
Identity Provider’s AuthnRequest
.
The
SAML Proxy ACS URL
is used for your Azure AD
Reply URL
(Assertion Consumer Service URL).
The SAML Proxy Issuer Certificate is used for your ServiceNow
X.509 Certificate
.
Go to the X.509 Certificates section in ServiceNow and click
New
.
Copy the full content of SAML Proxy Issuer Certificate from step 4, paste it in PEM Certificate, and then click
Submit
.
The new certificate should appear on the X.509 Certificates page.
Your settings should look like this:
Test the connection. Save the new configuration by clicking
Active
.
Disable the emergency bypass option in the Netskope UI.
Go to the log in page, authenticate with Azure, and the URL should show the Netskope reverse proxy.
In this Topic
Reverse Proxy for ServiceNow with Azure AD SSO

---
## SAML Proxy
**URL:** https://docs.netskope.com/en/saml-proxy/
**Last Modified:** 2025-08-31T01:55:39+00:00
**Scraped:** 2026-08-03T09:54:05.669601+00:00

SAML Proxy
Netskope enables you to integrate with your existing proxy implementation to direct your traffic to the Netskope Cloud using these proxy integrations.
Universal Reverse Proxy
Forward Proxy with ADFS
Configure Blue Coat for Proxy Chaining
Configure Forcepoint for Proxy Chaining
Netskope Explicit Proxy for Chromebooks with Google SAML Forward Proxy
In this Topic
SAML Proxy

---
## SSO Configuration
**URL:** https://docs.netskope.com/en/sso-configuration/
**Last Modified:** 2025-10-31T02:18:06+00:00
**Scraped:** 2026-08-03T09:54:20.989608+00:00

SSO Configuration - Netskope Knowledge Portal
SSO Configuration
An Admin can enable and disable SSO, and configure IdP settings. Also your service provider’s details are displayed on the SSO Configuration page. This workflow is explained in vendor-specific detail in the
Okta
and
Entra ID
SSO articles.
Admins can configure SSO identity provider details and see service provider details. SSO can be enabled/disabled from
Settings > Users
, on the
SSO Configuration
tab.
Go to
Settings > Users
and click
SSO Configuration
.
Enter the Identity Provider information:
FieldDescription
Identity Provider Issuer URL
Identity Provider Issuer URL
Identity provider SSO URL
Identity provider single sign on URL
Identity provider SLO URL
Identity provider single logout URL
Public x509 Certificate
Public x509 Certificate string.
View Service Provider information (provided for configuration in the SSO dashboard).
Field
Description
Service Provider Entity ID
Service Provider Entity ID URL.
Service Provider ACS URL
Service Provider assertion consumer service URL.
Service Provider SLS URL
Service Provider single logout service URL.
Click
Save
.
Note that if you migrated the domain or IP address of the machine where Cloud Exchange is deployed, you will need to disable the SSO toggle, and then re-enable it in order for Cloud Exchange to apply the change. After this, you need to update your SSO vendor details (like Okta) with the updated details in the SSO Configuration tab in the Cloud Exchange UI. (For detailed steps, please refer to the bottom of this
troubleshooting page
.)
Configure Force Authentication
Go to
Settings > Users > SSO Configurations
.
If toggle is enabled, users will be forced to re-authenticate on every login of Cloud Exchange, even if they have a valid session.
In this Topic
SSO Configuration

---
## SSO Access for Netskope Support
**URL:** https://docs.netskope.com/en/sso-access-for-netskope-support/
**Last Modified:** 2026-05-28T00:31:11+00:00
**Scraped:** 2026-08-03T09:54:25.738661+00:00

SSO Access for Netskope Support - Netskope Knowledge Portal
SSO Access for Netskope Support
The Cloud Exchange has recently introduced support for additional Single Sign-On (SSO) options. This new functionality allows Netskope Support to efficiently troubleshoot your environments with the new SSO options. By leveraging these SSO options, our Support engineers can access customer environments without requiring their login credentials, ensuring a more secure and streamlined troubleshooting experience.
If Cloud Exchange is deployed on-premises, you may need to grant Support access to your instance to configure additional SSO options. This ensures a smooth configuration process, and enables Support to efficiently troubleshoot any issues. Netskope recommends that you provide detailed instructions or remote access to their instance to facilitate the configuration process.
Configure SSO in Cloud Exchange
Log in to Cloud Exchange.
Go to
Settings > Users > SSO Configurations
.
Enable the SSO toggle.
Make a note of these SSO Configurations.
Cloud Exchange Field
Example (http://10.50.3.24/)
Service Provider Entity ID
http://10.50.3.24/api/metadata?
sre
=true
Service Provider ACS URL
http://10.50.3.24/api/ssoauth?acs
sre
=true
Service Provider SLS URL
http://10.50.3.24/api/slslogout
You need to add
sre
as additional parameters in value.
Copy these variables. You need to add all these variables in the
docker-compose.yml
file.
Environment Variables
Description
SRE_IDP_IDENTITY_ID
Identity Provider Issuer ID
SRE_IDP_SSO_URL
Identity Provider single sign on URL.
SRE_IDP_SLO_URL
Identity Provider single logout URL.
SRE_IDP_X509_CERT
Public x509 Certificate
Run these commands to set environment variables.
Go into the existing
ta_cloud_exchange
directory.
Stop the CE containers.
$ ./stop
Open the
yml
file to set up environment variables.
Linux:
$ vi docker-compose.yml
Redhat:
$ sudo vi podman-compose.yml
Put the environment variables into core service in the
yml
file.
core: index.docker.io/%24%7BCORE_TAG%7D
image: index.docker.io/${CORE_TAG}
environment:
–
SRE_IDP_IDENTITY_ID=
<value>
–
SRE_IDP_SSO_URL=
<value>
–
SRE_IDP_SLO_URL=
<value>
–
SRE_IDP_X509_CERT=
<value>
Save the file.
Start the CE Services:
$ ./start
The Netskope Support now has the ability to access your Cloud Exchange through the
/netskopesso
endpoint using SSO.
Configure Force Authentication
Go to
Settings > Users > SSO Configurations
.
If toggle is enabled, the user will be forced to re-authenticate on every login of Cloud Exchange, even if they have a valid session.
In this Topic
SSO Access for Netskope Support

---
## Test SSO via the IPSec or GRE Tunnel
**URL:** https://docs.netskope.com/en/test-sso-via-the-ipsec-or-gre-tunnel/
**Last Modified:** 2025-08-31T01:55:20+00:00
**Scraped:** 2026-08-03T09:54:26.898980+00:00

Test SSO via the IPSec or GRE Tunnel - Netskope Knowledge Portal
Test SSO via the IPSec or GRE Tunnel
Before proceeding, ensure the Netskope certificates have been deployed onto the required devices.
Log onto the device configured to go through the Netskope IPSec or GRE tunnel and launch the browser. Enter any external website like
bbc.com
.
First you will get redirected to the Netskope SAML Auth proxy, which will then redirect you to the Azure SAML Auth login page, as shown here.
Enter your Azure ID and click
Next
.
Enter your password and click
Sign-in
.
Select
No
or
Yes
to continue.
Note
Read the
Appendix
section to learn more about token lifetime.
After successful login the website is displayed.
Check the SSL certificate; it should be the Netskope certificate.
In this Topic
Test SSO via the IPSec or GRE Tunnel

---
## Enable SAML Authentication on the DPoP Appliance
**URL:** https://docs.netskope.com/en/enable-saml-authentication-on-dpop-appliance/
**Last Modified:** 2026-06-10T17:47:52+00:00
**Scraped:** 2026-08-03T09:59:55.325765+00:00

Enable SAML Authentication on the DPoP Appliance - Netskope Knowledge Portal
Enable SAML Authentication on the DPoP Appliance
You can integrate Netskope’s DPoP appliance into your existing IdP deployment. When you enable SAML authentication on an appliance configured in explicit proxy mode, the user will be required to authenticate with your IdP server before their connection is sent to the origin server, for example, www.abc.com via the DPoP appliance.
The following diagram exhibits the flow of traffic between a user, IdP server and the origin server through the DPoP appliance.
In this diagram:
The user accesses the URL, server,cnn.com. The user traffic to this origin server gets routed to DPoP through PAC redirection.
DPoP redirects the traffic to the auth service in the cloud which redirects the user to the IDP server for authentication.
The user performs SAML authentication, and the IDP server generates SAML assertion to redirect the user back to the NS auth service.
Auth service redirects the user to the original URL, server.cnn.com and the traffic will get routed to DPoP.
DPoP extracts user info, performs policy evaluation, and applies the action accordingly.
To enable SAML authentication on a DPoP appliance,
Ensure that SAML Forward Proxy is enabled on your Netskope tenant. To learn more:
Forward Proxy Authentication
.
In the appliance CLI, enter configuration mode and run the following command.
set dataplane proxy-mode explicit saml-auth enable true
You can disable SAML authentication on the appliance by setting the value to false. Run the following command in configuration mode.
set dataplane proxy-mode explicit saml-auth enable false
In this Topic
Enable SAML Authentication on the DPoP Appliance

---
## Reverse Proxy for ServiceNow with Pingfed IdP
**URL:** https://docs.netskope.com/en/reverse-proxy-for-servicenow-with-pingfed-idp/
**Last Modified:** 2025-08-31T01:55:02+00:00
**Scraped:** 2026-08-03T10:03:05.417378+00:00

Reverse Proxy for ServiceNow with Pingfed IdP - Netskope Knowledge Portal
Reverse Proxy for ServiceNow with Pingfed IdP
This topic provides instructions to configure Netskope Reverse Proxy for ServiceNow with Pingfed IdP.
Recommendation
It is recommended to tether ServiceNow with Pingfed without Netskope SAML Proxy before proceeding with configuration.
Netskope SAML Reverse Proxy configuration
Login to Netskope Tenant webUI and go to
Settings
>
Security Cloud Platform
->
Reverse Proxy
->
SAML
.
Add an account by selecting the
ServiceNow
from the
APPLICATION
option.
ACS URL
– Service Now ACS URL
IDP SSO URL
– Pingfed SSO URL
IDP Certificate
– Pingfed Certificate
Copy SAML Proxy ACS URL, IdP URL and the Certificate values from Netskope settings to configure ServiceNow Identity Provider / Pingfed SP connection settings as mentioned in the SeviceNow configuration section in this topic.
Enable Emergency Bypass mode for the SSO account.
Enable
Multiple SAML entity ID support
feature for SAML Reverse Proxy by using the following API.
curl -X POST http://dpmgmtsvc:80/saml/config/template/<tenant_id> -H 'content-type:application/json' -d '{"multiEntityId":{<app_id_1>: ["https://saml-<tenant_name>/<org_hash>/<acs_id_1>", "https://saml-<tenant_name>/<org_hash>/<acs_id_2>"]]}}'
Example
: curl -X POST http://dpmgmtsvc:80/saml/config/template/1042 -H 'content-type:application/json' -d '{"multiEntityId": "2115": ["https://saml-example.test.local/7Vw4TjT9VWcwvgJM6Q6j/31", "https://saml-example.test.local/7Vw4TjT9VWcwvgJM6Q6j/33"]}}'
Acs_id for ServiceNow app is 2115.
Pingfed IdP Configuration
Login to Pingfed IdP with admin credentials
Click on SP Connections. Create a new SP connection with SAML 2.0 protocol as shown in the below screenshot.
Export Pingfed SP connection Metadata.
ServiceNow Configuration
Create a dev ServiceNow tenant from the following the URL https://developer.servicenow.com
One of the pre-requisite requirements is to install some plugins into ServiceNow.
Setup a new Identity Provider by navigating to Multi-Provider SSO > Identity Providers.
Click
New
, select SAML and import your Pingfed metadata using the XML option.
Configure the below settings with the mentioned values.
Identity Provider URL
= Netskope SAML proxy Multi entity URL.
Identity Provider’s AuthnRequest
= Netskope SAML Proxy IdP URL.
Audience URI
=  Netskope SAML proxy Multi entity URL.
Uncheck
Auto Provisioning User
and
Update User Record Upon Each Login
from the User Provisioning tab.
In the
Advanced
tab, configure the following:
Protocol Binding for the IDP’s AuthnRequest = urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST
Protocol Binding for the IDP’s SingleLogoutRequest = urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST
Protocol Binding for the IDP’s SingleLogoutRequest = urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST
AuthnContextClassRef Method = urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified
Import Netskope SAML certificate under
X509 Certificate
section.
Save the configuration.
Enable SP initiated SAML for a specific user or all users in the organization.
Go to
Multi-Provider SSO
>
Identity Providers
.
Right-click an identity provider record and select
Copy sys_id
.
Save the sys_id value. You’ll need to use this value for the SP-initiated flow.
If want to enable SP-Initiated SAML on a user by user basis instead of for all users within a given company, do the following:
Go to the
Users
page from the
Filter navigator
at the top left of the page.
Select any given user to go to the user details page – the specific user you choose doesn’t matter.
From the menu icon, select
Configure
, then
Form Design
.
From the
Fields
sidebar on the left, select and drag the SSO Source field to the
User [sys_user]
table in the middle of the page as the last attribute in the list.
Click
Save
.
To enable SP-Initiated SAML for a specific user, go back to the
Users
page from the Filter Navigator.
Select your specific user to navigate to the user details page.
In the
SSO Source
field, type
sso:
and then paste the
sys_id
from the Identity Provider you created with the Multi-Provider SSO plugin. Choose
Update
to finish.
If you want to enable SP-Initiated SAML for all users within a given company instead of on a user-by-user basis, do the following:
Go to the
My Company
page from the
Filter Navigator
at the top left of the page.
From the menu icon, select
Configure
, then
Form Design
for the Company.
From the
Fields
sidebar on the left, select and drag the
SSO Source
field to the
Company [core_company]
table in the middle of the page as the last attribute in the list.
Click
Save
.
To apply SP-Initiated SAML to all users in a specific company, go back to the
My Company
page from the F
ilter Navigator
.
In the SSO Source field, type sso:. Paste the
sys_id
from the Identity Provider you created with the Multi-Provider SSO plugin. Choose
Update
to finish.
Reference: https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-ServiceNow.html#:~:text=To%20enable%20SP%2DInitiated%20SAML%20for%20a%20specific%20user%2C%20go,the%20Multi%2DProvider%20SSO%20plugin
Test the connection. Once the connection is successful, activate it.
Disable Emergency Bypass mode for the SSO account from the Netskope WebUI.
ServiceNow Troubleshooting
If the Identity provider connection could not be activated:
Create a new System Property (navigator search for sys_properties.list) named:
glide.authenticate.multisso.test.connection.mandatory
with Type true|false and Value of False.
Re-test your IDP connection
Click “Activate” and “Update and Exit”
If we need to check logs, location of logs on ServiceNow instance.
In this Topic
Reverse Proxy for ServiceNow with Pingfed IdP

---
## SAML Settings for Authentication
**URL:** https://docs.netskope.com/en/saml-settings-for-authentication/
**Last Modified:** 2026-05-14T21:49:24+00:00
**Scraped:** 2026-08-03T10:06:08.957275+00:00

SAML Settings for Authentication
The SAML Forward Proxy must be configured with the Assertion Consumer Service (ACS) URL, IdP URL, and IdP Certificate by following this procedure.
Before Configuring SAML Settings for Authentication
Things to know before you proceed with configuring SAML settings for authentication.
As of R121, IdPs can be partially configured and updated in order to grab the ACS URL and Metadata to be placed into the IdP more easily.
Creating IdPs through REST API calls is a controlled-GA feature. To enable this, please contact Netskope Support or your account executive.
Instructions in this section is applicable only for non admin users. For instructions to configure SSO for admin users, see Single Sign On for Administrators section.
Get Netskope SAML Settings
Log in to the Netskope WebUI
Go to
Settings
>
Security Cloud Platform
and click
SAML
under Forward Proxy.
When configuring a Netskope app in the IdP, use the metadata and certificate from
Settings
>
Administration
>
SSO
page in Netskope WebUI.
If the IdP account is already created, then in that IdP Account click
Netskope Settings
and copy the following:
For more information in creating an IdP account in Netskope, see the
Adding a New Forward Proxy IdP Service
section.
SAML Entity ID
SAML Proxy ACS URL
:
Download CERTIFICATE
Adding a New Forward Proxy IdP Service
To add a new IdP as an authentication service, do the following:
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
.
Click the
NEW ACCOUNT
button. In the
New Account
pop-up window, enter the following:
Name
: Provide a name to identify the IdP service.
Access Method
: Select the access method that will use this IdP service.
All
– To use the IdP service for all access methods.
IPSec
– Select this option to use the IdP service for IPsec access methods. For granular control, you can enable the IdP service for all tunnels or specific tunnels. To enable this IdP for a specific tunnel, select a Specific tunnel from the list and then select the tunnel from the IPSec Tunnel list.
If you have not configured an IPSec tunnel yet, click the gear icon to access the IPSec tunnel creation interface.
GRE
– To use the IdP service for GRE access methods. For granular control, you can enable the IdP service for all tunnels or specific tunnels. To enable this IdP for a specific tunnel, select Specific tunnel and then select the tunnel from the GRE Tunnel list.
Client Enrollment
– To use the IdP service for client enrollment workflow.
Cloud Explicit Proxy
– To use the IdP service when the access method is via Netskope Proxy.
IdP Configuration
– In the Setup tab, enter the following details to configure the IdP service.
IDP SSO URL
: This is the URL used to redirect the user to the IdP site for authentication. Contact your third-party Identity Provider and add the unique IdP login URL in this field.
IDP Entity ID
: An entity ID is a globally unique name for a SAML entity, either an Identity Provider (IdP) or a Service Provider (SP).
IDP Certificate
: Upload the certificate of the third-party IdP in this field. This is required by Netskope to validate the signature of the SAML assertion.
SAML Binding Method
: Select between HTTP Post and HTTP Redirect as a method of communication method between IdP and tenant.
Alternate User Id Field
: Netskope looks at the NameID field in the SAML assertion to get the user identity. If you would like to use another field for user identification, type the name of the SAML attribute in this field. Select the Status toggle to enable or disable the IdP service.
Click
SAVE
.
Options
tab. These are optional settings. In this tab, you can specify granular controls to an IdP service so that the IdP is used only when very specific criteria (like network location and authentication domain ) are matched.
Adding a New Forward Proxy IdP Service with the REST API
GET, POST (Create), PATCH (Update), and DELETE are supported for creating SAML IdP accounts.
For specifics, please see
Rest API v2
and your tenant’s Swagger API documentation located at https://<your_tenant>.netskope.com/apidocs/?include_beta_routes=0
Forward Proxy Global Settings
Administrators can use this page to configure user authentication settings. You can enable cookie surrogate, modify the authentication refresh interval, and modify the user authentication domain refresh interval. In addition, you can bypass specific domains and web categories for which authentication is not required.
Using IP Surrogate
IP surrogate is enabled by default for SAML forward proxy authentication. The Netskope service maps users to private IP addresses for user-based or group-based policy evaluations. User to private IP address mapping expires based on the configured authentication refresh interval setting.
Using Cookie Surrogate
A cookie surrogate is useful in cases where users are behind a NAT device and the Netskope Security Cloud Platform sees the same IP for all the users that are behind NAT. When this feature is enabled, the cookie surrogate resolves this by using a cookie to fetch user identity. For this purpose, enter the private IP address of the NAT.
To use a cookie surrogate, go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
and click
Settings
. In the
Settings
pop-up enable the
Enable Cookie Surrogate
toggle, and then enter the source IP address (like 1.1.1.1) or subnet (like 1.1.1.0/24) for the cookie surrogate in the Source IP Addresses text field and click the
+
button.
Cookie Surrogate for Desktop Applications
Native apps on a desktop that do not honor cookie redirects, or background traffic from a browser such as
.js
and
.css
that do forward cookies or support redirects, may not have user identity available. When user identity is unavailable:
Policies that are user specific for access to specific apps, instances, or SSL decryption, etc., will not be enforced.
Events (Application/Page) will not show user information, but will show the IP address of the user.
With cookie surrogate, IdP authentication will happen for each browser instance because it is cookie dependent.
Device information is not supported with cookie surrogate.
Remediate actions include bypassing authentication for problematic domains.
Limitations with the IPSec/GRE Cookie Surrogate
Depending on the website’s structure and its Cross-Origin Resource Sharing (CORS) policy, there may be scenarios where the nspatoken cookie is either omitted or cannot be transmitted as part of the request. During user authentication, Netskope establishes the user’s identity by setting and receiving the nspatoken cookie between the Netskope service and the user’s browser. If the nspatoken is absent in the browser’s subsequent requests, Netskope will block the connection as it relies on the token to validate the user session and authorize communication.
Refresh Interval Settings
In the
Settings
pop-up, in the
Authentication
tab, you can configure the Authentication Refresh Interval and User Authentication Domain Refresh Interval.
Authentication Refresh Interval
This option applies to both IP surrogate and the cookie surrogate token. To refresh the authentication token after a specified length of time, enter the days and hours for the Authentication Refresh Interval. The default value is 7 days, the minimum is 1 hour, and the maximum is 180 days.
For IPSec, GRE, or EPoT deployments, you can run the following POST request from the end device to force expiration of a specific user-to-IP mapping for IP surrogate behind the tunnel:
curl -X POST -H "X-NS-REMOVE-AUTH-ENTRY: 1" -H "Content-Type: application/json" -d "{"comment": "<enter your comment>"}" https://nsauth-<enter your tenant>.goskope.com/
When IP surrogate is removed for the inline user, an audit event is generated. This activity is listed as “Removed Auth Entry” followed by your comment in the curl command. Go to
Settings
>
Administration
>
Audit Logs
to view audit events.
User Authentication Domain Refresh Interval
If you set up the user authentication domain for IdP selection, you can control how frequently users are prompted to enter their email. Enter the days and hours for the User Authentication Domain Refresh Interval. This feature is optional; the default is 7 days, the minimum is 1 hour, and the maximum is 180 days.
Bypass Settings
You can specify domains, web categories, and network IP addresses for which user authentication is not required. To specify authentication bypass settings, go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
and click
Settings
. In the
Settings
pop-up click the
Bypass
tab.
Domain Bypass
Click to add comma-separated URLs to bypass. When finished, click
Save
.
Adding your IdP domains here are recommended.
Web Category Bypass
Click to add add comma-separated URLs to bypass. When finished, click
Save
.
Source IP Address Bypass
Click to edit and search for source networks. For each of the networks found, you can choose to bypass based on User IPs or Egress IPs (just one, not both). Enter the IP address, IP address range, or CIDR netmask in the text field. Click the
icon to add multiple network locations. After adding the network locations, click
Save
.
In this Topic
SAML Settings for Authentication

---
## SAML Authentication with OKTA
**URL:** https://docs.netskope.com/en/saml-authentication-with-okta/
**Last Modified:** 2025-08-31T01:56:04+00:00
**Scraped:** 2026-08-03T10:06:10.148876+00:00

SAML Authentication with OKTA
The following section illustrates the steps to set up SAML authentication via OKTA. Ensure that you have completed the provisioning steps as described
here
.
In the newly created Netskope User Enrollment App (Netskope SAML Auth), go to the
Sign On
tab and click
Edit
.
Under the SAML 2.0 section, click to expand
More Details
to view and copy the following. They will be required when creating a new account in SAML Forward Proxy in your Netskope tenant:
In the SAML Settings of the IDP, ensure that you set
Assertion Signature
field to
Signed
.
Sign on URL
Issuer URL
Download the Signing Certificate
The next set of steps will generate the necessary Netskope SSO URLs and certificate to configure the OKTA Sign on settings.
Generating Netskope SSO URLs and Certificate
In the Netskope tenant WebUI, go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
, and click
New Account
. Update the following details from Okta into the New Account pop-up window:
Provide a Name
Select the Appropriate Access Methods this Account will apply to.
Copy the
Sign-on URL
from Okta to
IDP SSO URL
Copy the
Issuer URL
from Okta to
IDP ENTITY ID
Upload
Signing certificate
from Okta to
IDP Certificate
Leave SAML Binding Method as the default, “
HTTP Post Binding
”.
Click
Save
.
Next to the newly created SAML Forward Proxy account, select Netskope Settings and copy the SAML Entity ID, SAML Proxy ACS URL.
Update Netskope User Enrollment App in OKTA
In the OKTA admin UI, go to the newly created Netskope User Enrollment App.
Go to the Sign On tab and click
Edit
.
In the Advanced Sign-on Settings section, update the following copied from the newly created Netskope SAML account.
Copy the
SAML Proxy ACS URL
from Netskope to SAML ACS URL
Copy the
SAML Entity ID
from Netskope to SAML Entity ID
Application UserName Format
: Select either the Okta Username or Email, as long as the value sent matches the primary email address of the user.
Click
Save
.
Enable New Account in Netskope Admin WebUI
In the Netskope admin WebUI, enable the New Account status.
Go to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
, and open the new SAML account.
Change the status to
Enabled
and click
SAVE
.
In this Topic
SAML Authentication with OKTA

---
## SAML Authentication with Entra ID
**URL:** https://docs.netskope.com/en/saml-authentication-with-entra-id/
**Last Modified:** 2026-07-14T06:32:07+00:00
**Scraped:** 2026-08-03T10:06:11.339861+00:00

SAML Authentication with Entra ID
Netskope utilizes the System for Cross-domain Identity Management (SCIM) standard to automate user lifecycle management and synchronize identity data from Microsoft Entra ID to the Netskope Security Cloud Platform. This integration supports the automated creation, update, and deactivation of user accounts and group memberships, ensuring identity consistency across your security infrastructure.
Before initiating the SAML handshake, ensure your Netskope tenant is configured to allow traffic from Microsoft Entra ID and that you have generated a secure access token for service-level communication.
Prerequisites to Provisioning with Entra ID
Before beginning the configuration, ensure you have the following:
Administrative Access
: Global Administrator permissions in the Microsoft Entra admin center.
Network Requirements
: If using an IP Allowlist, add the Microsoft Entra ID source IP addresses to your Netskope Custom IP list (
Settings
>
Administration
>
IP Allowlist
)
Authentication Token
: An RBAC v3 token generated via a Service Account in your Netskope tenant webUI to ensure persistent integration .
See this
help topic
for instructions to create a token.
If you want to use Group assignments, then you need at least a Microsoft P2 license or above. This may not apply in the future if Microsoft updates its software licensing models.
Recommended Order of Operations
SAML configuration between Netskope and Microsoft Entra ID can begin from either platform. However, starting the configuration in Microsoft Entra ID introduces a circular dependency: the Basic SAML Configuration in Microsoft Entra ID requires the Identifier (Entity ID) and Reply URL (ACS URL) before the setup can proceed, but Netskope generates these values only after the corresponding IdP configuration has been created.
The following workflow uses temporary placeholder values to resolve this dependency, allowing administrators to complete the configuration in Microsoft Entra ID first and update it with the correct values once they become available.
Enter Temporary Values in Microsoft Entra ID
. In the Basic SAML Configuration of the Netskope enterprise application in Microsoft Entra ID, enter temporary placeholder values for the
Identifier
(
Entity ID
) and
Reply URL
(
Assertion Consumer Service URL
) fields — for example,
https://placeholder
. Click
Save
to proceed with the remaining configuration.
Complete the Configuration in Microsoft Entra ID
. Configure the Attributes & Claims as described later in this article, download the SAML Signing Certificate (Base64), and copy the Login URL and Microsoft Entra Identifier values from the SAML configuration page.
Create the SAML Account in Netskope
. In the Netskope Admin Console, navigate to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
and click
New Account
. Enter the
Login URL
as the
IDP SSO URL
, the Microsoft Entra Identifier as the IDP Entity ID, and upload the certificate. Save the configuration.
Retrieve the Actual Values from Netskope
. After saving, click Netskope Settings (or the settings icon) next to the newly created SAML account to view the actual
SAML Entity ID
and
SAML Proxy ACS URL
.
Update Microsoft Entra ID with the Correct Values
. Return to the Basic SAML Configuration in Microsoft Entra ID and replace the placeholder values with the actual
SAML Entity ID
(Identifier field) and
SAML Proxy ACS URL
(Reply URL field). Save the changes.
Creating the Netskope SAML App
This section provides steps to locate and deploy the official Netskope User Authentication application from the Microsoft Entra App Gallery to serve as the gateway for single sign-on (SSO)
Log in to the Microsoft Entra admin center https://entra.microsoft.com
Go to
Applications
>
Enterprise Applications
and click
New Application
.
Enter Netskope in the search bar. Select
Netskope User Authentication
. Enter a name, for example, Netskope Authentication (for example). Click
Create
.
The chosen application name (for example:
Netskope Authentication
) is what will appear in the My Apps portal.
After the app is created, you will be redirected to the app’s overview page. Select
Single sign-on
>
SAML
.
Click
Edit
to enter the Basic SAML Configuration parameters.
Basic SAML Configuration
This section provide the steps to establish the technical connection between the two platforms by exchanging the unique Entity IDs and Assertion Consumer Service (ACS) URLs found in your Netskope tenant.
Click
Edit
to enter the Basic SAML Configuration parameters.
Enter
Netskope Entity ID
and
Netskope ACS URL
copied from the Netskope UI in the required fields, and then click
Save
.
IDP Field
Netskope Field
Identifier (Entity ID)
SAML Entity ID
Reply URL
SAML ACS URL
To get the
Netskope Entity ID
and
Netskope ACS URL
, login to your Netskope tenant and do the following:
Go to
Settings
>
SAML
(under Forward Proxy). Click
New Account
. In step 1 of the
New Account
pop-up, enter an
Account Name
and select
SAML
.Click
Save and Continue
.
In step 2 of the
New Account
pop-up,
Netskope Settings
tab will display the
SAML Entity ID
and
SAML ACS URL
, along with
SAML Certificate
and
Netskope Metadata
for download.
If your Netskope ACS URL contains a placeholder, you can find your specific
Organization ID
in the Netskope UI under
Settings > Security Cloud Platform > MDM Distribution
(
under Netskope Client
). Find your Organization key here.
You will be prompted to test SSO. Select
No, I’ll test later
.
User Attributes and Claims
This section provides steps to configure the specific identity data—such as email addresses—that Entra ID must pass to Netskope within the SAML assertion to uniquely identify and authenticate users.
Netskope requires the Name ID to be formatted as an email address.
Ensure the Source attribute is set correctly to
user.mail
to prevent authentication failures
Go to and edit the
Attributes & Claims
section.
Delete all the default Additional claims. You only need the Required Claim
Select the value to edit the Unique User Identifier (Name ID) field.
Set the
Source attribute
as user.mail and click
Save
.
user.mail is set as the claim value for Name ID. Click on the x to close this section.
Finalizing Integration & User Assignment
The section provides the steps to complete the integration by downloading the Entra ID security certificate and assigning specific users or groups who are authorized to access the Netskope platform via SSO.
After downloading the Certificate (Base64) and copying the Login URL, you
must
return to the Netskope tenant and upload these values into the
IDP Settings
tab of your SAML account configuration
Download the certificate in Certificate (Base64) format, and copy the Login URL and Azure AD Identifier values. These need to be entered into the Netskope Forward Proxy – SAML settings page later on.
Next, assign users who will log in using the Entra ID SAML Auth. Go to
Users and Groups
> Add
user/group
.
Select Users and groups. Select the users, and then click
Select
.
Click
Assign
to complete this procedure. This step enables the SSO app for the selected identites,.
Troubleshooting Tips
Entity ID / ACS URL not visible in Netskope:
Ensure you have clicked
New IDP Instance
or
Add New
. The values appear on the configuration form under
Service Provider Details
or
SP Metadata
once the form is open.
Multiple IdP instances:
Each new IDP instance generates its own unique Entity ID and ACS URL values. Ensure you are copying from the correct instance.
Metadata upload fails:
Ensure the XML file downloaded from Entra ID is unmodified and contains a valid signing certificate.
In this Topic
SAML Authentication with Entra ID

---
## Configure Browser-based Access with Multiple IdPs
**URL:** https://docs.netskope.com/en/browser-access-with-multiple-idps/
**Last Modified:** 2026-02-27T22:15:38+00:00
**Scraped:** 2026-08-03T10:06:59.206842+00:00

Configure Browser-based Access with Multiple IdPs - Netskope Knowledge Portal
Configure Browser-based Access with Multiple IdPs
This document explains how to configure and test a use case for the NPA Browser-based Access Multiple IdPs feature.
Enabling this feature allows you to configure multiple reverse proxy SAML accounts of type Private Apps. You can configure multiple reverse proxy SAML accounts (IdPs), and configure multiple email domains per SAML account configuration for criteria matching per IdP.
Use Case
: ACME Corp has an existing enterprise
IdP1
. ACME Corp also has external users from Vendor A (using
IdP a
) and Vendor B (using
IdP b
) who require access to their applications. In such a scenario, you can enable the Browser-based Access Multiple IdP Support feature.
Prerequisites
Enable the feature flag for NPA Browser-based Access Multiple IdP (contact Support or your sales rep).
Your NPA Browser-based Access Application(s), respective policies, and SAML Reverse Proxy Account of type Private Apps are already configured.
Go
here
for configuration details.
External users (users from additional IdPs) are imported via SCIM or Directory Importer to the Netskope tenant.
Review these articles for additional details.
Netskope SCIM Settings
Configure Directory Importer
UI Changes
SAML Account Page
When the
Browser-based Access
Multiple IdP
feature flag is enabled for a tenant, an additional setting labeled
User Authentication Domain
will appear in the UI.
Note
Netskope supports up to 10 SAML accounts for Private Applications.
Landing Page
When multiple SAML accounts for Private Apps are configured, a new landing page (shown below) is presented to the end-user when they access a browser-based application for the first time. On this page, the user enters their email address and clicks
Continue
. Based on the configured domain match criteria, the relevant IdP is then presented to the user.
Notes
When the feature for multiple IdP is enabled and multiple IdPs are configured in the tenant, the landing page is presented for all configured Browser-based Access apps and for all the users accessing those apps.
It appears when accessing an application for the first time, and for all users requiring access to these applications.
The user will be required to re-enter their email on the landing page only after the Browser-based Access cookie expires (default is 24 hours), or if the browser cache is cleared.
In the screenshot above,
ACME Corporation
represents the account name.
Configuration
Example Configuration
In this example, ACME Corp and its associated vendors use different IdPs for user authentication.
ACME Corp
:
Uses
IdP 1
with email domains
@acme.com
and
@eu.acme.com
.
Vendor A
:
Uses
IdP a
with email domains
@vendora.com
and
@vendora2.com
.
Vendor B:
Uses
IdP b
with the email domain
@vendorb.com
.
Vendors A and B, who use
IdP a
and
IdP b
respectively, are external users requiring access to ACME Corp’s Browser-based Access applications.
It is assumed that
IdP 1
is already configured. After the Browser Access Multiple IdP feature flag is enabled,
IdP 1
is designated as the default IdP for Private Apps.
The default IdP will authenticate all users, except for those with email domains explicitly defined under other SAML accounts for Private Apps. Note that no explicit email domains need to be configured for the default IdP.
Notes
Default IdP (
IdP 1
) can also be modified to include “Specific Domains” if needed.
It is
not
mandatory to have a default account.
Configure
IdP a
If you do not already have a SAML account to use, create a new SAML account.
Go to
Settings > Security Cloud Platform
and click
SAML
(under Reverse Proxy).
Click
Add Account
.
In the New Account window, enter a name for the account.
Select
Private Apps
from the Application dropdown list.
Enter these parameters:
IdP SSO URL: Enter your IdP SSO URL.
IdP Certificate: Enter your IdP certificate.
Select
Specific Domains
for
User Authentication Domain
and enter the domain(s). For multiple domains, add each on a separate line.
Click
Save and View Netskope Settings
to see the URLs for this account. Copy the Browser-based Access ACS URL and Audience URL to use in your IdP account. Update your IdP account with these URLs before proceeding.
Configure
IdP b
Similar to
IdP a
, create a new SAML account by repeating the steps above. Additionally, define the
User Authentication Domain
as seen in the screenshot below.
Landing Page Scenarios
These scenarios determine whether a landing page is presented for all configured Browser-based Access apps and the users accessing those apps.
Browser Access Multiple IdP Feature Flag
Default SAML Account
Specific Domain SAML Account
Landing Page
Disabled
Not applicable
Not applicable
No
Enabled
Yes
None
No
Enabled
Yes
No domain specified
No
Enabled
None
One account
Yes
Enabled
None
Many accounts
Yes
Enabled
Yes
One account
Yes
Enabled
Yes
Many accounts
Yes
Validation
Access a NPA Browser-based Access App and the end-user should be presented with a landing page.
Based on the configuration example above:
Email entered within the landing page
Expected IdP
testa@vendora.com
IdP a
testb@vendorb.com
IdP b
testc@acme.com
IdP 1
testd@blah.com
IdP 1
Troubleshooting
If any issues are found, please collect a screen recording and a HAR capture of the traffic flows, and share them with the Netskope support team for further troubleshooting.
In this Topic
Configure Browser-based Access with Multiple IdPs

---
## CrowdStrike Falcon Identity Protection Plugin for Risk Exchange
**URL:** https://docs.netskope.com/en/crowdstrike-falcon-identity-protection-v1-0-0-plugin-for-risk-exchange/
**Last Modified:** 2026-05-28T23:08:52+00:00
**Scraped:** 2026-08-03T10:07:18.047474+00:00

CrowdStrike Falcon Identity Protection Plugin for Risk Exchange - Netskope Knowledge Portal
CrowdStrike Falcon Identity Protection Plugin for Risk Exchange
This document explains how to configure the CrowdStrike Falcon Identity Protection v1.0.0 plugin with the Risk Exchange module of the Netskope Cloud Exchange platform. This plugin fetches users and their respective scores from Identity Protection > Users page of CrowdStrike Falcon Identity Protection. This plugin does not support any actions to be performed on users.
Netskope normalization score calculation = | (1 – (CrowdStrike Falcon Identity Protection Risk Score))|*1000
Prerequisites
To complete this integration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Risk Exchange
plugin already configured.
Connectivity to the CrowdStrike platform.
Connectivity to one of the following hosts:
https://api.crowdstrike.com (Commercial cloud (api.crowdstrike.com))
https://api.us-2.crowdstrike.com (US 2 (api.us-2.crowdstrike.com))
https://api.laggar.gcw.crowdstrike.com (Falcon on GovCloud (api.laggar.gcw.crowdstrike.com))
https://api.eu-1.crowdstrike.com (EU cloud (api.eu-1.crowdstrike.com))
Note that you just need any one of the URLs above for the plugin.
CrowdStrike Falcon Identity Protection Plugin Support
This plugin fetches users and their respective scores from Identity Protection > Users page of CrowdStrike Falcon Identity Protection. This plugin does not support any actions to be performed on users.
Type of data pulled
Users
Actions Supported
Not Supported
Mappings
Plugin Field
Expected Datatype
Suggested Field Name
Suggested Field Action
emailAddress
String
Email
Unique
riskScore
Number
riskScore
Overwrite
Note that the user score you’ll see will be different from what you see in the CrowdStrike Identity Protection Platform.
The platform displays CrowdStrike’s Identity Protection Risk Score in the scale of 1 – 10 (1 > minimum risk, 10 > maximum risk) but the fetch records API returns
Netskope normalization score calculation > | (1 – (CrowdStrike Falcon Identity Protection Risk Score))|*1000
Permissions
Below are the permissions needed for the URE CrowdStrike Falcon Identity Protection plugin.
Scope
Read
Write
Identity Protection GraphQL
–
Yes
Identity Protection Timeline
Yes
–
Identity Protection Entities
Yes
No
API Details
List of APIs Used
API Endpoint
Method
API Client Scope
Use Case
identity-protection/combined/graphql/v1
POST
Identity Protection GraphQL
Identity Protection Timeline
Pull Users and Scores
Fetch Records
API Endpoint:
identity-protection/combined/graphql/v1
Method:
POST
Parameters:
Key
Value
Description
creationTime
2022-12-26T17:05:20Z
Timestamp in “%Y-%m-%dT%H:%M:%SZ” format.
after
null
null for first API call and endCursor (eyJjcmVhdGlvblRpbWUiOnsiJGRhdGUiOiIyMDIyLTA5LTE3
VDA4OjI2OjM0LjAwMFoifSwiX2lkIjoiYjM2NTNmNTMtYjNjOS0zYTY5LWFlZDQtYzJjNDhiYzliYjNkIn0=)
Data:
query ($after: Cursor, $creationTime: DateTimeInput) {
                    entities(types: [USER], sortKey: CREATION_TIME, sortOrder: DESCENDING, first: 1000, accountCreationStartTime: $creationTime, after: $after,archived: false) {
                        nodes {
                        primaryDisplayName
                        secondaryDisplayName
                        ... on UserEntity {
                            emailAddresses
                        }
                        riskScore
                        }
                        pageInfo {
                        hasNextPage
                        endCursor
                        }
                    }
                    }
Sample API Response:
{
    "data": {
        "entities": {
            "nodes": [
                {
                    "primaryDisplayName": "Customer 2 Admin",
                    "secondaryDisplayName": "customer2@demo.netskope.pro",
                    "emailAddresses": [
                        "customer2@demo.netskope.pro"
                    ],
                    "riskScore": 0.15
                }
            ],
            "pageInfo": {
                "hasNextPage": true,
                "endCursor": "eyJjcmVhdGlvblRpbWUiOnsiJGRhdGUiOiIyMDIzLTExLTI3VDA5OjMzOjM2LjAwMFoifSwiX2lkIjoiZjY0YzNhYTctZmMwMi0zMDNlLWFiNTItNGU5MmViYzgxNTdjIn0="
            }
        }
    },
    "extensions": {
        "runTime": 569,
        "remainingPoints": 499999,
        "reset": 9969,
        "consumedPoints": 1
    }
}
Fetch Scores
API Endpoint:
identity-protection/combined/graphql/v1
Method:
POST
Variables:
Key
Value
Description
email
[“Dev7979user7979@bddev.com”]
List of email addresses.
Data:
query ($email: [String!]) {
                    entities(types: [USER], first: 1, emailAddresses: $email, archived: false) {
                        nodes {
                        ... on UserEntity {
                            emailAddresses
                        }
                        riskScore
                        }
                    }
                    }
Sample API Response:
{
    "data": {
        "entities": {
            "nodes": [
                {
                    "emailAddresses": [
                        "Dev7979user7979@bddev.com"
                    ],
                    "riskScore": 0.67
                }
            ]
        }
    },
    "extensions": {
        "runTime": 26,
        "remainingPoints": 499999,
        "reset": 6445,
        "consumedPoints": 1
    }
}
Performance Matrix
Below is the performance reading conducted on a Large CE Stack by pulling 500K User scores from CrowdStrike to Netskope CE.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Time taken to store the pulled and updated user records
~ 25 mins
User Agent
netskope-ce-5.1.0-cre-crowdstrike-falcon-identity-protection/1.0.0
Workflow
Get your Client ID and Client Secret.
Configure the CrowdStrike Falcon Identity Protection plugin.
Configure a business rule.
Configure an action.
Validate the plugin.
Click play to watch a video.
Get your Client ID and Client Secret
Log in to your CrowdStrike platform, go to the menu Icon, and select
Support and resources > API clients and Keys
.
Click
Add new API Client
.
Add the following scopes while adding the API Client:
Scope
Read
Write
Identity Protection GraphQL
–
Yes
Identity Protection Timeline
Yes
–
Identity Protection Entities
Yes
No
Make a note of the Base URL, Client ID, and Secret. You need these to configure the plugin.
Configure the CrowdStrike Falcon Identity Protection Plugin
Log in to Cloud Exchange and go to
Settings > Plugins
. Search for and select the
CrowdStrike Falcon Identity Protection (CRE)
plugin box.
Enter a Configuration Name and a Sync Interval.
Click
Next
, and then enter the Configuration Parameters:
Base URL: Enter the Base URL from the CrowdStrike Platform.
Client ID: Enter the Client ID generated from the CrowdStrike Platform.
Client Secret: Enter the Client Secret generated from the CrowdStrike Platform.
Initial Range (in days): Enter the number of days to fetch the data for the initial run.
Click
Next
, and provide the mappings according to your needs.
Click
Save
. The Plugin configuration will be available on the Plugins page.
Add a Risk Exchange Business Rule for CrowdStrike Falcon Identity Protection
In Risk Exchange, go to
Business Rules
.
Click
Create New Rule
.
Enter the Rule Name, select the Entity and fields that were mapped while configuring the plugin, and add filters per your needs.
Click
Save
.
Add Risk Exchange Actions for CrowdStrike Falcon Identity Protection
The CrowdStrike Falcon Identity Protection plugin supports the following action types:
No Action
This action does not perform any action on the users, but can generate alerts in CTO if the Generate Alerts toggle button is enabled.
Note that you can perform the actions on the users pulled from CrowdStrike Falcon Identity Protection on the Netskope tenant.
To configure this action:
Go to
Risk Exchange > Actions
and click
Add Action Configuration
.
Select the Business rule, the plugin configuration, and No action in Actions dropdown. Enable the toggle button for
Require Approval
if approval is required before performing the Generate Alert action.
And similarly enable
Perform action during the maintenance Window
if you wish to perform an action during the Maintenance Window. Click
Save
.
Manual Sync the action if users are already present in Records. To Validate the generated alerts, go to
Ticket Orchestrator > Alerts
.
Validate the CrowdStrike Falcon Identity Protection Plugin
Validate on CE
To validate the pulling and storing of users from the CrowdStrike into Cloud Exchange:
Go to the
Logging
and search for the plugin logs.
Go to the
Records
, and select the Entity that was selected while configuring the CrowdStrike IP plugin to view the pulled users.
Validate on CrowdStrike
To verify if the User scores are available on the platform to pull, follow the below steps:
Log in to CrowdStrike Falcon Platform.
Go to
Identity protection > Users
.
Here you’ll see the users.
Troubleshooting the CrowdStrike Falcon Identity Protection Plugin
Unable to configure the CrowdStrike Identity Protection plugin
If you are unable to configure the CrowdStrike Identity Protection plugin, then it could be due to one of these reasons:
Client Secret has been Reset for the particular Client ID.
Required Permissions are not given to the API Client.
Invalid values provided to the configuration parameters.
What to do:
Make sure that latest Client Secret is used for the API Client
Make sure valid values are provided in the configuration parameters. Go to the Logging page and verify the log message.
Provide the required permissions to the API Client using which configuration parameters are created.
Unable to pull user score from the CrowdStrike platform
If you are unable to pull any user scores, it could be due to one of these reasons:
No Users are available to be pulled.
Insufficient plugin permission was provided to the Client ID and Client Secret.
The API response has no value in the
emailAddresses
field.
The API response has multiple email addresses in the
email-addresses
field.
What to do:
No Users are available to be pulled.
Check the CrowdStrike platform to see if the users are available to be pulled from the steps provided in the CrowdStrike validation.
Note that only Unarchived users are pulled from the CrowdStrike platform.
Insufficient plugin permission was provided to the Client ID and Client Secret.
Verify the permissions required for the plugin.
In this Topic
CrowdStrike Falcon Identity Protection Plugin for Risk Exchange

---
## PingIdentity Set Up for Enterprise Browser
**URL:** https://docs.netskope.com/en/pingidentity-setup-for-enterprise-browser/
**Last Modified:** 2025-08-31T01:45:02+00:00
**Scraped:** 2026-08-03T10:08:29.526337+00:00

PingIdentity Set Up for Enterprise Browser - Netskope Knowledge Portal
PingIdentity Set Up for Enterprise Browser
PingIdentity Set Up for Enterprise Browser (PingOne)
This article outlines the steps and references to set up SAML and SCIM for PingOne to use with Enterprise Browser.
SAML Set Up
Ping supports Netskope out of the box. The integration is described in this article: How to Configure SAML 2.0 for the Netskope Client Enrollment with PingOne. The article expands on the article with more screenshots.
Log in to PingOne account (free trial will work). On the landing page, create an environment if one doesn’t yet exist.
Trial/developer accounts are available for free; sign up for a trial at
https://www.pingidentity.com
.
2. Click
Create a Workforce Solution
when creating an environment.
3. Add some test users from the new environment landing page.
4. The following is an example of a new user, note that username and email doesn’t have to be the same. However, it’s highly recommended to keep them in sync to avoid complications.
5. To make provisioning simpler, create a user group that contains all Enterprise Browser users. Click
Directory
>
Groups
.
6. Add any users that should have access to the Enterprise Browser to this user group.
As you provision additional users, add them to this user group.
7. Add an “Application”. Go to the environment landing page
OR
select
Applications
>
Application Catalog
. Then search for “Netskope” and select “Netskope Client Enrollment”.
8. Add a name and enter placeholder values for “ACS URL” and “Entity ID”. Those values will be copied over from Netskope in later steps in this article.
9. Ensure “SAML_SUBJECT” points to “Email Address”. This is important because Netskope policies (RTP, Browser Protection) are configured based on email addresses. Therefore, SAML needs to send user’s email addresses to Netskope upon authentication.
10. Assign any user groups to this application (for example, user group you added in step 5 above).
11. Once the application is saved, navigate to the
Applications
list:
Download its signing certificate:
Note
Single Signon Service
URL. It will be entered as
IDP SSO URL
in Netskope.
Note
Issuer ID
URL. It will be entered as
IDP ENTITY ID
in Netskope.
12. Configure SAML in Netskope. Log in to your Netskope account. Navigate to
Settings
>
Security Cloud Platform
>
Forward Proxy
>
SAML
. Click
New Account
and fill out the following information:
Select either
All
or
Enterprise Browser
ACCESS METHOD
.
IDP SSO URL
will come from
Single Signon Service
field in PingIdentity.
IDP ENTITY ID
will come from
Issuer ID
field in PingIdentity.
IDP CERTIFICATE
will be the signing certificate downloaded in the previous step from PingIdentity.
SAML BINDING METHOD
is
HTTP Post Binding
.
STATUS
should be
Enabled
.
13. After you save the Netskope configuration, click the gear logo to display the configuration.
14. Note the
SAML Entity ID
and
SAML Proxy ACS URL
.
15. Open PingIdentity > click
Applications
. Next to the Application created in Step 7 (“Netskope Client Enrollment – Reuse for EB”) click the ellipses and select
Edit Profile
.
16. Enter the values from Step 14 above and save the configuration.
ACS URL
should contain the value from
SAML Proxy ACS URL
field in Netskope.
Entity ID
should contain the value from
SAML Entity ID
field in Netskope.
17. To test the connection, return to Netskope > select
SAML – Forward Proxy
integration. Click
Test
from the integration context menu.
18. Type the Test user login credentials.
19. If the test is successful, the following screen displays.
SCIM Set Up
The SCIM API is used to automatically push users provisioned in PingIdentity to Netskope.
This configuration may be optional if users are provisioned using an alternate method like AD Importer.
Follow instructions to enable SCIM API v2 on Netskope. To learn more:
SCIM Settings for User Provisioning
Open PingIdentity and set up a new Provisioning Integration. Select
Identity Store
.
3. Select the SCIM Outbound tile.
4. Choose a descriptive name for a Netskope connection.
5. On the Authentication page, enter the following information:
For
SCIM BASE URL
enter “https://<tenant-name>.goskope.com/api/v2/scim”. Replace “<tenant-name>” with your actual tenant name.
Set
Authentication Method
to “OAuth 2 Bearer Token”.
Enter
Netskope API v2 token with SCIM permissions
from Step 1 into the
Oauth Access Token
field.
Click
Test Connection
to verify that PingIdentity can connect to Netskope. In case of errors:
Check that Rest v2 API is enabled in Netskope (by default it’s disabled).
Both Groups and Users SCIM endpoints are added to Rest v2 token you have entered.
Make sure that read and write permissions are enabled for both Groups and Users SCIM endpoints.
6. Default values are acceptable on this page. Optionally, you can customize if you’re familiar with the options.
7. Enable the connection after you create it.
8. Before the user sync can start, you will need to configure a rule. Select
Provisioning
from
Integrations
. Then select
New
Rule
from the context menu.
9. Enter a rule name.
10. Click the
Configuration
tab >
+
to add the Netskope SCIM connection to the
Target
part of the rule.
11. If you have configured everything correctly, you should see the following flow chart.
12.
User Filter, Attribute Mapping,
and
Group Provisioning
will need to be configured before you can enable the rule. Click
User Filter
.
For this example, configure a filter to send all Enabled users to Netskope.
13. Review the
Attribute Mapping
configuration. You can leave the default selection unless you’d like to configure a special mapping.
Attribute Mapping applies to the SCIM API only. The SAML/SSO attribute mapping is configured in the SAML Setup section above.
14. Click
Group Provisioning
to add the
Enterprise Browse
group.
15. Now you can Enable the rule. After enabling, you will see the sync status with the number of users and groups copied over to Netskope.
16. Log in to Netskope and confirm the user sync was successful. Navigate to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Users
(the user list available in Netskope Client is also available to Enterprise Browser, as long as the users are in SSO).
In this Topic
PingIdentity Set Up for Enterprise Browser

---
## Reverse Proxy for Workday with Entra ID SSO
**URL:** https://docs.netskope.com/en/reverse-proxy-for-workday-with-entra-id-sso/
**Last Modified:** 2025-08-31T01:55:04+00:00
**Scraped:** 2026-08-03T10:08:59.721270+00:00

Reverse Proxy for Workday with Entra ID SSO
This guide provides step-by-step instructions to configure Workday Single Sign-On (SSO) with Microsoft Entra ID, using Netskope Reverse Proxy for enhanced security and authentication management.
It is recommended to configure Workday with Microsoft EntraID without Netskope SAML Proxy before proceeding for a smoother configuration experience.
The configuration process involves:
Setting up Microsoft Entra ID SSO
– Establishing Microsoft Entra ID as the identity provider (IdP).
Enabling EntraID for Workday
– Enable Microsoft Entra ID for authentication.
Connecting Workday to Netskope Reverse Proxy
– Routing authentication through Netskope Reverse SAML Proxy
Configure Single Sign-On (SSO) in Microsoft Entra ID
Sign in to the Microsoft Entra Admin Center as a Cloud Application Administrator or higher.
Navigate to
Identity
>
Applications
>
Enterprise Applications
and select
Workday
.
Under the Manage section, select
Single sign-on
. On the Select a Single Sign-On method page, choose
SAML
.
In the Set up Single Sign-On with SAML section, click the edit (pencil) icon next to Basic SAML Configuration.
On the Basic SAML Configuration page, enter the values for the following fields:
In the
Sign-on URL
text box, type a URL using the following pattern:
https://impl.workday.com//login-saml2.flex
In the
Reply URL
text box, type a URL using the following pattern:
https://impl.workday.com//login-saml.htmld
In the
Logout URL
text box, type a URL using the following pattern:
https://impl.workday.com//login-saml.htmld
Your Workday application expects the SAML assertions in a specific format, which requires you to add custom attribute mappings to your SAML token attributes configuration. The following screenshot shows the list of default attributes, where
nameidentifier
is mapped with
user.userprincipalname
. Workday application expects
nameidentifier
to be mapped with
user.mail
,
UPN
, and so on. Edit the attribute mapping by clicking on the Edit icon and change the attribute mapping.
On the
Set up Single Sign-On with SAML
page, in the SAML Signing Certificate section, find Federation Metadata XML and select
Download
to download the certificate and save it on your computer.
On the Set up Workday section, copy below URLs. Screenshot showing Copy configuration URLs.
Now navigate to Users and groups. Select
Add user/group
, then select Users and groups in the Add Assignment dialog. Assign the users to the app.
Steps to configure Workday
In a different browser window, sign in to your Workday company site as an administrator.
In the Search box, search with the name Edit Tenant Setup – Security on the top left side of the home page.
In the SAML Setup section, click on Import Identity Provider.
In Import Identity Provider section, perform the below steps:
Enter the
Identity Provider Name
in the textbox.
In
Used for Environments
textbox, select the appropriate environment names from the dropdown.
Click on Select files to upload the downloaded Federation Metadata XML file. Click
OK
.
After clicking OK, a new row will be added in the SAML Identity Providers and then you can add the below steps for the newly created row.
Click on
Enable IDP Initiated
Logout checkbox.
In the
Logout Response URL
textbox, type http://www.workday.com.
Click on
Enable Workday Initiated Logout
checkbox.
In the
Logout Request URL
textbox, paste the Logout URL value.
Click on
SP Initiated
checkbox.
In the
Service Provider ID
textbox, type http://www.workday.com.
Select
Do Not Deflate SP-initiated Authentication Request
. Click
Ok
.
If the task was completed successfully, click
Done
.
Test SSO
Test your Microsoft Entra single sign-on configuration with following options.
Click on Test this application, this will redirect to Workday Sign-on URL where you can initiate the login flow.
Go to Workday Sign-on URL directly and initiate the login flow from there.
You can use Microsoft My Apps. When you click the Workday tile in the My Apps, you should be automatically signed in to the Workday for which you set up the SSO.
Steps to configure with Netskope SAML Proxy
Login to Netskope Tenant webUI. Navigate to
Settings
>
Security Cloud Platform
>
Reverseproxy
>
SAML
.
Add an account by selecting the “Workday” application.
Update the ACS URL (Workday ACS url), IDP SSO URL (EntraID SSO url) and IdP Certificate (EntraID certificate) fields. Save the configuration.
ACS URL
: Workday URL (eg: https://impl.workday.com//login-saml.htmld)
IDP SSO URL
: Azure EntraID login URL (eg: https://login.microsoftonline.com/f9ab0b18-51c1-42a4-8eb9-08f9f6994eea/saml2)
IDP Certificate
: Azure EntraID SAML certificate.
Copy SAML Proxy ACS URL, IdP URL and the Certificate values from Netskope settings to configure Workday / Azure EntraID settings mentioned later in the document.
Enable Emergency Bypass mode for this SSO account.
On the Workday app, in Workday Identity Provider settings, update “Issuer”, “x509 Certificate” and “IdP SSO service URL” fields with the values copied from Netskope SAMLproxy settings.
Issuer: Organization ID (Eg: 7i0O2d7wzsEru0jtkd0)
IdP SSO service URL: SAML Proxy IdP URL: (eg: https://saml-rproxyauto1.stg.boomskope.com/saml2/http-post/sso/7i0O2d7wzsEru0jtkd0/272
x509 Certificate: SAML Certificate
In Microsoft EntraID Workday Enterprise application, in single sign-on method page/basic SAML configuration, replace Reply URL (Assertion Consumer Service URL) value with Netskope SAMLproxy ACS URL (eg: https://saml-rproxyauto1.stg.boomskope.com/saml2/http-post/acs/7i0O2d7wzsEru0jtkd0/272)
Test SSO with Netskope SAMLproxy
Test Netskope SAMLProxy/Microsoft Entra single sign-on configuration with following options.
Go to Workday Sign-on URL directly and initiate the login flow from there.
You can use Microsoft My Apps. When you click the Workday tile in the My Apps, you should be automatically signed in to the Workday for which you set up the SSO.
Once Test SSO is successful, disable the “Emergency Bypass” option in Netskope SAMLproxy settings and check the flow. Flow should be rewritten with proxy.goskope.com URL.
In this Topic
Reverse Proxy for Workday with Entra ID SSO

---
## Multiple IdP Support for Netskope SSO
**URL:** https://docs.netskope.com/en/multiple-idp-support-for-netskope-sso/
**Last Modified:** 2025-08-31T01:38:36+00:00
**Scraped:** 2026-08-03T10:13:46.412333+00:00

Multiple IdP Support for Netskope SSO - Netskope Knowledge Portal
Multiple IdP Support for Netskope SSO
Multiple Identity Provider (IdP) support for Single Sign-On (SSO) is a feature that allows an organization to integrate with and use multiple identity providers for user authentication and authorization.
Netskope integrates with any SAML 2.0 IdP to provide a wide range of solutions. Admins can configure SSO through the Netskope Admin console to connect to these applications for authentication and you can configure multiple IdPs simultaneously.
Using the SSO enabled feature in the Netskope Admin console, you can set up forced authentication when connecting to third-party applications, e.g. Okta.
Navigate to
Settings
>
Administration
>
SSO
If you do not see the new UI page below, this means you must enable this feature in your account. Contact your Netskope account team to enable this feature in your account.
You must define the alternate userID attribute if the SAML assertion response of the NameID field is in a non-email format for this feature to function correctly. Before proceeding, review the
migration workflow topic
.
Use Cases
1.
Enhanced Security:
Using multiple IdPs can add an extra layer of security. For example, an organization can use one IdP for internal users and another for external users, allowing for different authentication and access control policies.
2.
Diverse User Bases:
Organizations often have diverse user bases, including employees, partners, and customers. These users may already have accounts with different identity providers. Multiple IdP support enables these users to use their existing credentials to access the organization’s resources.
3.
Integration Flexibility:
Different services or applications might have their own preferred identity providers. Multiple IdP support allows an organization to integrate with various IdPs seamlessly, making it easier to use a variety of services while maintaining a consistent SSO experience.
4.
Vendor Compatibility:
When an organization uses a mix of cloud-based and on-premises services, those services may have varying support for SSO and different IdPs. Supporting multiple IdPs ensures that users can access all these services through a unified SSO interface.
5.
Compliance:
Some industries and regions have specific compliance requirements related to identity and access management. Multiple IdP support can help organizations meet these requirements by allowing them to use IdPs that conform to the necessary standards.
6.
Mergers and Acquisitions
: onboard the new companies using IdP and grant access to the admins you need with the set of permissions you require.
Setting Up an SSO Account
Prerequisite
You must add your internal domains.
Navigate to
Settings
>
Administration
>
Internal Domains
Click Edit in the Admin Account Domains section.
You must add the domains for which you will create new accounts later through the SSO page.
Optionally, you use the ‘Import from Internal Domains’ to either add to or replace the current list of internal domains.
Optionally, you can enter domains separated on new lines. Wildcard matches are allowed, examples shown below.
2. Add your domains and click
Save
.
Creating a New Account
Navigate to
Settings
>
Administration
>
SSO
Click New Account.
2. In the Account Name field, add a name that you can identify quickly.
3. In the User Authentication Domains section, click in the Domains = field to view the selectable menu. Select the domain(s) for which you’re setting up the integration.
4. Optionally, enter the name of SAML attributes that provide the email format. Netskope looks at the ‘NameID’ field in the SAML assertion to get the user identity.
IMPORTANT
: You must define the alternate userID attribute if the SAML assertion response of the NameID field is in a non-email format. Before proceeding review the
migration workflow topic
.
5. Click
Save and continue
.
6. In the Netskope Settings (wizard step 2) you will see your Netskope service provider information. The ‘Entity ID’ and subsequent URLs will show an ID that is generated only for this integration, generating a unique ID per IdP configuration.
7. Optionally in Netskope Settings, you can define roles for this integration. Best practice for security is to lock down the roles.
8. In the Create Account (wizard step 3) confirm the required fields such as IdP SSO URL, IdP entity ID, and certificate and click Finish. Note, the required fields are available in your IdP UI.
Once your integration is complete, you will see your integration listed in the SSO home page.
If you can exit the configuration before it is completed. You will see the configuration is pending completion in the SSO home page.
Click the ellipses at the end of the list to complete your setup for your integration. This will re-open the wizard window.
You can verify the multiple IdP integration by accessing your account, you will see the following log in page.
Troubleshooting
Navigate to
Settings
>
Administration
>
Audit Log
to view information about your integration.
In this Topic
Multiple IdP Support for Netskope SSO

---
## Associate the Custom AI Provider to the AIG
**URL:** https://docs.netskope.com/en/associate-the-custom-ai-provider-to-the-aig/
**Last Modified:** 2026-05-18T15:00:32+00:00
**Scraped:** 2026-08-03T10:17:04.257258+00:00

Associate the Custom AI Provider to the AIG - Netskope Knowledge Portal
Associate the Custom AI Provider to the AIG
Once you add a custom AI provider, you can associate it to an AI Gateway. To associate it to an AI Gateway, follow the steps below.
Log in to the Netskope tenant UI and go to
Settings > Security Cloud Platform > AI Gateway > Gateway
Setup
.
In the
AI Gateway
page, from the
AI Virtual Machines
list choose an AI Gateway that you want to associate with the custom AI provider.
Click
Link Custom AI Providers
.
In the
Link Ai Providers
page, select a custom AI provider.
Click
Save
.
Saving the settings enables the AI Gateway to manage and secure traffic between the AI Agent and your custom AI provider.
In the
AI Gateway
page, you can also find the HTTPS/HTTP Base URL that your AI agent needs to use to reach an AI provider.
In this Topic
Associate the Custom AI Provider to the AIG

---
## Browser-based Access with Reverse Proxy SAML
**URL:** https://docs.netskope.com/en/browser-based-access-with-reverse-proxy-saml/
**Last Modified:** 2026-02-28T00:38:19+00:00
**Scraped:** 2026-08-03T10:18:27.858541+00:00

Browser-based Access with Reverse Proxy SAML
NPA supports browser access with these providers:
Configure Browser-based Access with Okta
Configure Browser-based Access with Microsoft Entra
Configure Browser-based Access with Google Workspace
In this Topic
Browser-based Access with Reverse Proxy SAML
Browser-based Access with Reverse Proxy SAML - Netskope Knowledge Portal

---
## Zone Selection Based on User Identity
**URL:** https://docs.netskope.com/en/zone-selection-based-on-user-identity/
**Last Modified:** 2026-07-24T17:05:29+00:00
**Scraped:** 2026-08-03T10:20:42.218195+00:00

Zone Selection Based on User Identity - Netskope Knowledge Portal
Zone Selection Based on User Identity
The primary goal of Zone Selection is to enable customers to selectively provide access to specialized infrastructure, such as
China Elite POPs
or
Special Access POPs
, based on the user identity such as Users Groups or Organization Units (OUs).  Administrators can ensure that users requiring high-performance or specific regional access (like China Elite) are automatically routed through the appropriate POPs.
Prerequisite
Supported minimum Client version: 135.0.0
Applicable to tenants with
China Elite subscription
.
Enable Zone Selection
To activate Zone Selection, navigate to
Settings
>
Security Cloud Platform
>
Netskope Client
>
Client Configuration
>
Tunnel Settings
>
Advanced Options
and enable
Zone Selection
. To learn more, view
Zone Selection
.
Implementation Details
The feature allows specific zone selections with Client Configuration profiles:
China Elite: Returns an ordered list of Elite POPs followed by Premium POPs.
China Elite Extended: Returns China Elite Extended POPs (for example, HKG2), followed by Elite POPs and then Premium POPs.
If an administrator chooses China Elite or China Elite Extended in at least one Client Configuration profile, users associated with other Client Configurations that do not have a Zone selection specified will no longer receive China Elite POPs.
China Elite Extended: Supported Use Cases and Guidelines
China Elite Extended is available to China Elite users for two use cases:
Supporting traveling executives or VIP users who need consistent access to sites and apps outside China while in mainland China.
Supporting marketing teams that need access to social media sites to manage ad campaigns.
Approach your Netskope account team to enable the China Elite Extended license.
China Elite Extended is intended for steering specific user groups to solve specific problems, not for routing an entire user base through the service. Netskope enforces this scope to ensure China Elite Extended is provided only to the user groups that need it.
In this Topic
Zone Selection Based on User Identity

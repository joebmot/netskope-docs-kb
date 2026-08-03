# Netskope Docs — Sase
_Generated: 2026-08-03 10:45 UTC_
_Pages: 4_

---
## Borderless SD-WAN
**URL:** https://docs.netskope.com/en/borderless-sd-wan/
**Last Modified:** 2026-06-02T01:38:20+00:00
**Scraped:** 2026-08-03T09:50:09.101780+00:00

Borderless SD-WAN - Netskope Knowledge Portal
Borderless SD-WAN
The enterprise perimeter is expanding, with users and devices everywhere, and apps distributed across multiple clouds. While legacy WAN solutions fail to meet the modern enterprise’s requirements, Borderless SD-WAN ensures a secure, high-quality experience—anywhere and to any cloud. It simplifies the steering of traffic to the Netskope Security Cloud, so customers can more rapidly take advantage of Netskope Intelligent SSE.
For product documentation, see
https://netskope.document360.io/
.
Note
The documentation is behind a login wall. You can log in with your existing credential or sign up.
In this Topic
Borderless SD-WAN

---
## Netskope IPSec with Aruba EdgeConnect SD-WAN
**URL:** https://docs.netskope.com/en/netskope-ipsec-with-aruba-edgeconnect-sd-wan/
**Last Modified:** 2025-08-31T01:55:23+00:00
**Scraped:** 2026-08-03T10:04:34.995763+00:00

Netskope IPSec with Aruba EdgeConnect SD-WAN - Netskope Knowledge Portal
Netskope IPSec with Aruba EdgeConnect SD-WAN
Netskope supports Internet Protocol Security (IPSec) tunnels as a traffic steering method. IPSec VPN tunnels allow you to route web traffic (port 80 and 443) to Netskope using logical tunnel interfaces that terminate to a Netskope IPSec gateway. When you create IPSec tunnels in the Netskope UI, Netskope provides parameters for configuring the tunnels on your router.
You can integrate Netskope and Aruba EdgeConnect appliances in two ways:
Active – Backup Internet Breakout
When an EdgeConnect appliance has access to the Internet using a single internet service provider (ISP), the appliance can create IPSec tunnels to a primary Netskope Point of Presence (POP) and a secondary Netskope POP. The tunnel to the primary POP carries all traffic unless the tunnel or POP becomes unavailable. In this case, the traffic automatically fails over to the secondary POP.
Active – Active Internet Breakout
When an EdgeConnect appliance has access to the internet using two internet service providers (e.g.,
ISP1
and
ISP2
), the appliance can create four IPSec VPN tunnels to the primary and secondary POPs. Only the primary tunnels from both
ISP1
and
ISP2
carry the traffic to the primary POP unless one of the primary tunnels or POPs is unavailable. When you create the Business Intent Overlay policies, you can allow the EdgeConnect appliance to load balance traffic to the primary POP using
ISP1
and
ISP2
by providing the same service name for the primary tunnels from both ISPs. This is a flow-based load balancing method.
This guide illustrates how to configure IPSec tunnels between Netskope and the Aruba EdgeConnect SD-WAN platform running the EdgeConnect OS (ECOS) version 9.2.5.0_94689. To learn more about the steps in ECOS, see the
Aruba EdgeConnect SD-WAN Documentation
.
Prerequisites
Before configuring IPSec, review the
Netskope guidelines
.
Creating IPSec Tunnels in Netskope
To create the IPSec VPN tunnels for Aruba EdgeConnect SD-WAN in the Netskope UI, see
Creating an IPSec Site
.
Creating IPSec Tunnels in Aruba EdgeConnect SD-WAN
To create the IPSec VPN tunnels in Aruba EdgeConnect SD-WAN:
Log in to Aruba EdgeConnect SD-WAN.
Go to
Configuration
>
Tunnels
.
Click
next to the appliance site you want to add a tunnel to.
Choose
Passthrough
.
Click
Add Tunnel
.
In the
Add Passthrough Tunnel
window:
Alias
: Enter a name for the IPSec tunnel.
Mode
: Choose
IPSec
.
IPSec Suite B Preset
: Choose
None
.
Admin
: Choose
up
. which is the default setting for the administrative state of the tunnel.
Local IP
: Select or enter the IP address of the WAN interface for the IPSec tunnel.
Remote IP
: Enter the IPSec Gateway IP addresses of the primary Netskope POP you copied in the Netskope UI. In this example, it’s
163.116.205.38
.
NAT
: Leave as
none
.
Peer/Service
: Enter the name of a new service using the IPSec tunnel. You use this service for configuring breakout to Netskope under Business Intent Overlays.
Auto max BW enabled
: Select this option to let the appliance auto-negotiate the maximum tunnel bandwidth.
Max BW Kbps
: Unavailable if you selected
Auto max BW enabled
.
Click
IKE
:
Pre-shared key
: Enter the pre-shared key you entered in the Netskope UI.
Authentication Algorithm
: Choose
SHA2-256
.
Encryption Algorithm
: Choose encryption cipher you chose in the Netskope UI.
Diffie-Hellman Group
: Choose
14
.
Rekey interval/lifetime
: Leave as
360
minutes.
Dead peer detection
:
Delay time
: Leave as
10
seconds.
Retry count
: You can’t modify this field.
Local IKE identifier
: Enter the source identity you entered in the Netskope UI.
Remote IKE identifier
: Enter the IPSec Gateway IP addresses of the primary Netskope POP you copied in the Netskope UI. In this example, it’s
163.116.205.38
.
Phase 1 mode
: Leave as
Aggressive
.
IKE Version
: Choose
IKE v2
.
Click
IPSec
:
Authentication algorithm
: Choose
SHA2-256
.
Encryption algorithm
: Choose
auto
.
IPSec anti-replay window
: Choose
1024
.
Rekey interval/lifetime
: Enter
360
minutes and
0
megabytes.
Perfect forward secrecy group
: Choose
2
.
Click
Save
.
Repeat the steps to create the backup IPSec tunnel. Use the same values except for the following fields:
Alias
: Enter a unique name for the backup tunnel.
Remote IP
: Enter the IPSec Gateway IP addresses of the failover Netskope POP you copied in the Netskope UI.
Peer/Service
: Enter a new service name to direct traffic to the backup tunnel.
Remote IKE Identifier
: Enter the IPSec Gateway IP addresses of the failover Netskope POP you copied in the Netskope UI.
Adding a Route Policy
You must add a route policy to send traffic through the IPSec tunnel.
To add a route policy:
Go to
Configuration
>
Route Policies
.
Click
next to the appliance site you configured a tunnel for.
Click
Add Rule
.
Click under
Priority
to enter a low value so the rule applies first.
Click under
Set Actions
.
In the
Set Actions
window:
Destination Type
: Choose
Passthrough Tunnel
.
Destination
: Choose the primary IPSec tunnel name you created earlier. In this example, it’s Netskope-Primary.
Fallback
: Leave as
pass-through
.
Click
Save
.
Click
Save
.
Configuring Business Intent Overlay Policies
After creating the IPSec tunnels from the Aruba EdgeConnect appliance to the primary and failover Netskope POPs, you must create Business Intent Overlays (BIOs) that points to those IPSec tunnels. Using access control lists (ACL), specify the applications that you want to forward to Netskope in the BIO policies.
Before creating a BIO, go to
Configuration
>
Template
to create ACLs and apply them to the Aruba EdgeConnect appliance.
To create BIO policies:
Go to
Configuration
>
Business Intent Overlays
.
Click
+New
.
In the
Create Overlay
window, enter a name for the overlay.
Click the overlay you created.
In the
Overlay Configuration
window, for
Match
, choose
Overlay ACL
.
Click
.
In the
Associate ACL
window, click
Add Rule
and
Save
to add an ACL that matches everything.
In the
SD-WAN Traffic to Internal Subnets
tab, drag the
Available Interfaces
to
Build SD-WAN Using These Interfaces
to configure your primary and backup interfaces.
In the
Breakout Traffic to Internet & Cloud Services
tab, click
next to
Available Policies
.
In the
Services
window, under
Service Name
, enter the primary and backup IPSec tunnel names you created earlier, and click
Add
. In this example, it’s Netskope-Primary and Netskope-Backup.
Click
Save
.
In the
Breakout Traffic to Internet & Cloud Services
tab, drag the primary and backup IPSec tunnel names under
Available Policies
to
Preferred Policy Order
in the desired order.
Click
OK
.
Click
Save and Apply Changes to Overlays
.
Click
Save
.
Adding a Route Policy for the BIO
Go to
Configuration
>
Route Policies
.
Click
next to the appliance site you configured a tunnel for.
Click
Add Rule
.
Click under
Priority
to enter a greater value than the previous routing policy.
Click under
Set Actions
.
In the
Set Actions
window:
Destination Type
: Choose
Overlay
.
Destination
: Choose the BIOs overlay name you created earlier. In this example, it’s Netskope.
Fallback
: Choose
drop
.
Click
Save
.
Click
Save
.
Verifying the IPSec Tunnel Status in Aruba EdgeConnect SD-WAN
To verify the IPSec tunnel status in Aruba EdgeConnect, go to
Configuration
>
Tunnels
. The primary and backup tunnels display an
up – active
status:
In this Topic
Netskope IPSec with Aruba EdgeConnect SD-WAN

---
## Netskope Borderless WAN Tenant Plugin
**URL:** https://docs.netskope.com/en/netskope-borderless-wan-tenant-plugin/
**Last Modified:** 2026-05-05T22:35:25+00:00
**Scraped:** 2026-08-03T10:10:09.357962+00:00

Netskope Borderless WAN Tenant Plugin
This document explains how to configure the Netskope Borderless WAN Tenant v1.1.0 plugin in Cloud Exchange. This plugin is responsible for configuring BWAN tenants and collecting events of types Audit, Authentication, Client, Gateway, and System from Netskope Borderless WAN.
Prerequisites
To complete this configuration, you need:
Netskope Borderless WAN Tenant with permission to generate an API token.
Connectivity to Netskope Borderless WAN Tenant host: Example:
https://infiot.api.stage1.infiot.net
CE Version Compatibility
Netskope CE v5.1.1
Borderless WAN Tenant Plugin Support
This plugin is used to pull events from Netskope Borderless WAN Tenant.
Event Types
Yes (Audit, Authentication, Client, Gateway, System)
Alert Types
Not Supported
WebTx
Not Supported
Permissions
You need to have these permissions in the Auth Token:
[
   {
      "rap_privs":[
         "privAuditRecordRead"
      ],
      "rap_resource":"*"
   }
]
API Details
List of APIs Used
API Endpoint
Method
Use Case
/v2/auditevents
GET
Fetch Events from Borderless WAN Tenant.
Fetch Events
API Endpoint:
<BASE URL>
v2/auditevents
Method:
GET
Request Headers
Key
Value
Authorization
Bearer
<API TOKEN>
User-Agent
netskope-ce-5.1.1-tenant-netskope_borderless_wan-v1.1.0
grant_type
client_credentials
Request Parameters
Key
Value
first
100
after
end_cursor (end cursor from previous response)
filter
event_time>="
<START TIME>
" AND event_time<="END TIME" AND (class:
<EVENT TYPE>
)
Example:
event_time>="2025-01-29T12:20:42.124910Z" AND event_time<="2025-01-29T12:58:01.122Z" AND (class: AUDIT OR class:AUTHENTICATION OR class:SYSTEM OR class:CLIENT OR class:GATEWAY)
Sample API Response
{
    "page_info": {
        "end_cursor": "WyIyMDI1LTAxLTI5VDEyOjQzOjIyLjAzNVoiLCI2NzlhMjI2YTIyNmUyYTBmYzU2YzJjOGIiXQ",
        "has_next": true,
        "total_count": 4
    },
    "data": [
        {
            "id": "679a226a226e2a0fc56c2c8b",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:token:6245b39c611790724910338f",
            "target_nrn": "nrn:bwan:site:us:5dadf8a91602d141e060c93e:site:673757abb51faf57f043a36a",
            "type": "AUDIT",
            "subtype": "AUDIT_GATEWAY",
            "activity": "SITE_UPDATED",
            "note": "",
            "event_time": "2025-01-29T12:43:22Z"
        },
        {
            "id": "679a24c905aa7377e0924ab0",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:user:656e127fd8a92afdc8447576",
            "target_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:user:656e127fd8a92afdc8447576",
            "type": "AUTHENTICATION",
            "subtype": "AUTHENTICATION_USER",
            "activity": "USER_LOGIN",
            "note": "",
            "event_time": "2025-01-29T12:53:29Z"
        },
        {
            "id": "679a20d105aa7377e0924931",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:token:675145c90f1ebb6e8c59983b",
            "target_nrn": "nrn:bwan:site:us:5dadf8a91602d141e060c93e:site:675145b90f1ebb6e8c59982a",
            "type": "CLIENT",
            "subtype": "CLIENT_SYSTEM",
            "activity": "SITE_CLIENT_DEVICE_ENROLL_STARTED",
            "note": "",
            "event_time": "2025-01-29T12:36:34Z"
        },
        {
            "id": "679a259d05aa7377e0924afa",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:token:67343709ca023562f3b8f02e",
            "target_nrn": "nrn:bwan:site:us:5dadf8a91602d141e060c93e:site:6734367c1f66fecb2dff8554",
            "type": "GATEWAY",
            "subtype": "GATEWAY_UNDERLAY",
            "activity": "SITE_LINK_UP",
            "note": "wlp0s0",
            "event_time": "2025-01-29T12:57:00Z"
        },
        {
            "id": "679a25b439a4bd42a70bb934",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:token:6245b39c611790724910338f",
            "target_nrn": "nrn:bwan:tenant:us:5dadf8a91602d141e060c93e:tenant:5dadf8a91602d141e060c93e",
            "type": "SYSTEM",
            "subtype": "SYSTEM_SSE_TUNNEL",
            "activity": "SITE_NS_TUNNEL_ERROR",
            "note": "https://tunnel-test.goskope.com (accountId: 62b3a3e3b7f108a3b8b74815): get tunnels: status: 401 -> Unauthorized\naccountId: 62b3a3e3b7f108a3b8b74815",
            "event_time": "2025-01-29T12:57:24Z"
        }
    ]
}
User Agent
netskope-ce-5.1.1-tenant-netskope_borderless_wan-v1.1.0
Workflow
Generate an Auth Token for your Netskope Borderless WAN tenant.
Configure the Netskope Borderless WAN Tenant plugin.
Validate the Netskope Borderless WAN Tenant plugin.
Click play to watch a video.
Generate an Auth Token
Log in to your Netskope Borderless WAN Tenant.
Go to
Settings > API Token
and click
New Token
.
Enter the Token Name, Expiration, and Description per your requirements.
For Permissions, refer to the Permissions section.
Click
Save
and copy the generated token.
The generated token will be used to configure the Netskope BWAN Tenant in Cloud Exchange.
Configure the Netskope BWAN Tenant Plugin
In Cloud Exchange, go to
Settings > Plugins
. Search for and select the
Netskope Borderless WAN Tenant v1.1.0
plugin box.
Enter the tenant parameters. Make sure to enter full tenant URL (Example:
https://infiot.api.stage1.infiot.net
), and then enter the Auth Token your generated previously.
Click
Save
.
Validate the Borderless WAN Tenant Plugin
To verify the configured BWAN Tenant in Cloud Exchange, go to
Settings > Netskope Tenants
. You will see the newly configured tenant in the list.
Troubleshooting the Borderless WAN Tenant Plugin
Receiving error while configuring the tenant
Getting the error:
“TENANT Netskope Borderless WAN Tenant [BWAN Tenant Demo]: Validation error occurred. Unable to establish connection with Netskope Borderless WAN platform. Proxy server or Netskope Borderless WAN server is not reachable.”
What to do:
Verify whether the Base URL of your tenant is entered correctly. Refer to
Connectivity in the following hosts
list item.
Getting the error:
“TENANT Netskope Borderless WAN Tenant [BWAN Tenant Demo]: Validation error occurred. Invalid Auth Token provided in the configuration parameters. Make sure that the Auth Token has all the required permissions and is not expired.”
What to do:
Verify whether the Auth Token of your tenant is entered correctly.
Verify the Auth Token has the necessary permissions. Refer to
Generate an Auth Token
section.
In this Topic
Netskope Borderless WAN Tenant Plugin

---
## Netskope Borderless WAN Plugin for Log Shipper
**URL:** https://docs.netskope.com/en/netskope-borderless-wan-plugin-for-log-shipper/
**Last Modified:** 2026-05-28T22:48:53+00:00
**Scraped:** 2026-08-03T10:10:10.469883+00:00

Netskope Borderless WAN Plugin for Log Shipper - Netskope Knowledge Portal
Netskope Borderless WAN Plugin for Log Shipper
This document explains how to configure the Borderless WAN 1.1.0 plugin with the Log Shipper module of the Netskope Cloud Exchange platform. This plugin is used to fetch Events (Audit, Authentication, Client, Gateway, System) from the
Monitor > Events
page of Netskope Borderless WAN Tenant. The plugin fetches the data in JSON format.
Prerequisites
To complete this configuration, you need:
A Borderless WAN Tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
and
Log Shipper
plugin already configured.
A 3rd-party plugin (like
Syslog
) already configured.
Minimum CE version required 5.1.1 for the plugin configuration.
Connectivity to the Borderless WAN Tenant host.
Example: https://infiot.api.stage1.infiot.net
Borderless WAN Plugin Support
The Borderless WAN plugin is used to pull Events of types Audit, Authentication, Client, Gateway, System from Borderless WAN tenant.
Alerts Support
Not Supported
Event Support
Yes (Audit, Authentication, Client, Gateway, System)
WebTx Support
Not Supported
CE Logs
Not Supported
Permissions
You need to have these permissions in the Auth Token:
[
   {
      "rap_privs":[
         "privAuditRecordRead"
      ],
      "rap_resource":"*"
   }
]
API Details
List of APIs used
API Endpoint
Method
Use Case
/v2/auditevents
GET
Fetch Events from Borderless WAN Tenant.
Note that all the API calls for a source plugin are made from the
Tenant
plugin, so the user agent will be of the tenant plugin.
Fetch Events
API Endpoint:
<BASE URL>
v2/auditevents
Method:
GET
Request Headers
Key
Value
Authorization
Bearer
<API TOKEN>
User-Agent
netskope-ce-5.1.1-tenant-netskope_borderless_wan-v1.1.0
grant_type
client_credentials
Request Parameters
Key
Value
first
100
after
end_cursor (end cursor from previous response)
filter
event_time>="<START TIME>" AND event_time<="END TIME" AND (class: <EVENT TYPE>)
For example:
event_time>="2025-01-29T12:20:42.124910Z" AND event_time<="2025-01-29T12:58:01.122Z" AND (class: AUDIT OR class:AUTHENTICATION OR class:SYSTEM OR class:CLIENT OR class:GATEWAY)
Sample API Response
{
    "page_info": {
        "end_cursor": "WyIyMDI1LTAxLTI5VDEyOjQzOjIyLjAzNVoiLCI2NzlhMjI2YTIyNmUyYTBmYzU2YzJjOGIiXQ",
        "has_next": true,
        "total_count": 4
    },
    "data": [
        {
            "id": "679a226a226e2a0fc56c2c8b",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:token:6245b39c611790724910338f",
            "target_nrn": "nrn:bwan:site:us:5dadf8a91602d141e060c93e:site:673757abb51faf57f043a36a",
            "type": "AUDIT",
            "subtype": "AUDIT_GATEWAY",
            "activity": "SITE_UPDATED",
            "note": "",
            "event_time": "2025-01-29T12:43:22Z"
        },
        {
            "id": "679a24c905aa7377e0924ab0",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:user:656e127fd8a92afdc8447576",
            "target_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:user:656e127fd8a92afdc8447576",
            "type": "AUTHENTICATION",
            "subtype": "AUTHENTICATION_USER",
            "activity": "USER_LOGIN",
            "note": "",
            "event_time": "2025-01-29T12:53:29Z"
        },
        {
            "id": "679a20d105aa7377e0924931",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:token:675145c90f1ebb6e8c59983b",
            "target_nrn": "nrn:bwan:site:us:5dadf8a91602d141e060c93e:site:675145b90f1ebb6e8c59982a",
            "type": "CLIENT",
            "subtype": "CLIENT_SYSTEM",
            "activity": "SITE_CLIENT_DEVICE_ENROLL_STARTED",
            "note": "",
            "event_time": "2025-01-29T12:36:34Z"
        },
        {
            "id": "679a259d05aa7377e0924afa",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:token:67343709ca023562f3b8f02e",
            "target_nrn": "nrn:bwan:site:us:5dadf8a91602d141e060c93e:site:6734367c1f66fecb2dff8554",
            "type": "GATEWAY",
            "subtype": "GATEWAY_UNDERLAY",
            "activity": "SITE_LINK_UP",
            "note": "wlp0s0",
            "event_time": "2025-01-29T12:57:00Z"
        },
        {
            "id": "679a25b439a4bd42a70bb934",
            "actor_nrn": "nrn:bwan:authn:us:5dadf8a91602d141e060c93e:token:6245b39c611790724910338f",
            "target_nrn": "nrn:bwan:tenant:us:5dadf8a91602d141e060c93e:tenant:5dadf8a91602d141e060c93e",
            "type": "SYSTEM",
            "subtype": "SYSTEM_SSE_TUNNEL",
            "activity": "SITE_NS_TUNNEL_ERROR",
            "note": "https://tunnel-test.goskope.com (accountId: 62b3a3e3b7f108a3b8b74815): get tunnels: status: 401 -> Unauthorized\naccountId: 62b3a3e3b7f108a3b8b74815",
            "event_time": "2025-01-29T12:57:24Z"
        }
    ]
}
Performance Matrix
This performance reading is conducted on a Large Stack CE with the below-mentioned VM specifications.
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Events pulled from Borderless WAN
~2.4k EPM
User Agent
netskope-ce-5.1.1-tenant-netskope_borderless_wan-v1.1.0
All the API calls for a source plugin are made from the Borderless WAN tenant plugin, so the user agent will be that of the tenant plugin.
Workflow
Configure the Borderless WAN Plugin for Log Shipper.
Add a Business Rule.
Add a SIEM Mapping.
Validate the Borderless WAN plugin.
Click play to watch a video.
Configure the Borderless WAN Plugin
In Cloud Exchange, go to
Settings > Plugins
. Search for and select the
Netskope Borderless WAN v1.1.0 (CLS)
plugin box.
Add the plugin configuration name and select your configured BWAN tenant.
Configuration Name
: Plugin configuration name.
Tenant
: Tenant to pull alerts from. Select your Borderless WAN tenant.
Ensure that you select the BWAN tenant and not the Netskope tenant, as selecting the wrong tenant will prevent data from being fetched successfully.
Click
Next
and enter values for these parameters:
Event Types
: Selected types of events will be fetched.
Initial Range
: Number of hours to pull the event data for the initial run.
Click
Save
. The plugin configuration will be available on the
Log Shipper > Plugins
page.
To support Borderless WAN events, you need to create a new mapping by cloning an existing one and adding Borderless WAN events to it, or creating a new file by using the
Add Mapping
option. Make sure to use this file while creating the 3rd-party (like the
Syslog
plugin). Follow these steps to create and configure the mapping.
Steps to Create a New Mapping for Borderless WAN Events
Go to the
Settings > Log Shipper > Mappings
.
Click
Add Mapping
.
Enter a name and select
View as Editor
.
Add this mapping file in it.
{
   "delimiter":"|",
   "bwan_map_version":"1.0.0",
   "cef_version":"0",
   "validator":"valid_extensions.csv",
   "taxonomy":{
      "events":{
         "bwan_audit":{
            "header":{
            },
            "extension":{
            }
         }
      },
      "json":{
         "events":{
            "bwan_audit":[
            ],
            "bwan_authentication":[
            ],
            "bwan_client":[
            ],
            "bwan_gateway":[
            ],
            "bwan_system":[
            ]
         }
      }
   }
}
Click
Save
.
Configure a Log Shipper Business Rule for the Borderless WAN Plugin
In Log Shipper, go to
Business Rules
.
By default,there is a business rule that filters all alerts and events. If you want to filter out any specific type of alert or event, click
Create New Rule
, and configure a new business rule by adding the rule name and filter.
If you want to only filter the Borderless WAN Events, create a new rule and select the Borderless WAN types from the following options:
bwan_audit, bwan_authentication, bwan_system, bwan_gateway, and bwan_client
.
Click
Save
.
Configure a Log Shipper SIEM Mapping for the Borderless WAN Plugin
In Log Shipper, go to
SIEM Mappings
and click
Add SIEM Mapping
.
Select the Source plugin (CLS BWAN), the Destination plugin (Syslog, or as per your requirement), and a Business Rule, and then click
Save
.
After the SIEM mapping is added, the data will start being pulled from the Borderless WAN tenant, transformed, and ingested into the Destination platform.
Validate the Borderless WAN Plugin
Validate the Pull
Go to the
Logging
in Cloud Exchange. Search for the pulled logs.
Validate the Events present on Borderless WAN Tenant
Log in to your Borderless WAN tenant.
Go to
Monitor > Events
page.
Troubleshooting the Borderless WAN Plugin
No events are pulled even though the plugin is enabled.
What to do:
Verify whether you have configured the Borderless WAN tenant correctly. Refer to the
Borderless WAN tenant guide
.
Log in to your Borderless WAN tenant and navigate to
Monitor > Events
page then verify whether the events for the same time frame are present or not.
Known Behaviors
1. You may encounter below error in the logs:
02/03/2025 11:15:01 AM
CLS_1014
error
Historical alerts pulling failed for CLS BWAN to CLS Syslog, rule Events.
What to do:
Since we only support pulling Events from BWAN, CE will display this error in the logs.
2. You may encounter below error in the logs:
02/05/2025 12:06:59 PM
–
error
Error occurred while sharing analytics using User-Agent with Netskope
What to do:
Since you are using Borderless WAN Tenant, instead of a Netskope tenant, it will not recognize the User-Agent of Netskope, so it will display this error log.
Limitation
Borderless WAN API Limitations: We have observed inconsistencies in the data returned by BWAN APIs, which may lead to discrepancies in the event counts displayed on the platform versus those received and sent from CE. This is because the BWAN APIs are currently facing the “late breaking events” issue.
In this Topic
Netskope Borderless WAN Plugin for Log Shipper

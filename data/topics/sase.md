# Netskope Docs — Sase
_Generated: 2026-11-06 14:50 UTC_
_Pages: 6_

---
## Borderless SD-WAN
**URL:** https://docs.netskope.com/en/borderless-sd-wan/
**Last Modified:** 2026-06-02T01:38:20+00:00
**Scraped:** 2026-11-06T13:53:55.114467+00:00

Borderless SD-WAN - Netskope Technical Documentation
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
**Scraped:** 2026-11-06T14:07:45.746532+00:00

Netskope IPSec with Aruba EdgeConnect SD-WAN - Netskope Technical Documentation
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
**Scraped:** 2026-11-06T14:12:57.046056+00:00

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
**Scraped:** 2026-11-06T14:12:58.200187+00:00

Netskope Borderless WAN Plugin for Log Shipper - Netskope Technical Documentation
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

---
## Netskope One SD-WAN Licensing Terms
**URL:** https://docs.netskope.com/en/netskope-one-sd-wan-licensing-terms/
**Last Modified:** 2026-08-14T17:15:50+00:00
**Scraped:** 2026-11-06T14:24:05.258163+00:00

Netskope One SD-WAN Licensing Terms - Netskope Technical Documentation
Netskope One SD-WAN Licensing Terms
To learn more:
Netskope One SD-WAN Licensing Terms
The documentation is behind a login wall. You can log in with your existing credential or sign up.
In this Topic
Netskope One SD-WAN Licensing Terms

---
## Netskope Borderless WAN Plugin for Risk Exchange
**URL:** https://docs.netskope.com/en/netskope-borderless-wan-plugin-for-risk-exchange/
**Last Modified:** 2026-11-06T04:24:47+00:00
**Scraped:** 2026-11-06T14:28:31.090274+00:00

Netskope Borderless WAN Plugin for Risk Exchange - Netskope Technical Documentation
Netskope Borderless WAN Plugin for Risk Exchange
Release Notes
2.0.0 (Requires minimum Cloud Exchange version 7.0.0 and minimum Netskope BWAN Tenant version 1.2.0)
Added
Added support for pulling Client and Gateway records from Netskope BWAN platform.
Added support for performing Add to Custom App action.
1.0.0 (Requires minimum Cloud Exchange version 6.1.0)
Added
Initial release.
Actions: Add to Address Group, Remove from Address Group, No Action
Added revert support for the “Add to Address Group” and “Remove from Address Group” actions.
This is an action-only plugin that does not pull any records from Netskope Borderless WAN.
This document explains how to configure the Netskope Borderless WAN v2.0.0 plugin with the Risk Exchange module of the Netskope Cloud Exchange platform. This plugin fetches Clients and Gateways from the Netskope Borderless WAN (BWAN) platform. It supports the Add to Custom App, Add to Address Group and Remove from Address Group actions on the Netskope Borderless WAN platform.
The Netskope Borderless WAN platform exposes no risk score on Clients or Gateways, hence the plugin does not set the Netskope Normalized Score.
Prerequisites
To complete the configuration, you need:
A Netskope tenant (or multiple, for example, production and development/test instances).
A Netskope Cloud Exchange tenant with the
Tenant plugin
,
Risk Exchange plugin
,
Netskope Borderless WAN Tenant plugin
, and a 3rd-party plugin, like
Cisco ISE
, already configured.
A Netskope Borderless WAN instance with a user account and permission to generate API token.
Connectivity to the following hosts:
Netskope Borderless WAN Tenant
Example:
https://
<instance>
.api.stage1.infiot.net
For the Secret Manager configuration, refer to this
documentation
,and to set up Azure Key Vault Secrets Manager, refer to this
documentation
.
Netskope CE v7.0.0 or above.
Netskope Borderless WAN Plugin Support
This plugin fetches Clients and Gateways from the Netskope Borderless WAN (BWAN) platform. It supports the Add to Custom App, Add to Address Group, and Remove from Address Group actions on the Netskope Borderless WAN platform.
Type of Data Pulled
Actions
Client
Gateway
Add to Custom App
Add to Address Group
Remove from Address Group
No Action
Mappings
Pull Mappings for Clients
Plugin Field Label
Expected Data Type
Suggested Field Label
Aggregate Strategy
Example
Client ID
String
NetskopeBWAN_Client_ID
Unique
69df5707462857e5bbcbbab6
Serial Number
String
NetskopeBWAN_Serial_Number
Unique
4CE0460D0G
Name
String
NetskopeBWAN_Name
Overwrite
DESKTOP-PERF4C
User Email
String
NetskopeBWAN_User_Email
Overwrite
asha@example.com
Created At
DateTime
NetskopeBWAN_Created_At
Overwrite
2024-09-02T14:50:53Z
Modified At
DateTime
NetskopeBWAN_Modified_At
Overwrite
2026-07-15T07:07:58Z
Template ID
String
NetskopeBWAN_Template_ID
Overwrite
680b641358f13236ddca9bf0
Labels
List
NetskopeBWAN_Labels
Overwrite
[“quarantine”]
Overlay IPv4 Address
String
NetskopeBWAN_Overlay_IPv4_Address
Overwrite
169.254.0.15
IOT Security
Boolean
NetskopeBWAN_IOT_Security
Overwrite
false
City
String
NetskopeBWAN_City
Overwrite
Boydton
Country
String
NetskopeBWAN_Country
Overwrite
United States
Pull Mappings for Gateways
Plugin Field Label
Expected Data Type
Suggested Field Label
Aggregate Strategy
Example
Gateway ID
String
NetskopeBWAN_Gateway_ID
Unique
6728b4725c474be290cc3df4
Serial Number
String
NetskopeBWAN_Gateway_Serial_Number
Unique
4CE0460D0G
Name
String
NetskopeBWAN_Name
Overwrite
testgwm120
User Email
String
NetskopeBWAN_User_Email
Overwrite
asha@example.com
Created At
DateTime
NetskopeBWAN_Created_At
Overwrite
2024-11-04T11:48:02Z
Modified At
DateTime
NetskopeBWAN_Modified_At
Overwrite
2026-07-06T16:48:32Z
Labels
List
NetskopeBWAN_Labels
Overwrite
[“ntsk”, “rr”]
Tags
List
NetskopeBWAN_Tags
Overwrite
[“branch-office”, “emea”]
Overlay ID
Number
NetskopeBWAN_Overlay_ID
Overwrite
33
Is Activated
Boolean
NetskopeBWAN_Is_Activated
Overwrite
false
Managed
Boolean
NetskopeBWAN_Managed
Overwrite
false
Config Updates Enabled
Boolean
NetskopeBWAN_Config_Updates_Enabled
Overwrite
true
Overlay IPv4 Address
String
NetskopeBWAN_Overlay_IPv4_Address
Overwrite
169.254.0.33
Role
String
NetskopeBWAN_Role
Overwrite
spoke
Hardware Model
String
NetskopeBWAN_Hardware_Model
Overwrite
v600
Model Display Name
String
NetskopeBWAN_Model_Display_Name
Overwrite
iX100W
Software Version
String
NetskopeBWAN_Software_Version
Overwrite
R6.3.149
City
String
NetskopeBWAN_City
Overwrite
Chennai
Country
String
NetskopeBWAN_Country
Overwrite
India
IOT Security
Boolean
NetskopeBWAN_IOT_Security
Overwrite
false
If you have the same records across multiple plugins, make sure to map the same fields in the plugins.
The Netskope Borderless WAN platform exposes no risk score, so the plugin does not set the Netskope Normalized Score. You can build business rules on the mapped attributes instead, such as Is Activated, Config Updates Enabled, Software Version, Role, Tags and Labels for Gateways.
The Serial Number field of Gateways is populated on only some records and does not contain real serial numbers (observed values are MAC-formatted strings), so it must not be used as an identity key.
Overlay IPv4 Address is stored as a string field, but only a single valid IPv4 host address is ever stored. It is a suitable source for the Add to Address Group and Add to Custom App actions.
User Email is best-effort. If the token cannot read users on the Netskope Borderless WAN platform, the entities are still pulled and the records are stored without the User Email value.
Permissions
The API token should have below listed permissions:
[
  {
    "rap_resource": "",
    "rap_privs": [
      "privAddressGroupCreate",
      "privAddressGroupRead",
      "privAddressGroupWrite",
      "privAddressObjectCreate",
      "privAddressObjectDelete",
      "privAddressObjectRead",
      "privCustomAppCreate",
      "privCustomAppDelete",
      "privCustomAppRead",
      "privCustomAppWrite",
      "privManagedDeviceRead",
      "privPolicyRead",
      "privSiteRead",
      "privUserRead"
    ]
  }
]
Make sure the configured
Netskope Borderless WAN Tenant Plugin
has the above listed permissions.
API Details
List of APIs Used
API Endpoint
Method
Use Case
/v2/clients
GET
Validate the connection and pull Clients
/v2/gateways
GET
Pull Gateways
/v2/users
GET
Resolve the User Email field of Clients and Gateways
/v2/custom-apps
GET
List Custom Applications, resolve a name to an identifier and enumerate a roll-over group
/v2/custom-apps
POST
Create a Custom Application or a roll-over sibling
/v2/custom-apps/{id}
GET
Read the traffic definitions of a Custom Application
/v2/custom-apps/{id}
PATCH
Write the traffic definitions of a Custom Application
/v2/custom-apps/{id}
DELETE
Delete a Custom Application left holding no hosts
/v2/app-categories
GET
List categories for the Category dropdown
/v2/address-groups
GET
List Address Groups and resolve a name to an identifier
/v2/address-groups
POST
Create an Address Group
/v2/address-groups/{group-id}/address-objects
GET
List the Address Objects of a group
/v2/address-groups/{group-id}/address-objects
POST
Add an Address Object to a group
/v2/address-groups/{group-id}/address-objects/{id}
DELETE
Remove an Address Object from a group
Clients
Endpoint:
GET /v2/clients
Request Headers
Key
Value
Authorization
Bearer {api_token}
Accept
application/json
Content-Type
application/json
Query Parameters
Parameter
Description
first
Page size. Maximum 100
sort
modified_at
filter
modified_at>='<checkpoint>’ AND modified_at<‘<pull_window_end>’. Omitted on the first run
after
Cursor from the previous response. Omitted on the first page
Sample Response
{
  "page_info": {
    "end_cursor": "WyI2NmQ1ZDBjZGNlM2E1NzExZmE2NGQ3YzUiXQ",
    "has_next": true,
    "total_count": 815
  },
  "data": [
    {
      "created_at": "2024-09-02T14:50:53Z",
      "modified_at": "2026-10-27T09:01:18Z",
      "id": "66d5d0cdce3a5711fa64d7c5",
      "name": "DESKTOP-PERF4C",
      "device_config_raw": {
        "dcfg_1_to_1_nat_rules": [],
        "dcfg_1_to_1_nat_rules_enabled": false,
        "dcfg_auth_binding": {
          "dcfga_auth_enabled": true,
          "dcfga_auth_params": []
        },
        "dcfg_bgp": [],
        "dcfg_bgp2ospf_redis": {
          "bgp2ospf_redis_attrs": {
            "ospf_neighbour_ebgp": false,
            "ospf_neighbour_overlay": false,
            "ospf_redis_metric_ebgp": 100,
            "ospf_redis_metric_overlay": 100,
            "ospf_redis_routemap": "",
            "ospf_redis_type_ebgp": "ospf_redis_type_oe2",
            "ospf_redis_type_overlay": "ospf_redis_type_oe2"
          },
          "bgp2ospf_redis_enabled": false
        },
        "dcfg_bgp_ecmp_enable": false,
        "dcfg_ca_store": {
          "castr_cert_type": "URI",
          "castr_certs": [],
          "castr_device_location": "/etc/ca-certificates"
        },
        "dcfg_client_config": {
          "always_on": false,
          "block_unmanaged": false,
          "disable_dtls": false,
          "disable_sbl": false,
          "disable_vif": true,
          "dns_suffixes": [],
          "dtls_mtu": 1300,
          "ipv4_alloc_method": "template_ipv4_pool",
          "ipv4_dns_servers": [],
          "ipv4_pool_range": [
            {
              "intf_name_id": "hicti-1724854626029",
              "ipv4_pool_end": "10.95.56.220",
              "ipv4_pool_start": "10.95.56.20"
            }
          ],
          "mtu_vif": 0,
          "multilink_support": "",
          "onprem_config": {
            "enabled": false,
            "onprem_detection": {
              "auto": true,
              "dns_config": {
                "check_all": false,
                "enabled": true,
                "hosts": [
                  {
                    "hostipv4": "0.0.0.0",
                    "hostname": ""
                  }
                ]
              },
              "http_config": {
                "check_all": false,
                "enabled": false,
                "http_endpoints": [
                  {
                    "cert_sha1_fingerprint": "",
                    "cert_sha256_fingerprint": "",
                    "check_fingerprint": false,
                    "timeout": 10,
                    "url": ""
                  }
                ]
              }
            }
          },
          "tls_enable": false,
          "user_authentication": {
            "enabled": false,
            "force_auth_onlogin": false,
            "token_expiry": 86400,
            "token_expiry_grace_period": 60
          },
          "vnet_id": 0
        },
        "dcfg_cloud": {
          "account_id": "",
          "cidr": "",
          "keyname": "",
          "pubkey": "",
          "region": "",
          "vmSize": ""
        },
        "dcfg_config_version": "",
        "dcfg_dc_edge": false,
        "dcfg_dns_search": [],
        "dcfg_general": {
          "dcfg_description": "infiot gateway",
          "dcfg_domain": "netskope.com",
          "dcfg_hostname": "netskope.com",
          "dcfg_localadmin_vlan_id": 4094,
          "dcfg_localadmin_wifi_net": "192.168.50.1/24",
          "dcfg_localadmin_wifi_psk": "",
          "dcfg_localadmin_wifi_ssid": "",
          "dcfg_localui_custom_port": 443,
          "dcfg_localui_password": "",
          "dcfg_location": {
            "dloc_address": "",
            "dloc_city": "",
            "dloc_country": "",
            "dloc_hash": "f1f17934834ae2613699701054ef9684",
            "dloc_ip_location": true,
            "dloc_lat": 0,
            "dloc_lng": 0,
            "dloc_state": "",
            "dloc_zip": ""
          },
          "dcfg_maintainer": "infiot",
          "dcfg_ssh_password": "",
          "dcfg_sw_manifest_url": "",
          "dcfg_sw_version": "6.3.250",
          "dcfg_timezone": "US/Pacific",
          "dcfg_ula_prefix": "",
          "dcfg_user": "660104954ce5132d1b51a5aa"
        },
        "dcfg_hardware": {
          "hw_cpu": "arm64",
          "hw_manufacturer": "infiot",
          "hw_model": "v5000",
          "hw_model_display_name": "Client",
          "hw_version": "1.0",
          "hw_version_display_name": ""
        },
        "dcfg_interfaces": [
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_address": "0.0.0.0",
                "intf_advertise": false,
                "intf_dns": {
                  "dns_custom": [],
                  "dns_name": "google",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_family": "ipv4",
                "intf_gateway": "0.0.0.0",
                "intf_mask": "0.0.0.0",
                "intf_name_id": "qzof7-1724854569323",
                "intf_proto": "dhcp",
                "intf_zone": "trusted"
              }
            ],
            "intf_advertise": false,
            "intf_alerts": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "None",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 100000,
            "intf_bandwidth_tx_kbps": 100000,
            "intf_disabled": false,
            "intf_duplex": "full",
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu": 1500,
            "intf_mtu_discovery": "auto",
            "intf_name": "WAN",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 1,
            "intf_zone": "trusted"
          },
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_address": "0.0.0.0",
                "intf_advertise": false,
                "intf_dns": {
                  "dns_custom": [],
                  "dns_name": "google",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_family": "ipv4",
                "intf_gateway": "0.0.0.0",
                "intf_mask": "0.0.0.0",
                "intf_name_id": "v2xkd-1724854569325",
                "intf_proto": "dhcp",
                "intf_zone": "trusted"
              }
            ],
            "intf_advertise": false,
            "intf_alerts": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "None",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 100000,
            "intf_bandwidth_tx_kbps": 100000,
            "intf_disabled": false,
            "intf_duplex": "full",
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu": 1500,
            "intf_mtu_discovery": "auto",
            "intf_name": "LAN",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 1,
            "intf_zone": "trusted"
          }
        ],
        "dcfg_iotsecurity": {
          "dcfg_iotsec_enabled": false,
          "dcfg_iotsec_logging": "none",
          "dcfg_iotsec_tenant_url": ""
        },
        "dcfg_ipsec": [],
        "dcfg_k3s": {
          "k3s_ipv4": "0.0.0.0",
          "k3s_mode": "server",
          "node_name": "infmaster"
        },
        "dcfg_multi_tenant": {
          "ike_port": -1
        },
        "dcfg_name": "DESKTOP-PERF4C",
        "dcfg_netflow_collector": {
          "nflw_collector_ip": "0.0.0.0",
          "nflw_collector_port": 2055,
          "nflw_incoming_filter": {
            "ifltr_iplist": [],
            "ifltr_portlist": [],
            "ifltr_protocol": "tcp"
          },
          "nflw_name": ""
        },
        "dcfg_operating_system": {
          "os_description": "",
          "os_kernel": "4.16",
          "os_os_name": "infiot",
          "os_version": "18.04",
          "os_version_display_string": ""
        },
        "dcfg_ospf": [],
        "dcfg_ospf2bgp_redis": {
          "ospf2bgp_redis_attrs": {
            "bgp_redis_routemap": ""
          },
          "ospf2bgp_redis_enable": false
        },
        "dcfg_overlay": {
          "ovlay_auth": {
            "ovlay_auth_psk": "",
            "ovlay_auth_pubkey": ""
          },
          "ovlay_ipv4": "169.254.0.15",
          "ovlay_netmask": "255.255.255.0",
          "ovlay_netmask_extended": "255.255.0.0"
        },
        "dcfg_pbr_rules": {
          "pbr_rules": []
        },
        "dcfg_port_forwarding_rules": [],
        "dcfg_port_forwarding_rules_enabled": false,
        "dcfg_radios": [],
        "dcfg_radius": [],
        "dcfg_role": "spoke",
        "dcfg_routemap": [],
        "dcfg_schemaver": 10,
        "dcfg_schemaver_minor": 44,
        "dcfg_serial": "",
        "dcfg_sig_gre": [],
        "dcfg_sig_ipsec": [],
        "dcfg_static_routes": [],
        "dcfg_type": "DeviceConfiguration",
        "dcfg_virtual_networks": [
          {
            "client_ip_pool": {
              "ipv4_pool_range": []
            },
            "vnet_bgp": [],
            "vnet_bgp2ospf_redis": {
              "bgp2ospf_redis_attrs": {
                "ospf_neighbour_ebgp": false,
                "ospf_neighbour_overlay": false,
                "ospf_redis_metric_ebgp": 100,
                "ospf_redis_metric_overlay": 100,
                "ospf_redis_routemap": "",
                "ospf_redis_type_ebgp": "ospf_redis_type_oe2",
                "ospf_redis_type_overlay": "ospf_redis_type_oe2"
              },
              "bgp2ospf_redis_enabled": false
            },
            "vnet_bgp_ecmp_enable": false,
            "vnet_bwan_sse": [],
            "vnet_icmp_probes": {
              "icmp_client_tunnel_disable": false,
              "icmp_probes": []
            },
            "vnet_icmp_responders": {
              "icmp_responders": []
            },
            "vnet_id": 0,
            "vnet_ipsec": [],
            "vnet_min_gu_bandwidth": 100,
            "vnet_name": "GLOBAL",
            "vnet_ospf": [],
            "vnet_ospf2bgp_redis": {
              "ospf2bgp_redis_attrs": {
                "bgp_redis_routemap": ""
              },
              "ospf2bgp_redis_enable": false
            },
            "vnet_pbr_rules": {
              "pbr_rules": []
            },
            "vnet_policy": {
              "vpol_id": "66cf30ea8aacce889f86adfe",
              "vpol_local": true,
              "vpol_name": "bwan_client_policy"
            },
            "vnet_routing": [],
            "vnet_sig_gre": [],
            "vnet_sig_ipsec": [],
            "vnet_static_routes": [],
            "vnet_vpnnat_enabled": false,
            "vnet_vpnnat_rules": []
          }
        ],
        "dcfg_vpnnat_enabled": false,
        "dcfg_vpnnat_rules": []
      },
      "template_id": "680b641358f13236ddca9bf0",
      "labels": [
        "bwan1"
      ]
    }
  ]
}
Gateways
Endpoint:
GET /v2/gateways
Request Headers
Key
Value
Authorization
Bearer {api_token}
Accept
application/json
Content-Type
application/json
Query Parameters
Parameter
Description
first
Page size. Maximum 100
sort
modified_at
filter
modified_at>='<checkpoint>’ AND modified_at<‘<pull_window_end>’. Omitted on the first run
after
Cursor from the previous response. Omitted on the first page
Sample Response
{
  "page_info": {
    "end_cursor": "WyI2NzljODE3ZjU0ZjMxODNlNmM3M2Y4ZjciXQ",
    "has_next": true,
    "total_count": 253
  },
  "data": [
    {
      "created_at": "2025-01-31T07:53:35Z",
      "modified_at": "2026-10-22T07:45:21Z",
      "id": "679c817f54f3183e6c73f8f7",
      "name": "001-terraform11",
      "config_updates_enabled": true,
      "device_config_raw": {
        "dcfg_1_to_1_nat_rules": [
          {
            "inat_bidirectional": true,
            "inat_incoming_filter": {
              "ifltr_iplist": [],
              "ifltr_portlist": [],
              "ifltr_protocol": "tcp"
            },
            "inat_lan_ip": "192.168.1.10",
            "inat_lan_port": 0,
            "inat_name": "test",
            "inat_public_ip": "1.1.1.1",
            "inat_public_port": 0,
            "inat_uplink_interface": "GE1",
            "inat_virtual_network": 0
          }
        ],
        "dcfg_1_to_1_nat_rules_enabled": true,
        "dcfg_auth_binding": {
          "dcfga_auth_enabled": true,
          "dcfga_auth_params": []
        },
        "dcfg_bgp": [
          {
            "bfd_interval_ms": 0,
            "bfd_multiplier": 0,
            "bfd_recv_interval_ms": 0,
            "bgp_allow_as_in": false,
            "bgp_bfd": false,
            "bgp_default_originate": false,
            "bgp_default_originate_routemap": "",
            "bgp_inbound_routemap": "",
            "bgp_name": "tgwpeer-2",
            "bgp_outbound_routemap": "",
            "bgp_redis_underlay_overlay": false,
            "bgp_shutdown": false,
            "bgp_vnet": 0,
            "local_as": 400,
            "neighbor": "169.254.1.2",
            "remote_as": 64512,
            "router_id": ""
          }
        ],
        "dcfg_bgp2ospf_redis": {
          "bgp2ospf_redis_attrs": {
            "ospf_neighbour_ebgp": false,
            "ospf_neighbour_overlay": false,
            "ospf_redis_type_ebgp": "ospf_redis_type_oe2",
            "ospf_redis_type_overlay": "ospf_redis_type_oe2"
          },
          "bgp2ospf_redis_enabled": false
        },
        "dcfg_bgp_ecmp_enable": false,
        "dcfg_ca_store": {
          "castr_certs": []
        },
        "dcfg_client_config": {
          "always_on": false,
          "block_unmanaged": false,
          "disable_dtls": false,
          "disable_sbl": false,
          "disable_vif": true,
          "dns_suffixes": [],
          "ipv4_alloc_method": "template_ipv4_pool",
          "ipv4_dns_servers": [],
          "ipv4_pool_range": [],
          "mtu_vif": 0,
          "multilink_support": "",
          "onprem_config": {
            "enabled": false,
            "onprem_detection": {
              "auto": true,
              "dns_config": {
                "check_all": false,
                "enabled": true,
                "hosts": [
                  {}
                ]
              },
              "http_config": {
                "check_all": false,
                "enabled": false,
                "http_endpoints": [
                  {}
                ]
              }
            }
          },
          "user_authentication": {
            "enabled": false,
            "force_auth_onlogin": false,
            "token_expiry": 86400,
            "token_expiry_grace_period": 3600
          },
          "vnet_id": 0
        },
        "dcfg_cloud": {
          "account_id": "",
          "cidr": "",
          "keyname": "",
          "pubkey": "",
          "region": "",
          "vmSize": ""
        },
        "dcfg_dc_edge": false,
        "dcfg_dns_search": [],
        "dcfg_frr_cli_configuration": {
          "cmd_sets": [],
          "enabled": false
        },
        "dcfg_general": {
          "dcfg_description": "",
          "dcfg_domain": "netskope.com",
          "dcfg_high_availability": {
            "dha_sync_enabled": false,
            "dha_wan_intf_tracking_enabled": true
          },
          "dcfg_hostname": "netskope.com",
          "dcfg_localui_password": "<redacted>",
          "dcfg_location": {
            "dloc_address": "",
            "dloc_city": "",
            "dloc_country": "",
            "dloc_ip_location": true,
            "dloc_lat": 0,
            "dloc_lng": 0,
            "dloc_state": "",
            "dloc_zip": ""
          },
          "dcfg_maintainer": "infiot",
          "dcfg_ntp_servers": {},
          "dcfg_ssh_password": "<redacted>",
          "dcfg_sw_manifest_url": "https://swrepo.netskope.com/R6.2.1010-PRIV/swmanifest.json",
          "dcfg_sw_version": "6.3.250",
          "dcfg_timezone": "US/Pacific",
          "dcfg_ula_prefix": "",
          "dcfg_user": ""
        },
        "dcfg_hardware": {
          "hw_cpu": "arm64",
          "hw_manufacturer": "infiot",
          "hw_model": "v500",
          "hw_model_display_name": "iXVirtual",
          "hw_version": "1.0",
          "hw_version_display_name": ""
        },
        "dcfg_ignore_legacy_cli": true,
        "dcfg_interfaces": [
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_dhcp": {
                  "dhcs_address": "0.0.0.0",
                  "dhcs_custom_options": [],
                  "dhcs_dns": {
                    "dns_custom": [],
                    "dns_name": "google",
                    "dns_primary": "8.8.8.8",
                    "dns_secondary": "8.8.4.4"
                  },
                  "dhcs_lease_time_seconds": 86400,
                  "dhcs_network": "255.255.255.255/32",
                  "dhcs_ranges": [],
                  "dhcs_static_binding": []
                },
                "intf_dns": {
                  "dns_custom": [
                    "10.20.12.1",
                    "25.1.2.1"
                  ],
                  "dns_name": "custom",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_dns_proxy": {
                  "intf_forward_dns": [],
                  "intf_reverse_dns": []
                },
                "intf_family": "ipv4",
                "intf_name_id": "ef43m-1740032179934",
                "intf_proto": "dhcp",
                "intf_relay": {
                  "rel_server_ip": "0.0.0.0",
                  "rel_server_ip_list": [
                    "0.0.0.0"
                  ]
                }
              }
            ],
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 100000,
            "intf_bandwidth_tx_kbps": 100000,
            "intf_dedicated_to_ha_sync": false,
            "intf_description": "",
            "intf_disabled": false,
            "intf_duplex": "full",
            "intf_enable_high_perf_mode": false,
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu_discovery": "auto",
            "intf_name": "GE1",
            "intf_nat": true,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_overlay": {
              "ovly_backuptype": "hotstandby",
              "ovly_bw_measurement_mode": "manual",
              "ovly_copy_tos": false,
              "ovly_isbackup": false,
              "ovly_ismetered": false,
              "ovly_preferred_encap_type": "ipsec",
              "ovly_rx_bw_kbps": 10000000,
              "ovly_tag": "wired",
              "ovly_tag_link_id": "67e23e3256d902fbce36eb10",
              "ovly_tag_net_id": "67e23e3256d902fbce36eb14",
              "ovly_tx_bw_kbps": 10000000
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000,
            "intf_type": "ethernet",
            "intf_vlan": 0,
            "intf_zone": "trusted"
          },
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_advertise": false,
                "intf_dhcp": {
                  "dhcs_address": "0.0.0.0",
                  "dhcs_custom_options": [],
                  "dhcs_dns": {
                    "dns_custom": [],
                    "dns_name": "google",
                    "dns_primary": "8.8.8.8",
                    "dns_secondary": "8.8.4.4"
                  },
                  "dhcs_lease_time_seconds": 86400,
                  "dhcs_network": "255.255.255.255/32",
                  "dhcs_ranges": [],
                  "dhcs_static_binding": []
                },
                "intf_dns": {
                  "dns_custom": [
                    "8.8.8.8",
                    "8.8.4.4"
                  ],
                  "dns_name": "custom",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_dns_proxy": {
                  "intf_forward_dns": [],
                  "intf_reverse_dns": []
                },
                "intf_family": "ipv4",
                "intf_name_id": "pxipt-1740032179942",
                "intf_proto": "dhcp",
                "intf_relay": {
                  "rel_server_ip": "0.0.0.0",
                  "rel_server_ip_list": [
                    "0.0.0.0"
                  ]
                }
              }
            ],
            "intf_advertise": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "None",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 1000000,
            "intf_bandwidth_tx_kbps": 1000000,
            "intf_dedicated_to_ha_sync": false,
            "intf_description": "",
            "intf_disabled": false,
            "intf_duplex": "full",
            "intf_enable_high_perf_mode": false,
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu_discovery": "auto",
            "intf_name": "GE2",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_neighbor_ipv4": "",
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 0,
            "intf_vrrp": {
              "is_preemptive": true,
              "preempt_delay": 60,
              "vrrp_advert_int_millisec": 4000,
              "vrrp_advert_int_sec": 4,
              "vrrp_priority": 100,
              "vrrp_state": "master",
              "vrrp_virtual_ip": "1.1.1.1",
              "vrrp_virtual_router_id": 10,
              "vrrp_vmac_enable": false
            },
            "intf_zone": "trusted"
          },
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_advertise": false,
                "intf_dhcp": {
                  "dhcs_address": "0.0.0.0",
                  "dhcs_custom_options": [],
                  "dhcs_dns": {
                    "dns_custom": [],
                    "dns_name": "google",
                    "dns_primary": "8.8.8.8",
                    "dns_secondary": "8.8.4.4"
                  },
                  "dhcs_lease_time_seconds": 86400,
                  "dhcs_network": "255.255.255.255/32",
                  "dhcs_ranges": [],
                  "dhcs_static_binding": []
                },
                "intf_dns": {
                  "dns_custom": [
                    "8.8.8.8",
                    "8.8.4.4"
                  ],
                  "dns_name": "custom",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_dns_proxy": {
                  "intf_forward_dns": [],
                  "intf_reverse_dns": []
                },
                "intf_family": "ipv4",
                "intf_name_id": "7nd5uh-1740032179952",
                "intf_proto": "dhcp",
                "intf_relay": {
                  "rel_server_ip": "0.0.0.0",
                  "rel_server_ip_list": [
                    "0.0.0.0"
                  ]
                }
              }
            ],
            "intf_advertise": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "None",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 1000000,
            "intf_bandwidth_tx_kbps": 1000000,
            "intf_dedicated_to_ha_sync": false,
            "intf_description": "",
            "intf_disabled": false,
            "intf_duplex": "full",
            "intf_enable_high_perf_mode": false,
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu_discovery": "auto",
            "intf_name": "GE3",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 0,
            "intf_zone": "trusted"
          },
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_advertise": false,
                "intf_dhcp": {
                  "dhcs_address": "0.0.0.0",
                  "dhcs_custom_options": [],
                  "dhcs_dns": {
                    "dns_custom": [],
                    "dns_name": "google",
                    "dns_primary": "8.8.8.8",
                    "dns_secondary": "8.8.4.4"
                  },
                  "dhcs_lease_time_seconds": 86400,
                  "dhcs_network": "255.255.255.255/32",
                  "dhcs_ranges": [],
                  "dhcs_static_binding": []
                },
                "intf_dns": {
                  "dns_custom": [],
                  "dns_name": "google",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_dns_proxy": {
                  "intf_forward_dns": [],
                  "intf_reverse_dns": []
                },
                "intf_family": "ipv4",
                "intf_name_id": "ivan3-1740032179957",
                "intf_proto": "dhcp",
                "intf_relay": {
                  "rel_server_ip": "0.0.0.0",
                  "rel_server_ip_list": [
                    "0.0.0.0"
                  ]
                }
              }
            ],
            "intf_advertise": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 100000,
            "intf_bandwidth_tx_kbps": 100000,
            "intf_dedicated_to_ha_sync": false,
            "intf_description": "",
            "intf_disabled": false,
            "intf_duplex": "full",
            "intf_enable_high_perf_mode": false,
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu_discovery": "auto",
            "intf_name": "GE4",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_neighbor_ipv4": "",
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 0,
            "intf_zone": "trusted"
          },
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_advertise": false,
                "intf_dhcp": {
                  "dhcs_address": "0.0.0.0",
                  "dhcs_custom_options": [],
                  "dhcs_dns": {
                    "dns_custom": [],
                    "dns_name": "google",
                    "dns_primary": "8.8.8.8",
                    "dns_secondary": "8.8.4.4"
                  },
                  "dhcs_lease_time_seconds": 86400,
                  "dhcs_network": "255.255.255.255/32",
                  "dhcs_ranges": [],
                  "dhcs_static_binding": []
                },
                "intf_dns": {
                  "dns_custom": [],
                  "dns_name": "google",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_dns_proxy": {
                  "intf_forward_dns": [],
                  "intf_reverse_dns": []
                },
                "intf_family": "ipv4",
                "intf_name_id": "ky59m-1740032179962",
                "intf_proto": "dhcp",
                "intf_relay": {
                  "rel_server_ip": "0.0.0.0",
                  "rel_server_ip_list": [
                    "0.0.0.0"
                  ]
                }
              }
            ],
            "intf_advertise": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 100000,
            "intf_bandwidth_tx_kbps": 100000,
            "intf_dedicated_to_ha_sync": false,
            "intf_description": "",
            "intf_disabled": true,
            "intf_duplex": "full",
            "intf_enable_high_perf_mode": false,
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu_discovery": "auto",
            "intf_name": "GE5",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 0,
            "intf_zone": "trusted"
          },
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_advertise": false,
                "intf_dhcp": {
                  "dhcs_address": "0.0.0.0",
                  "dhcs_custom_options": [],
                  "dhcs_dns": {
                    "dns_custom": [],
                    "dns_name": "google",
                    "dns_primary": "8.8.8.8",
                    "dns_secondary": "8.8.4.4"
                  },
                  "dhcs_lease_time_seconds": 86400,
                  "dhcs_network": "255.255.255.255/32",
                  "dhcs_ranges": [],
                  "dhcs_static_binding": []
                },
                "intf_dns": {
                  "dns_custom": [],
                  "dns_name": "google",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_dns_proxy": {
                  "intf_forward_dns": [],
                  "intf_reverse_dns": []
                },
                "intf_family": "ipv4",
                "intf_name_id": "0e7bd-1740032179966",
                "intf_proto": "dhcp",
                "intf_relay": {
                  "rel_server_ip": "0.0.0.0",
                  "rel_server_ip_list": [
                    "0.0.0.0"
                  ]
                }
              }
            ],
            "intf_advertise": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 100000,
            "intf_bandwidth_tx_kbps": 100000,
            "intf_dedicated_to_ha_sync": false,
            "intf_description": "",
            "intf_disabled": true,
            "intf_duplex": "full",
            "intf_enable_high_perf_mode": false,
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu_discovery": "auto",
            "intf_name": "GE6",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 0,
            "intf_zone": "trusted"
          },
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_advertise": false,
                "intf_dhcp": {
                  "dhcs_address": "0.0.0.0",
                  "dhcs_custom_options": [],
                  "dhcs_dns": {
                    "dns_custom": [],
                    "dns_name": "google",
                    "dns_primary": "8.8.8.8",
                    "dns_secondary": "8.8.4.4"
                  },
                  "dhcs_lease_time_seconds": 86400,
                  "dhcs_network": "255.255.255.255/32",
                  "dhcs_ranges": [],
                  "dhcs_static_binding": []
                },
                "intf_dns": {
                  "dns_custom": [],
                  "dns_name": "google",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_dns_proxy": {
                  "intf_forward_dns": [],
                  "intf_reverse_dns": []
                },
                "intf_family": "ipv4",
                "intf_name_id": "nwofq-1740032179968",
                "intf_proto": "dhcp",
                "intf_relay": {
                  "rel_server_ip": "0.0.0.0",
                  "rel_server_ip_list": [
                    "0.0.0.0"
                  ]
                }
              }
            ],
            "intf_advertise": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 100000,
            "intf_bandwidth_tx_kbps": 100000,
            "intf_dedicated_to_ha_sync": false,
            "intf_description": "",
            "intf_disabled": true,
            "intf_duplex": "full",
            "intf_enable_high_perf_mode": false,
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu_discovery": "auto",
            "intf_name": "GE7",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 0,
            "intf_zone": "trusted"
          },
          {
            "intf_8021x_mab": false,
            "intf_addresses": [
              {
                "intf_advertise": false,
                "intf_dhcp": {
                  "dhcs_address": "0.0.0.0",
                  "dhcs_custom_options": [],
                  "dhcs_dns": {
                    "dns_custom": [],
                    "dns_name": "google",
                    "dns_primary": "8.8.8.8",
                    "dns_secondary": "8.8.4.4"
                  },
                  "dhcs_lease_time_seconds": 86400,
                  "dhcs_network": "255.255.255.255/32",
                  "dhcs_ranges": [],
                  "dhcs_static_binding": []
                },
                "intf_dns": {
                  "dns_custom": [],
                  "dns_name": "google",
                  "dns_primary": "8.8.8.8",
                  "dns_secondary": "8.8.4.4"
                },
                "intf_dns_proxy": {
                  "intf_forward_dns": [],
                  "intf_reverse_dns": []
                },
                "intf_family": "ipv4",
                "intf_name_id": "7c5sa-1740032179970",
                "intf_proto": "dhcp",
                "intf_relay": {
                  "rel_server_ip": "0.0.0.0",
                  "rel_server_ip_list": [
                    "0.0.0.0"
                  ]
                }
              }
            ],
            "intf_advertise": false,
            "intf_allow_mgmt_services": false,
            "intf_allowed_vlans": [],
            "intf_authentication": "",
            "intf_autonegotiation": true,
            "intf_autostart": true,
            "intf_bandwidth_rx_kbps": 100000,
            "intf_bandwidth_tx_kbps": 100000,
            "intf_dedicated_to_ha_sync": false,
            "intf_description": "",
            "intf_disabled": true,
            "intf_duplex": "full",
            "intf_enable_high_perf_mode": false,
            "intf_mac": "00:00:00:00:00:00",
            "intf_mode": "routed",
            "intf_mtu_discovery": "auto",
            "intf_name": "GE8",
            "intf_nat": false,
            "intf_ospf_inline": {
              "intf_ospf_area_attrs_ref": "",
              "intf_ospf_dead_timer_interval_secs": 40,
              "intf_ospf_hello_interval_secs": 10,
              "intf_ospf_md5_attrs": {
                "intf_ospf_md5_keyid": ""
              },
              "intf_ospf_md5_auth_enable": false,
              "intf_ospf_network_type": "ospf_nw_type_broadcast"
            },
            "intf_proxyarp": [],
            "intf_routable_addresses": [],
            "intf_segment": 0,
            "intf_segment_id": 0,
            "intf_speed_mbps": 1000,
            "intf_switch_type": "access",
            "intf_txqueuelen": 1000,
            "intf_type": "ethernet",
            "intf_virtual_network": 0,
            "intf_vlan": 0,
            "intf_zone": "trusted"
          }
        ],
        "dcfg_iotsecurity": {
          "dcfg_iotsec_enabled": false,
          "dcfg_iotsec_logging": "none"
        },
        "dcfg_ipsec": [],
        "dcfg_name": "001-terraform11",
        "dcfg_netflow_collector": {
          "nflw_collector_ip": "0.0.0.0",
          "nflw_collector_port": 2055,
          "nflw_incoming_filter": {
            "ifltr_iplist": [],
            "ifltr_portlist": [],
            "ifltr_protocol": "tcp"
          },
          "nflw_name": ""
        },
        "dcfg_operating_system": {
          "os_version": "18.04"
        },
        "dcfg_ospf": [],
        "dcfg_ospf2bgp_redis": {
          "ospf2bgp_redis_attrs": {},
          "ospf2bgp_redis_enable": false
        },
        "dcfg_overlay": {
          "ovlay_auth": {
            "ovlay_auth_psk": "<redacted>",
            "ovlay_auth_pubkey": "<redacted>"
          },
          "ovlay_ipv4": "169.254.0.86",
          "ovlay_myroutable_addrs": [],
          "ovlay_netmask": "255.255.255.0",
          "ovlay_netmask_extended": "255.255.0.0"
        },
        "dcfg_pbr_rules": {
          "pbr_rules": []
        },
        "dcfg_port_forwarding_rules": [
          {
            "inat_bidirectional": true,
            "inat_incoming_filter": {
              "ifltr_iplist": [],
              "ifltr_portlist": [],
              "ifltr_protocol": "tcp"
            },
            "inat_lan_ip": "192.168.1.10",
            "inat_lan_port": 9000,
            "inat_name": "test",
            "inat_public_ip": "1.1.1.1",
            "inat_public_port": 80,
            "inat_uplink_interface": "GE1",
            "inat_virtual_network": 0
          }
        ],
        "dcfg_port_forwarding_rules_enabled": true,
        "dcfg_radios": [],
        "dcfg_radius": [],
        "dcfg_role": "hub",
        "dcfg_routemap": [],
        "dcfg_schemaver": 10,
        "dcfg_schemaver_minor": 50,
        "dcfg_serial": "string",
        "dcfg_sig_gre": [],
        "dcfg_sig_ipsec": [],
        "dcfg_static_routes": [],
        "dcfg_tags": [
          {
            "inftag_name": "topology.netskope.com",
            "inftag_values": [
              {
                "inftag_id": "6a4e8c6e711f6f454e1542b2",
                "inftag_value": "api-client-GW"
              },
              {
                "inftag_id": "69f9d3ed8ddf3dbbd3fa96e7",
                "inftag_value": "test"
              },
              {
                "inftag_id": "69d5fdec45a6f4774fb005da",
                "inftag_value": "testtag"
              }
            ]
          }
        ],
        "dcfg_type": "DeviceConfiguration",
        "dcfg_virtual_networks": [
          {
            "client_ip_pool": {
              "ipv4_dhcp_relay": {
                "idr_dhcp_network_scope": "",
                "idr_dhcp_servers": [
                  "",
                  ""
                ],
                "idr_dhcp_subnets": [],
                "idr_enabled": false
              },
              "ipv4_domain_list": [],
              "ipv4_name_servers": [],
              "ipv4_pool_range": []
            },
            "vnet_bgp": [
              {
                "bfd_interval_ms": 0,
                "bfd_multiplier": 0,
                "bfd_recv_interval_ms": 0,
                "bgp_allow_as_in": false,
                "bgp_bfd": false,
                "bgp_default_originate": false,
                "bgp_default_originate_routemap": "",
                "bgp_inbound_routemap": "",
                "bgp_name": "tgwpeer-2",
                "bgp_outbound_routemap": "",
                "bgp_redis_underlay_overlay": false,
                "bgp_shutdown": false,
                "bgp_vnet": 0,
                "local_as": 400,
                "neighbor": "169.254.1.2",
                "remote_as": 64512,
                "router_id": ""
              }
            ],
            "vnet_bgp2ospf_redis": {
              "bgp2ospf_redis_attrs": {
                "ospf_neighbour_ebgp": false,
                "ospf_neighbour_overlay": false,
                "ospf_redis_type_ebgp": "ospf_redis_type_oe2",
                "ospf_redis_type_overlay": "ospf_redis_type_oe2"
              },
              "bgp2ospf_redis_enabled": false
            },
            "vnet_bgp_aggregate_routes": [],
            "vnet_bgp_ecmp_enable": false,
            "vnet_bgp_transit_community": "",
            "vnet_bwan_sse": [],
            "vnet_icmp_probes": {
              "icmp_probes": []
            },
            "vnet_icmp_responders": {
              "icmp_responders": []
            },
            "vnet_id": 0,
            "vnet_ipsec": [],
            "vnet_ipsec_tunnels": [],
            "vnet_min_gu_bandwidth": 100,
            "vnet_name": "GLOBAL",
            "vnet_ospf": [],
            "vnet_ospf2bgp_redis": {
              "ospf2bgp_redis_attrs": {},
              "ospf2bgp_redis_enable": false
            },
            "vnet_pbr_rules": {
              "pbr_rules": []
            },
            "vnet_policy": {
              "vpol_id": "",
              "vpol_local": true,
              "vpol_name": ""
            },
            "vnet_routing": [],
            "vnet_sig_gre": [],
            "vnet_sig_ipsec": [],
            "vnet_static_routes": [],
            "vnet_vpnnat_enabled": false,
            "vnet_vpnnat_rules": []
          }
        ],
        "dcfg_vpnnat_enabled": false,
        "dcfg_vpnnat_rules": [],
        "template_user_groups": []
      },
      "labels": [],
      "managed": false,
      "is_activated": true,
      "overlay_id": 86
    }
  ]
}
Users
Endpoint:
GET /v2/users
Request Headers
Key
Value
Authorization
Bearer {api_token}
Accept
application/json
Content-Type
application/json
Sample Response
{
  "page_info": {
    "end_cursor": "WyI2NjAyYjY5NjQzODk4MGVjNDgyZjdiNjEiXQ",
    "has_next": true,
    "total_count": 112
  },
  "data": [
    {
      "created_at": "2024-03-26T11:50:46Z",
      "modified_at": "2024-03-26T11:50:46Z",
      "created_by": {
        "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:user:6441733e9c0fcdaf178d0063",
        "id": "6441733e9c0fcdaf178d0063"
      },
      "modified_by": {
        "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:user:6441733e9c0fcdaf178d0063",
        "id": "6441733e9c0fcdaf178d0063"
      },
      "id": "6602b696438980ec482f7b61",
      "name": "jordan.avery",
      "email": "jordan.avery@netskope.com",
      "raw_role": "infrSystemAdmin",
      "enabled": true,
      "controlled": "sso"
    }
  ]
}
Custom Applications
Endpoint:
GET /v2/custom-apps, POST /v2/custom-apps, GET /v2/custom-apps/{id}, PATCH /v2/custom-apps/{id}, DELETE /v2/custom-apps/{id}
Request Headers
Key
Value
Authorization
Bearer {api_token}
Accept
application/json
Content-Type
application/json
Query Parameters:
(GET /v2/custom-apps)
Parameter
Description
first
Page size. Maximum 100
after
Cursor from the previous response. Omitted on the first page
Request Body:
(POST)
{
  "name": "CE_API_Doc_Test_App",
  "category_id": 24,
  "definitions_v2": [
    {
      "protocol": "tcp",
      "web_access": true,
      "port_range": [ { "start": 443, "end": 443 } ],
      "hosts": [ "198.51.100.25" ]
    }
  ]
}
Request Body:
(PATCH)
{
  "category_id": 24,
  "definitions_v2": [
    {
      "protocol": "tcp",
      "web_access": true,
      "port_range": [ { "start": 443, "end": 443 } ],
      "hosts": [ "198.51.100.25", "198.51.100.26" ]
    }
  ]
}
Sample Response:
(GET)
{
  "page_info": {
    "end_cursor": "WyI2NzJlMzgxZmVjYTBmNGVjZDM2M2Q4NWYiXQ",
    "has_next": true,
    "total_count": 515
  },
  "data": [
    {
      "created_at": "2024-11-08T16:11:11Z",
      "modified_at": "2024-12-28T11:51:52Z",
      "created_by": {
        "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:user:6729ead0cb8cbc88ce68b2d3",
        "id": "6729ead0cb8cbc88ce68b2d3"
      },
      "modified_by": {
        "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:user:65ffabac4ce5132d1b11f65b",
        "id": "65ffabac4ce5132d1b11f65b"
      },
      "id": "672e381feca0f4ecd363d85f",
      "name": "custom_rr2",
      "type": "Instant Messaging",
      "native": false,
      "enabled": true,
      "description": "custom_rr",
      "definitions": [
        {
          "web_access": false,
          "host": "abc.def.ghi.jkl",
          "protocol": "ipv4"
        },
        {
          "web_access": false,
          "host": "hhh.wew.wer.ttt",
          "protocol": "ipv4"
        },
        {
          "web_access": false,
          "host": "1.2.2.2/24",
          "protocol": "ipv4"
        }
      ],
      "definitions_v2": [
        {
          "web_access": false,
          "hosts": [
            "abc.def.ghi.jkl",
            "hhh.wew.wer.ttt",
            "1.2.2.2/24"
          ],
          "protocol": "ipv4"
        }
      ],
      "vid": -4,
      "type_id": 14
    }
  ]
}
Sample Response:
(POST)
{
  "created_at": "2026-10-31T07:50:08Z",
  "modified_at": "2026-10-31T07:50:08Z",
  "created_by": {
    "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:token:6ac888d694a9a8b7bd27958c",
    "id": "6ac888d694a9a8b7bd27958c"
  },
  "modified_by": {
    "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:token:6ac888d694a9a8b7bd27958c",
    "id": "6ac888d694a9a8b7bd27958c"
  },
  "id": "6ae59db0f53ba0968dbd8cfd",
  "name": "CE_API_Doc_Test_App",
  "native": false,
  "enabled": true,
  "definitions": [
    {
      "web_access": true,
      "host": "198.51.100.25",
      "port_range": "443",
      "protocol": "tcp"
    }
  ],
  "definitions_v2": [
    {
      "web_access": true,
      "hosts": [
        "198.51.100.25"
      ],
      "port_range": [
        {
          "start": 443,
          "end": 443
        }
      ],
      "protocol": "tcp"
    }
  ],
  "vid": -4510,
  "category_id": 24
}
Sample Response:
(PATCH)
{
  "created_at": "2026-10-31T07:50:08Z",
  "modified_at": "2026-10-31T07:50:08Z",
  "created_by": {
    "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:token:6ac888d694a9a8b7bd27958c",
    "id": "6ac888d694a9a8b7bd27958c"
  },
  "modified_by": {
    "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:token:6ac888d694a9a8b7bd27958c",
    "id": "6ac888d694a9a8b7bd27958c"
  },
  "id": "6ae59db0f53ba0968dbd8cfd",
  "name": "CE_API_Doc_Test_App",
  "native": false,
  "enabled": true,
  "definitions": [
    {
      "web_access": true,
      "host": "198.51.100.25",
      "port_range": "443",
      "protocol": "tcp"
    },
    {
      "web_access": true,
      "host": "198.51.100.26",
      "port_range": "443",
      "protocol": "tcp"
    }
  ],
  "definitions_v2": [
    {
      "web_access": true,
      "hosts": [
        "198.51.100.25",
        "198.51.100.26"
      ],
      "port_range": [
        {
          "start": 443,
          "end": 443
        }
      ],
      "protocol": "tcp"
    }
  ],
  "vid": -4510,
  "category_id": 24
}
Sample Response:
(DELETE) (Status Code: 200 Empty Response)
Application Categories
Endpoint:
GET /v2/app-categories
Request Headers:
Key
Value
Authorization
Bearer {api_token}
Accept
application/json
Content-Type
application/json
Sample Response:
{
  "name": "CE_API_Doc_Test_App",
  "category_id": 24,
  "definitions_v2": [
    {
      "protocol": "tcp",
      "web_access": true,
      "port_range": [ { "start": 443, "end": 443 } ],
      "hosts": [ "198.51.100.25" ]
    }
  ]
}
Address Groups
Endpoint:
GET /v2/address-groups, POST /v2/address-groups
Request Headers
Key
Value
Authorization
Bearer {api_token}
Accept
application/json
Content-Type
application/json
Request Body:
(POST)
{
  "name": "CE_API_Doc_Test_Group",
  "description": "Temporary group for API response capture"
}
Sample Response:
(GET)
{
  "page_info": {
    "end_cursor": "WyI2ODI4YWFkZDI0MGU1ODY4NzY5YjZiYjkiXQ",
    "has_next": true,
    "total_count": 22
  },
  "data": [
    {
      "created_at": "2025-05-17T15:27:25Z",
      "modified_at": "2026-07-06T05:15:09Z",
      "id": "6828aadd240e5868769b6bb9",
      "name": "AddrGrp1",
      "description": "AddrGrp1asf",
      "usage_type": "static",
      "metadata_tags": [
        "st1",
        "ag1"
      ]
    }
  ]
}
Sample Response:
(POST)
{
  "created_at": "2026-10-31T07:49:56Z",
  "modified_at": "2026-10-31T07:49:56Z",
  "id": "6ae59da4f53ba0968dbd8cd8",
  "name": "CE_API_Doc_Test_Group",
  "description": "Temporary group for API response capture",
  "usage_type": "static"
}
Address Objects
Endpoint:
GET /v2/address-groups/{group-id}/address-objects, POST /v2/address-groups/{group-id}/address-objects, DELETE /v2/address-groups/{group-id}/address-objects/{id}
Request Headers
Key
Value
Authorization
Bearer {api_token}
Accept
application/json
Content-Type
application/json
Query Parameters:
(GET)
Parameter
Description
first
Page size. Maximum 100
after
Cursor from the previous response. Omitted on the first page
Request Body:
(POST)
{
  "name": "198.51.100.25",
  "address": "198.51.100.25",
  "type": "ipv4"
}
Sample Response:
(GET)
{
  "page_info": {
    "end_cursor": "eyJjIjpbeyIkb2lkIjoiNmFlNTlkYTVmNTNiYTA5NjhkYmQ4Y2RhIn1dfQ",
    "has_next": false,
    "total_count": 1
  },
  "data": [
    {
      "created_at": "2026-10-31T07:49:57Z",
      "modified_at": "2026-10-31T07:49:57Z",
      "created_by": {
        "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:token:6ac888d694a9a8b7bd27958c",
        "id": "6ac888d694a9a8b7bd27958c"
      },
      "modified_by": {
        "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:token:6ac888d694a9a8b7bd27958c",
        "id": "6ac888d694a9a8b7bd27958c"
      },
      "id": "6ae59da5f53ba0968dbd8cda",
      "name": "198.51.100.25",
      "address": "198.51.100.25",
      "group_ids": [
        "6ae59da4f53ba0968dbd8cd8"
      ],
      "type": "ipv4"
    }
  ]
}
Sample Response:
(POST)
{
  "created_at": "2026-10-31T07:49:57Z",
  "modified_at": "2026-10-31T07:49:57Z",
  "created_by": {
    "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:token:6ac888d694a9a8b7bd27958c",
    "id": "6ac888d694a9a8b7bd27958c"
  },
  "modified_by": {
    "nrn": "nrn:bwan:authn:ap:643f8d461db9576d498576a9:token:6ac888d694a9a8b7bd27958c",
    "id": "6ac888d694a9a8b7bd27958c"
  },
  "id": "6ae59da5f53ba0968dbd8cda",
  "name": "198.51.100.25",
  "address": "198.51.100.25",
  "group_ids": [
    "6ae59da4f53ba0968dbd8cd8"
  ],
  "type": "ipv4"
}
Sample Response:
(DELETE) (Status code: 200 Empty Response)
Performance Matrix
Here is the performance matrix conducted on a Large CE Stack with these specifications by sharing/removing 1k IPs from the Address Group, pulling 500k clients and gateways and sharing 20k IPs to Custom App.
Description
Specifications
Stack details
Size: Large
RAM: 32 GB
CPU: 16 Cores
Time taken to pull and store clients records
~ 20 minutes
Time taken to pull and store Gateway records
~ 25 minutes
Time taken to share Host/IPs to Custom App
~ 5 minutes
Time taken to share IPs to the Address Group
~ 20 minutes
Time taken to remove IPs from the Address Group
~ 20 minutes
The Netskope Borderless WAN tenant has a maximum limit of 1000 IPs per Address Group.
User Agent
netskope-ce-7.0.0-cre-netskope-borderless-wan-v2.0.0
Workflow
Get your API Token.
Configure the Netskope Borderless WAN plugin.
Configure a Business Rule.
Configure Risk Exchange Actions.
Validate the plugin.
Watch a Video
Click play to watch a video.
Generate a Netskope Borderless WAN API Token
Log in to your Netskope Borderless WAN instance and go to
Settings > API Tokens
.
Click
New Token
.
Provide a Name, Description, and Expiration as per your requirement. Add the permissions listed in the Permissions section.
Click
Review Changes
, verify the permissions, and then click
Save
.
Copy the Generated token. This is need to configure the plugin.
Configure the Netskope Borderless WAN Plugin
In Cloud Exchange, go to
Settings > Plugin Store
. Search for and select the
Netskope Borderless WAN v2.0.0 (CRE)
plugin.
Add a plugin configuration name and select the BWAN tenant.
Click
Next
and enter the Configuration Parameters:
API Token (Optional):
Optional API Token of the Netskope Borderless WAN platform. If provided, it is used for all the API calls instead of the Auth Token of the selected Netskope Borderless WAN Tenant. If not provided, the Auth Token of the Tenant is used. The API Token can be generated from the
Settings > API Tokens
page of the Netskope Borderless WAN tenant.
Click
Next
and select an Entity from the
Entity
dropdown. Provide the field mapping per your needs. To create a new field, under any entity, click
Add Field
.
Provide a Field Label, Data Type, Normalization, Unique, and Aggregate Strategy.
Client ID and Serial Number field will be required to pull the Clients details. Similarly for Gateways entity, Gateway ID and Serial Number is required to pull the Gateways details.
Click
Save
.
Configure a Risk Exchange Business Rule for the Netskope Borderless WAN Plugin
Go to
Risk Exchange > Business Rules
.
Click
Create New Rule
in the top right corner.
Enter a Rule Name. Select the Entity for which Fields have been configured, and configure the query based on your requirements. Here are examples that filter the data fetched from the Cisco ISE plugin.
Click
Save
.
Configure Risk Exchange Actions for the Netskope Borderless WAN Plugin
The Netskope Borderless WAN plugin supports the following action types:
Add to Custom App
: This action allows users to add IP addresses/Hostnames or domains to the Custom Apps on the Netskope Borderless WAN tenant.
Add to Address Group
: This action allows users to add IP addresses to the Address Group on the Netskope Borderless WAN tenant.
Remove from Address Group
: This action allows users to remove IP addresses from the Address Group on the Netskope Borderless WAN tenant.
No Action
: No action will be performed for this action. You can generate UBA alerts in Ticket Orchestrator by using this action, and enabling the
Generate Alerts
toggle.
You can share IPs pulled via
Netskope Risk Exchange plugin
, or any other 3rd-party plugins like
Cisco ISE
to the Address group, and IPs from
Illumio
or other 3rd-party plugins, to Custom Apps on the Netskope Borderless WAN tenant.
Add to a Custom App
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select the required Business Rule, Configuration, and
Add to Custom App
Action from their respective dropdowns.
Enter the Action Parameters:
Custom App Name:
Select an existing Custom Application from the dropdown, or select
Create New custom App
to create one. Static field only.
Create New Custom App:
Name of the Custom Application to create. Required only when Create New Custom App is selected in Custom App Name. Must be at least 6 characters. If a Custom Application with this name already exists, it is used instead. Static field only.
Category:
Category the Custom Application is reported under. It is applied to every Custom Application the action writes, including an existing one. Static field only.
Host:
Host address to append to the Custom Application. Each value must be an IPv4 address, an IPv4 CIDR range, or a domain name/domain of at least two labels, up to 100 characters total and 63 characters per label, optionally with a leftmost wildcard such as *.example.com. One or more Source fields can be selected, and multiple comma-separated values are supported. Source or static field.
Maximum Hosts Per Custom App:
Maximum number of host slots one Custom Application may hold before the action rolls over into a sibling or skips the remainder, as decided by Skip Excess Hosts. A host counts once per selected protocol. The value must be at least 1. Default: 1000. Static field only.
Skip Excess Hosts:
Select No to create roll-over sibling Custom Applications until all the hosts are accommodated. Select Yes to create no siblings and skip the hosts beyond the existing capacity. Default: No. Static field only.
Protocol:
IP protocols the traffic definition matches. One traffic definition is written per selected protocol. Available options are ICMP, TCP, UDP and IPv4. Default: all four. Static field only.
TCP Ports:
Comma-separated ports or port ranges for the TCP protocol, for example 443, 8080-8090. Enter a value only when TCP is selected in Protocol. When left empty, the definition matches the protocol without a port constraint. Static field only.
UDP Ports:
Comma-separated ports or port ranges for the UDP protocol, for example 53, 5000-5010. Enter a value only when UDP is selected in Protocol. When left empty, the definition matches the protocol without a port constraint. Static field only.
Web Access:
Whether the traffic definition matches web traffic. Available options are Yes and No. Default: No. Static field only.
Enable the
Require Approval
toggle if Approval is needed before performing action on the pulled records.
Click
Save
.
Add to an Address Group
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select the required Business Rule, Configuration, and
Add to Address Group
Action from their respective dropdowns.
Enter the Action Parameters:
IPs:
Select the Source field containing IPv4 addresses or IPv4 CIDR ranges, or provide Static comma-separated values to add to the Address Group. IPv6 values are skipped. CIDR ranges are used exactly as provided.
Address Group:
Select an Address Group from the available options, or select ‘Create New Address Group’ to create a new Address Group and add the IPs to it. Select the Address Group from the Static Field dropdown only.
New Address Group Name:
Name of the Address Group to create. Required only when ‘Create New Address Group’ is selected in Address Group. If an Address Group with this name already exists, it is used instead. Provide it in the Static Field.
Description:
Description of the new Address Group. Used only when ‘Create New Address Group’ is selected in Address Group. Ignored if the Address Group already exists. Provide it in the Static Field.
Enable the
Require Approval
toggle if Approval is needed before performing action on the pulled records.
Add to Address Group action supports revert action. Means the user can revert the executed action from the Action logs page.
After the action is reverted successfully, its status will be available under the Revert Action Parameters Details section for that particular action log.
Remove from Address Group
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select the required Business Rule, Configuration, and the
Remove from Address Group
Action from their respective dropdowns.
Enter these Action Parameters:
IPs:
Select the Source field containing IPv4 addresses or IPv4 CIDR ranges, or provide Static comma-separated values to remove from the Address Group. IPv6 values are skipped. CIDR ranges are used exactly as provided. Values are matched exactly, e.g. removing 10.0.0.7 does not remove 10.0.0.0/24.
Address Group:
Select the Address Group to remove the IPs from. Select the Address Group from the Static Field dropdown only.
Enable the
Require Approval
toggle if Approval is needed before performing action on the pulled records.
Click
Save
.
The Remove from Address Group action supports revert action. This means you can revert the executed action from the Action Logs page.
After the action is reverted successfully, its status will be available under the Revert Action Parameters Details section for that particular action log.
No Action
In Risk Exchange, go to
Actions
and click
Add Action Configuration
.
Select the required Business Rule, Configuration, and the
No Action
Action from their respective dropdowns.
Enable the
Require Approval
toggle if Approval is needed before performing action on the pulled records.
Click
Save
.
Validate the Netskope Borderless WAN Plugin
Validate in Cloud Exchange
To validate the pulled records, go to
Risk Exchange > Records
. Select the entity where the records are to be stored.
To verify the logs related to the plugin workflows, go to the
Settings > Logging
page and apply the filter with plugin name or plugin configuration name.
Logs for validating the pull for Clients and Gateway entity:
Logs for Add to Custom App action:
Logs for performed Add to Address Group action:
Logs for performed Remove from Address Group action:
Logs for performed No action:
Logs for performed revert action:
When a pulled record matches one of the configured business rules, the configured action will be performed on the record. This can be seen in the Risk Exchange > Action Logs.
Validate in your Netskope Borderless WAN Instance
The plugin pull Clients and Gateway details from
Manage > Clients
, and
Manage > Gateways
pages in the BWAN tenant.
To validate the Add to Custom App action, go to
Configure > Custom Apps
on the BWAN tenant. Search for and select the Custom App you used for adding the IPs/Host.
To view the Address Groups on Netskope Borderless WAN instance, go to
Configure > Objects > Address Groups
.
Search for the Address Group used in the Action configuration and click on it to open the Address Group.
Address Group after performing Add to Address Group action:
Address Group after performing Remove from Address Group action:
Troubleshooting the Netskope Borderless WAN Plugin
Unable to configure the plugin
If you are unable to configure the plugin, it could be due to one of these reasons:
Incorrect Netskope Borderless WAN tenant URL
BWAN Tenant does not have necessary permissions to configure the CRE Netskope Borderless WAN plugin.
The token provided in the plugin configuration does not have required permissions.
What to do
:
Verify the Netskope Borderless WAN tenant URL in the
BWAN Tenant plugin
.
Verify the API token used by the BWAN Tenant plugin or the CRE Netskope Borderless WAN has required permissions. Refer to the Permissions section.
Unable to pull Client or Gateway records from BWAN
If you are not able to pull the data, it might be because of one of these reasons:
Field mapping is not added for the entity.
No data is available for pulling
Plugin has error in the pull cycle.
What to do:
Edit the plugin, see if any field is mapped for the entity that you want to pull data, if not map the fields. For more details on mapping refer to Mappings.
See if there is any data available on the BWAN tenant for pulling. Refer to validation for the same.
Go to Logging and search for the plugin logs, check if there are any error logs available. If so, expand the same and look for resolution.
IP Already Exists as Address Object
If an action log entry shows Failed for a specific IP during Add to Address Group, it could be due to one of the following reasons:
The IP already exists as an Address Object elsewhere on the Netskope Borderless WAN tenant and cannot be added to another Address Group.
What to do
:
Log in to your Netskope Borderless WAN instance and verify that the IP does not already exist as an Address Object on the tenant.
Remove the duplicate Address Object from the Netskope Borderless WAN console before retrying the action.
Known Behavior
The Netskope BWAN API accepts a wider range of values than the BWAN tenant UI. For example, the API accepts malformed or unsupported entries such as out-of-range CIDR prefixes (like
1.1.1.1/34
), wildcard-only domains (like
*.com
), IPv6 addresses (like
2001:db8::1
), and invalid FQDNs (like
example..com
), whereas the UI rejects them. The plugin is designed to stay in sync with the UI behavior, so it validates values against the UI rules and only accepts values that the BWAN tenant UI would accept. Values that the UI does not accept will be skipped by the plugin, even though the API would have allowed them.
In this Topic
Netskope Borderless WAN Plugin for Risk Exchange

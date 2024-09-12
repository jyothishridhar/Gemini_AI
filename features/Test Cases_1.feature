**Test Plan**

**1. POST with valid payload**

**Test Case:**
- Request:
   - Endpoint: `/V2/preferences`
   - Method: `POST`
   - Payload:
     ```json
     {
       "notificationPreferences": {
         "CDM_DEVICE_FOUND": {
           "enabled": true,
           "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "SMS": false
           }
         }
       }
     }
     ```
- Expected Response:
   - Status Code: 200
   - Response Body:
     ```json
     {
       "notificationPreferences": {
         "CDM_DEVICE_FOUND": {
           "enabled": true,
           "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "SMS": false
           }
         }
       }
     }
     ```

**2. POST with invalid payload (unknown notification type)**

**Test Case:**
- Request:
   - Endpoint: `/V2/preferences`
   - Method: `POST`
   - Payload:
     ```json
     {
       "notificationPreferences": {
         "UNKNOWN_NOTIFICATION_TYPE": {
           "enabled": true,
           "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "SMS": false
           }
         }
       }
     }
     ```
- Expected Response:
   - Status Code: 400
   - Response Body:
     ```json
     {
       "error": "Invalid notification type: UNKNOWN_NOTIFICATION_TYPE"
     }
     ```

**3. POST with invalid payload (unknown medium)**

**Test Case:**
- Request:
   - Endpoint: `/V2/preferences`
   - Method: `POST`
   - Payload:
     ```json
     {
       "notificationPreferences": {
         "CDM_DEVICE_FOUND": {
           "enabled": true,
           "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "UNKNOWN_MEDIUM": false
           }
         }
       }
     }
     ```
- Expected Response:
   - Status Code: 400
   - Response Body:
     ```json
     {
       "error": "Invalid medium: UNKNOWN_MEDIUM"
     }
     ```

**4. GET successful**

**Test Case:**
- Request:
   - Endpoint: `/V2/preferences`
   - Method: `GET`
- Expected Response:
   - Status Code: 200
   - Response Body:
     ```json
     {
       "notificationPreferences": {
         "CDM_DEVICE_FOUND": {
           "enabled": true,
           "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "SMS": false
           }
         },
         "CDM_DEVICE_MISSING": {
           "enabled": true,
           "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "SMS": false
           }
         },
         "CDM_LOW_BATTERY_5PCT": {
           "enabled": true,
           "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "SMS": false
           }
         },
         "CDM_LOW_BATTERY_10PCT": {
           "enabled": true,
             "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "SMS": false
           }
         },
         "CDM_LOW_BATTERY_25PCT": {
           "enabled": true,
             "mediums": {
             "EMAIL": true,
             "IN_APP": false,
             "SMS": false
           }
         }
       }
     }
     ```

**5. OPTIONS request**

**Test Case:**
- Request:
   - Endpoint: `/V2/preferences`
   - Method: `OPTIONS`
- Expected Response:
   - Status Code: 200
   - Response Headers:
     - `Access-Control-Allow-Methods`: `POST, GET, OPTIONS`
     - `Access-Control-Allow-Headers`: `Content-Type, Authorization`
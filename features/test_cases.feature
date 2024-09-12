**Test Case 1:**

* **Scenario:** POST request with valid JSON payload
* **URL:** `/V2/preferences`
* **Method:** POST
* **Headers:**
    * `application: cloud-device-management`
    * `Content-Type: application/json`
    * `Authorization: Bearer eyJra`
* **Payload:**
    ```
    {
        "notificationPreferences": {
            "CDM_DEVICE_FOUND": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            },
            "CDM_DEVICE_MISSING": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            },
            "CDM_LOW_BATTERY_5PCT": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            },
            "CDM_LOW_BATTERY_10PCT": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            },
            "CDM_LOW_BATTERY_25PCT": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            }
        }
    }
    ```
* **Expected Response:** HTTP status code 201 Created

**Test Case 2:**

* **Scenario:** GET request with no payload
* **URL:** `/V2/preferences`
* **Method:** GET
* **Headers:**
    * `application: cloud-device-management`
    * `Content-Type: application/json`
    * `Authorization: Bearer eyJra`
* **Payload:** None
* **Expected Response:** HTTP status code 200 OK, with a JSON response containing the current notification preferences

**Test Case 3:**

* **Scenario:** OPTIONS request
* **URL:** `/V2/preferences`
* **Method:** OPTIONS
* **Headers:**
    * `application: cloud-device-management`
    * `Content-Type: application/json`
    * `Authorization: Bearer eyJra`
* **Payload:** None
* **Expected Response:** HTTP status code 200 OK, with allowed methods in the Allow header

**Test Case 4:**

* **Scenario:** POST request with invalid JSON payload
* **URL:** `/V2/preferences`
* **Method:** POST
* **Headers:**
    * `application: cloud-device-management`
    * `Content-Type: application/json`
    * `Authorization: Bearer eyJra`
* **Payload:**
    ```
    {
        "notificationPreferences": {
            "CDM_DEVICE_FOUND": {
                "enabled": "not a boolean",
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            },
            "CDM_DEVICE_MISSING": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            },
            "CDM_LOW_BATTERY_5PCT": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            },
            "CDM_LOW_BATTERY_10PCT": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            },
            "CDM_LOW_BATTERY_25PCT": {
                "enabled": true,
                "mediums": {
                    "EMAIL": true,
                    "IN_APP": true,
                    "SMS": true
                }
            }
        }
    }
    ```
* **Expected Response:** HTTP status code 400 Bad Request

**Test Case 5:**

* **Scenario:** GET request with invalid header
* **URL:** `/V2/preferences`
* **Method:** GET
* **Headers:**
    * `application: cloud-device-management`
    * `Content-Type: text/plain`
    * `Authorization: Bearer eyJra`
* **Payload:** None
* **Expected Response:** HTTP status code 400 Bad Request

**Test Case 6:**

* **Scenario:** OPTIONS request with invalid header
* **URL:** `/V2/preferences`
* **Method:** OPTIONS
* **Headers:**
    * `application: cloud-device-management`
    * `Content-Type: application/json`
    * `Authorization: Invalid token`
* **Payload:** None
* **Expected Response:** HTTP status code 401 Unauthorized
```typescript
import { SuperTest, Test } from 'supertest';
import { HttpStatus } from '@nestjs/common';

export const request = (server: SuperTest<Test>) => server.get(environment.PreferencesEndpoint);

it('POST with valid payload should be returned with a 200 status code', async () => {
  const response = await request(environment.PublicApiUrl)
    .post(environment.PreferencesEndpoint)
    .send(notificationsTestData.successPreferencesTrue)
    .set('User-Agent', userAgentHeader)
    .set('Authorization', `Bearer ${token}`)
    .set('application', 'cloud-device-management');
  expect(response.statusCode).toBe(HttpStatus.OK);
  expect(response.body).toStrictEqual({
    notificationPreferences: {
      CDM_DEVICE_FOUND: {
        enabled: true,
        mediums: {
          EMAIL: true,
          IN_APP: false,
          SMS: false,
        },
      },
    },
  });
});

it('POST with invalid payload (unknown notification type) should be returned with a 400 status code', async () => {
  const response = await request(environment.PublicApiUrl)
    .post(environment.PreferencesEndpoint)
    .send(notificationsTestData.invalidPayloadUnknownType)
    .set('User-Agent', userAgentHeader)
    .set('Authorization', `Bearer ${token}`)
    .set('application', 'cloud-device-management');
  expect(response.statusCode).toBe(HttpStatus.BAD_REQUEST);
  expect(response.body).toStrictEqual({
    error: 'Invalid notification type: UNKNOWN_NOTIFICATION_TYPE',
  });
});

it('POST with invalid payload (unknown medium) should be returned with a 400 status code', async () => {
  const response = await request(environment.PublicApiUrl)
    .post(environment.PreferencesEndpoint)
    .send(notificationsTestData.invalidPayloadUnknownMedium)
    .set('User-Agent', userAgentHeader)
    .set('Authorization', `Bearer ${token}`)
    .set('application', 'cloud-device-management');
  expect(response.statusCode).toBe(HttpStatus.BAD_REQUEST);
  expect(response.body).toStrictEqual({
    error: 'Invalid medium: UNKNOWN_MEDIUM',
  });
});

it('GET successful should be returned with a 200 status code', async () => {
  const response = await request(environment.PublicApiUrl)
    .set('User-Agent', userAgentHeader)
    .set('Authorization', `Bearer ${token}`)
    .set('application', 'cloud-device-management');
  expect(response.statusCode).toBe(HttpStatus.OK);
  expect(response.body).toStrictEqual({
    notificationPreferences: {
      CDM_DEVICE_FOUND: {
        enabled: true,
        mediums: {
          EMAIL: true,
          IN_APP: false,
          SMS: false,
        },
      },
      CDM_DEVICE_MISSING: {
        enabled: true,
        mediums: {
          EMAIL: true,
          IN_APP: false,
          SMS: false,
        },
      },
      CDM_LOW_BATTERY_5PCT: {
        enabled: true,
        mediums: {
          EMAIL: true,
          IN_APP: false,
          SMS: false,
        },
      },
      CDM_LOW_BATTERY_10PCT: {
        enabled: true,
        mediums: {
          EMAIL: true,
          IN_APP: false,
          SMS: false,
        },
      },
      CDM_LOW_BATTERY_25PCT: {
        enabled: true,
        mediums: {
          EMAIL: true,
          IN_APP: false,
          SMS: false,
        },
      },
    },
  });
});

it('OPTIONS request should be returned with a 200 status code and appropriate headers', async () => {
  const response = await request(environment.PublicApiUrl)
    .options()
    .set('User-Agent', userAgentHeader)
    .set('Authorization', `Bearer ${token}`)
    .set('application', 'cloud-device-management');
  expect(response.statusCode).toBe(HttpStatus.OK);
  expect(response.headers['access-control-allow-methods']).toBe('POST, GET, OPTIONS');
  expect(response.headers['access-control-allow-headers']).toBe('Content-Type, Authorization');
});
```
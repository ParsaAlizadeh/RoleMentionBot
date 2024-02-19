# RoleMentionBot

This telegram bot adds a feature to groups and super-groups similar to mention a role in Discord.
Members can join some roles and get notified when the role mentioned.

## Variables

| Name         | Description                                 | Default |
|:------------:|:--------------------------------------------|:-------:|
| `PREFIX`     | Command Prefix                              | `;`     |
| `BATCH`      | Maximum number of mention in single message | `7`     |
| `MAX_ROLE`   | Maximum number of roles a user can have     | `10`    |
| `TOKEN`      | Bot token                                   | N/A     |
| `REGISTERED` | Registered groups id, separated by `:`      | N/A     |


You may set variables in `.env` file.

### Webhook

In case you want to use webhooks instead of polling, you need to set these extra variables.

| Name              | Description                                                         | Example                 |
|:-----------------:|:--------------------------------------------------------------------|:-----------------------:|
| `DEBUG`           | Set this to `false`                                                 | `false`                 |
| `WEBHOOK_URL`     | Public URL of webhook. RoleMentionBot adds `TOKEN` at the end of it | `https://example.com`   |
| `PORT`            | Local port of webhook                                               | `5000`                  |

You need to setup nginx (or any other reverse proxy) to pass requests
from `{WEBHOOK_URL}/{TOKEN}` to `127.0.0.1:{PORT}/{TOKEN}`.

## Docker
If you know docker, you know...

# Iam57-Bot

**Iam57-Bot** 是五七的机器人后端，基于 **Nonebot2** 框架。本仓库用于整合个人开发的插件，并实现快速部署。

![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-0.1.0-blue)

## 目录

- [简介](#简介)
- [部署](#部署)
- [使用 Dev Container 作为开发模板](#使用-dev-container-作为开发模板)
- [贡献](#贡献)
- [许可证](#许可证)

## 简介

**Iam57-Bot** 是五七的机器人后端，基于 **Nonebot2** 框架。此仓库用于存储开发环境配置，并简化后期部署过程。

## 部署

### 直接部署

请按照以下步骤安装和配置项目：

1. 安装 `pipx` 并通过 `pipx` 安装 `nb-cli` 和 `pdm`：

    ```bash
    python -m pip install pipx
    pipx ensurepath
    pipx install nb-cli
    pipx install pdm
    ```

2. 克隆项目代码：

    ```bash
    git clone https://github.com/iam57ao/iam57-bot.git
    cd iam57-bot
    ```

3. 安装项目依赖：

    ```bash
    pdm install
    ```

### 通过 Docker 部署

使用 `docker-compose` 部署项目：

1. 克隆项目代码：

    ```bash
    git clone https://github.com/iam57ao/iam57-bot.git
    cd iam57-bot
    ```

2. 创建并启动容器：

    ```bash
    docker-compose up -d
    ```

### 环境变量

环境变量配置文件包括：

- **.env**：通用环境变量配置
- **.env.dev**：开发环境配置
- **.env.prod**：生产环境配置

请根据NoneBot2官方文档进行配置。通过 `docker-compose` 部署默认开放5705端口。

## 使用 Dev Container 作为开发模板

要使用 Dev Container 作为开发模板，请按照以下步骤操作：

1. 克隆项目代码：

    ```bash
    git clone https://github.com/iam57ao/iam57-bot.git
    cd iam57-bot
    ```

2. 在 VS Code 或 PyCharm 中打开项目，并使用 `.devcontainer` 构建和启动容器。

3. 你现在可以在容器中进行开发，所有必要的工具和依赖都已预先配置好。

## 贡献

欢迎为本项目贡献代码！

### 贡献准则

- 请确保代码符合项目的编码风格和规范。
- 提交前请充分测试，以确保代码的正确性和稳定性。
- 提供详细的描述和相关文档，以帮助他人理解你的更改。
- 尊重项目的代码所有权和许可证协议。

感谢你的贡献和支持！

## 许可证

本项目采用 [MIT 许可证](LICENSE) 许可。

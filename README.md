# Local AI Hub - 本地私有 AI 工作台 | Self-hosted Local AI Workspace

[![Build](https://github.com/however-yir/local-ai-hub/actions/workflows/build-release.yml/badge.svg)](https://github.com/however-yir/local-ai-hub/actions/workflows/build-release.yml)
[![Docs](https://img.shields.io/badge/docs-README-0A7EFA)](https://github.com/however-yir/local-ai-hub#readme)
[![License](https://img.shields.io/badge/license-See%20repo-16A34A)](./LICENSE)
[![Status](https://img.shields.io/badge/status-active-2563EB)](https://github.com/however-yir/local-ai-hub)

> Status: `active`
>
> Upstream: `open-webui/open-webui`
>
> Attribution: upstream license remains in `LICENSE`; fork boundary and redistribution notes are maintained in `LICENSE.HOWEVER` and `NOTICE.md`.
>
> Series: [LZKB](https://github.com/however-yir/LZKB) · [yourrag](https://github.com/however-yir/yourrag)

> A personalized, self-hosted AI workspace forked from Open WebUI.

`Local AI Hub` 的角色不是知识库平台，也不是企业 RAG 平台，而是“本地 AI 工作台”。  
它更强调模型接入、私有部署、工作台体验、团队内日常使用与后续能力扩展。

![Local AI Hub Splash](./static/static/brand-splash.svg)

## Demo 媒体

> 当前仓库已补入一张现有运行界面图；后续会继续替换为完全品牌化后的最新实拍截图。

![Local AI Hub workspace capture](./demo.png)

## 项目快照

- 定位：本地优先、自托管的 AI 工作台。
- 亮点：Open WebUI 深度定制、Docker 部署、模型网关、品牌脱钩与私有化配置。
- 最短运行路径：`cp .env.example .env && docker compose up -d --build`
- 系列分工：`Local AI Hub` 负责工作台入口，`LZKB` 负责知识平台，`YourRAG` 负责企业 RAG/Agent 交付。

## AI 平台分工矩阵

| Repo | 主要角色 | 部署形态 | 最适合的场景 |
| --- | --- | --- | --- |
| `Local AI Hub` | 本地 AI 工作台 | 自托管工作台 | 模型接入、团队日用、统一入口 |
| `LZKB` | 知识库平台 | 本地优先平台 | 文档入库、知识运营、检索问答 |
| `YourRAG` | 企业 RAG/Agent 平台 | 企业交付导向 | 私有化部署、RAG + Agent 交付 |

## 项目定位
`Local AI Hub` 是基于 `open-webui` 深度定制的私有化 AI 工作台，面向本地部署、团队协作、模型编排与知识工作流。

本仓库当前目标：
- 强化本地/私有部署能力（数据库、Redis、模型网关）。
- 完成品牌与工程层脱钩（名称、Logo、仓库元数据、协议）。
- 保留上游兼容性（核心运行方式不变，新增项目级入口）。

## 本次已完成改造

### 1) 品牌与命名
- 项目名改为 `Local AI Hub`。
- 前端默认应用名改为 `Local AI Hub`（`src/lib/constants.ts`）。
- 页面默认标题改为 `Local AI Hub`（`src/app.html`）。
- 通知标题从硬编码 `Open WebUI` 改为动态 `$WEBUI_NAME`。
- 新增品牌资源：`brand-logo.svg`、`brand-splash.svg`。
- PWA manifest 名称改为 `Local AI Hub`。

### 2) 包名与入口
- `package.json` 包名改为 `local-ai-hub`。
- `pyproject.toml` 包名改为 `local-ai-hub`。
- 保留 `open-webui` 命令兼容。
- 新增 CLI 入口：`local-ai-hub`。

### 3) 配置模板（DB / Redis / 模型地址）
- 完整重写 `.env.example`。
- 新增 `.env.local.example`（开发环境模板）。
- 新增 `.env.production.example`（生产环境模板）。
- 增加数据库与 Redis 的标准化示例配置。
- 增加 OpenAI/Ollama 别名环境变量说明，便于迁移。

### 4) 后端配置重构
- 抽离品牌元数据：`backend/open_webui/utils/branding.py`。
- FastAPI 标题改为动态 `WEBUI_NAME`。
- `manifest.json` 描述和图标改为品牌模块驱动。
- OAuth 动态客户端注册名称改为 `WEBUI_NAME`。
- OpenRouter 头部 `X-Title` 与 `HTTP-Referer` 改为品牌配置。

### 5) 数据与部署默认值优化
- `env.py` 新增 `PROJECT_NAME / PROJECT_SLUG` 机制。
- `WEBUI_NAME` 不再强制追加 `(Open WebUI)`。
- `DATABASE_URL` 支持 `APP_DATABASE_URL` 别名与本地回退策略。
- `REDIS_URL` 支持 `APP_REDIS_URL` 别名。
- `REDIS_KEY_PREFIX` 默认改为项目 slug。

### 6) Docker 与仓库元信息
- Docker 镜像/容器名改为 `local-ai-hub` 语义。
- `docker-compose.yaml` 新增 Redis 服务并默认接入。
- OTel compose 的服务名和卷名同步品牌化。
- 新增 `.github/settings.yml`（仓库描述、首页、Topics 模板）。

### 7) 协议与治理
- 新增 `PROJECT_PROTOCOL.md`，定义本项目的品牌、协作、安全与维护约束。

## 快速开始

### 方式 A：Docker Compose（推荐）
```bash
cp .env.example .env
# 按需编辑 .env 中的 OPENAI_API_KEY / DATABASE_URL / CORS_ALLOW_ORIGIN 等

docker compose up -d --build
```

默认端口：`http://localhost:3000`

### 三档启动（无 Ollama / 有 Ollama / 生产 Redis）

```bash
# 1) 无 Ollama（连接外部 Ollama，保留本地 Redis）
cp .env.local.example .env
./scripts/start-profile.sh no-ollama

# 2) 有 Ollama（本地一体化）
cp .env.local.example .env
./scripts/start-profile.sh with-ollama

# 3) 生产 Redis（外部 Redis + 外部 Ollama）
cp .env.production.example .env
./scripts/start-profile.sh prod-redis
```

建议：

- `no-ollama`：开发机内存有限，但已有外部 Ollama。
- `with-ollama`：本地演示与功能联调。
- `prod-redis`：预生产/生产，Redis 不再走 compose 默认容器。

### 方式 B：本地开发（前后端）
```bash
cp .env.local.example .env.local

# 前端
npm install
npm run dev:local

# 后端（另开终端）
cd backend
./start.sh
```

## 核心配置建议

### 数据库
生产推荐 PostgreSQL：
```env
DATABASE_URL=postgresql://user:password@postgres:5432/local_ai_hub
```

### Redis
生产建议启用（WebSocket / 会话 / 任务协同）：
```env
REDIS_URL=redis://redis:6379/0
REDIS_KEY_PREFIX=local-ai-hub
```

### 模型网关
```env
OLLAMA_BASE_URL=http://ollama:11434
OPENAI_API_BASE_URL=https://api.openai.com/v1
OPENAI_API_KEY=replace_with_secure_key
```

## 部署剖面矩阵

| 形态 | 入口文件 | 适合场景 |
| --- | --- | --- |
| 标准自托管 | `docker-compose.yaml` | 默认本地工作台部署 |
| GPU 版 | `docker-compose.gpu.yaml` | 本地 GPU 推理与工作台一体化 |
| API 偏后端 | `docker-compose.api.yaml` | 仅开放 API / backend 能力 |
| 数据依赖拆分 | `docker-compose.data.yaml` | 单独准备数据库与状态服务 |
| 可观测版 | `docker-compose.otel.yaml` | 需要 OTel 追踪与运维接入 |
| UI 自动化 | `docker-compose.playwright.yaml` | 页面冒烟与交互验证 |

## 模型提供方兼容矩阵

| 提供方类型 | 关键配置 | 最适合的使用方式 |
| --- | --- | --- |
| Ollama / 本地模型 | `OLLAMA_BASE_URL` | 本地优先、数据不出机 |
| OpenAI 兼容网关 | `OPENAI_API_BASE_URL` + `OPENAI_API_KEY` | SaaS 或私有代理统一接入 |
| OpenRouter / 多模型代理 | 同 OpenAI 兼容配置 | 多模型路由与团队统一出口 |
| Redis / 数据库扩展 | `REDIS_URL`, `DATABASE_URL` | 多会话、任务协同与持久化 |

## 文档入口

| 入口 | 路径 | 说明 |
| --- | --- | --- |
| 项目文档首页 | `docs/README.md` | 总览与导航 |
| 安全说明 | `docs/SECURITY.md` | 私有部署与安全建议 |
| 协作协议 | `PROJECT_PROTOCOL.md` | fork 后的治理边界 |
| 品牌资源 | `static/static/brand-splash.svg` | README 与首屏品牌资产 |

## 与上游 Open WebUI 的区别
- 目标定位：从通用开源界面，转向“个人/团队可运营”的私有 AI 工作台。
- 品牌体系：完整替换项目名称、Logo、PWA 元信息、仓库元数据模板。
- 部署策略：新增 Redis 默认接入与生产配置模板。
- 配置治理：增加别名环境变量，方便历史环境平滑迁移。
- 工程治理：新增项目协议文件，定义持续维护约束。

## GitHub 仓库元信息建议
已在 `.github/settings.yml` 提供模板：
- Repository Name: `local-ai-hub`
- Description: Personalized self-hosted AI workspace forked from Open WebUI...
- Topics: `ai`, `llm`, `self-hosted`, `ollama`, `rag`, `fastapi`, `svelte`, `local-ai`, `chinese-localization`

> 如使用 Settings App，可自动同步这些仓库设置。

## 兼容性说明
- 内部 Python 包命名空间仍为 `open_webui`，用于最大限度保持上游兼容。
- 已新增项目入口 `local-ai-hub`，同时保留 `open-webui` 兼容命令。

## 协议与许可证
- 项目协议：[`PROJECT_PROTOCOL.md`](./PROJECT_PROTOCOL.md)
- 原始许可证与历史：[`LICENSE`](./LICENSE), [`LICENSE_HISTORY`](./LICENSE_HISTORY)

本项目协议是补充治理文件，不替代原许可证义务。

## 后续路线图
- 持续同步上游关键安全修复。
- 补充 CI 的 fork-specific 回归检查。
- 增加定制功能模块（组织权限、企业审计、模型路由策略）。
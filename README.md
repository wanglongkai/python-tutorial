# python

## 安装uv

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
set Path=C:\Users\admin\.local\bin;%Path%
```

```shell
# 初始化项目
uv init

# 安装依赖(并会同时创建.venv虚拟环境)
uv add pands

# 进入虚拟环境
.venv\Scripts\activate
```

<!-- 配置deepseek API Key -->

sk-7a7158cf81884ce6993c86eb457a6e2b

# 虚拟环境中安装jupyter

`uv add jupyter`
虚拟环境中使用jupyter

方法1：`uv run jupyter notebook`

方法2：

```shell
.\.venv\Scripts\activate
jupyter notebook
```

## 同步依赖
根据pyproject.toml同步依赖,并会自动创建.venv虚拟环境
```shell
uv sync
```

## 运行项目
不用手动激活虚拟环境,直接使用uv运行项目即可自动激活虚拟环境
```shell
uv run xxx.py
```

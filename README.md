# Dify x Oceanbase Integration

## Description

This guide provides instructions on how to integrate Dify with Oceanbase, a distributed relational database management system. By following these steps, you can set up a seamless connection between Dify and Oceanbase for efficient data management and retrieval.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python version ≥ 3.12
- Dify CLI
- Homebrew (for Mac users)

## Part 1: Dify Setup

### Cloud Version

Open cloud.dify.ai, create an account and login.

### Self-Hosted

```bash
git clone https://github.com/langgenius/dify.git
cd dify
cd docker
cp .env.example .env
docker compose up -d
```

Using homebrew to install [Dify Cli](https://github.com/langgenius/homebrew-dify)

### MacOS
```base
brew install langgenius/dify/dify
```

### Linux
```bash
# Download dify-plugin-linux-amd64
chmod +x dify-plugin-linux-amd64
./dify-plugin-linux-amd64 version
# Rename and move to system path
# Example (macOS ARM)
mv dify-plugin-darwin-arm64 dify
sudo mv dify /usr/local/bin/
dify version
```

## Part 2: Oceanbase Setup

[Seekdb](https://github.com/oceanbase/seekdb) is the lightweight, embedded version of OceanBase Database - a powerful AI search database designed for the AI applications. It combines enterprise-grade database capabilities with cutting-edge **AI search ** features, such as Vector search, fulltext search, Json.

```bash
docker run -d \
  --name seekdb \
  -p 2881:2881 \
  -v ./data:/var/lib/oceanbase/store \
  oceanbase/seekdb:latest
```

## Part 3: Develop a plugin

ow you are ready to go! The CLI will create a new directory with the plugin name you provided, and set up the basic structure for your plugin.

```bash
cd hello-world
```

## Run the Plugin

Make sure you are in the hello-world directory

```bash
cp .env.example .env
```

Edit the `.env` file to set your plugin's environment variables, such as API keys or other configurations. You can find these variables in the Dify dashboard. Log in to your Dify environment, click the “Plugins” icon in the top right corner, then click the debug icon (or something that looks like a bug). In the pop-up window, copy the “API Key” and “Host Address”. (Please refer to your local corresponding screenshot, which shows the interface for obtaining the key and host address)


```bash
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=debug-plugin.dify.dev
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=********-****-****-****-************
```

Now you can run your plugin locally using the following command:

```bash
pip install -r requirements.txt
python -m main
```
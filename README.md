# Paper Selection Tool

> **Author: [StevenChaoo](https://github.com/StevenChaoo)**

![vscode](https://img.shields.io/badge/visual_studio_code-007acc?style=flat&logo=visual-studio-code&logoColor=ffffff) ![neovim](https://img.shields.io/badge/Neovim-57a143?style=flat&logo=Neovim&logoColor=ffffff) ![git](https://img.shields.io/badge/Git-f05032?style=flat&logo=git&logoColor=ffffff)

This blog is written by **Neovim** and **Visual Studio Code**. You may need to clone this repository to your local and use **Visual Studio Code** to read. ***Markdown Preview Enhanced*** plugin is necessary as well.

## Introduction

Reading paper is an invigoration work. However, memorizing which paper containing what method is quiet hard for researchers. The motivation of writing this simple tool is a naive idea to quickly locate paper I've read before. For a better taste, **YOU NEED TO PUT ALL PAPERS YOU HAVE READ IN A SPECIFIC FOLDER**. This tool can run on MacOS and Linux.

## Usage

1. Install & Run

```bash
# Install requirement library
pip install colorama -i https://mirror.baidu.com/pypi/simple/

# Run Retrieve.py
python Retrieve.py
```

2. You need to select **MODE** first (`s` for search or `o` for open). Then enter the key words (Searching words for `s` mode and result index for `o` mode)

```bash
# Search mode
Please enter command (MODE + KEY WORDS): s joint
1. xxx xxx xxx Joint xxx xxx xxx.pdf
2. xxx xxx Joint xxx xxx.docx
...
  
# Open mode
Please enter command (MODE + KEY WORDS): o 2

Open xxx\ xxx\ Joint\ xxx\ xxx.docx
```

## Coming Features

- More friendly user interface
- More friendly fonts color
- Migrate to npm framework

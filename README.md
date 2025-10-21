# NASA MCP Project

## Setup and Usage

### Clone the Project
bash git clone [https://github.com/extraterestra/nasa_mcp.git](https://github.com/extraterestra/nasa_mcp.git)


### Install Dependencies
Run the following command in the terminal from the root directory of the project to add required dependencies:
bash uv add python-dotenv requests mcp


### Run MCP Inspector Locally
To run the MCP Inspector locally:
- Launch `mcp-inspector`.
- When connecting to the MCP server using **Run locally** or **Start server**, provide the **absolute path** to the Python server file:  
  `nasa_mcp_my/nasa_mcp_server_my.py`.

---

## Setup MCP Server in Claude

### Create the Configuration File (MacOS)
Run the following commands to create the configuration file:

# Setup MCP Server in Claude

### Create the Configuration File (MacOS)
Run the following commands to create the configuration file:

bash mkdir -p ~/Library/Application\ Support/Claude && touch ~/Library/Application\ Support/Claude/claude_desktop_config.json


### Verify Configuration
Check if the file was created:

/Library/Application Support/Claude/claude_desktop_config.json

### Add the Following Content to the File

{
  "mcpServers": {
    "nasa_mcp_my": {
      "command": "uv",
      "args": [
        "--directory",
        "<Absolute path to project on your machine>",
        "run",
        "nasa_mcp_server_my.py"
      ]
    }
  }
}

Make sure to replace `<Absolute path to project on your machine>` with the **absolute path** of the project folder.

---

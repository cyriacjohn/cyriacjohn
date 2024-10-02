{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5FmglnCbChi2rBodyC4Qc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/cyriacjohn/cyriacjohn/blob/main/demo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 384
        },
        "id": "p0iGJAU5-_wb",
        "outputId": "edd048a4-f825-4cda-8f9a-811ad41e8f25"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'chainlit'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-bbe5619371b0>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mchainlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mcl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m@\u001b[0m\u001b[0mcl\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtype\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"tool\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32masync\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mtool\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'chainlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import chainlit as cl\n",
        "\n",
        "\n",
        "@cl.step(type=\"tool\")\n",
        "async def tool():\n",
        "    # Fake tool\n",
        "    await cl.sleep(2)\n",
        "    return \"Response from the tool!\"\n",
        "\n",
        "\n",
        "@cl.on_message  # this function will be called every time a user inputs a message in the UI\n",
        "async def main(message: cl.Message):\n",
        "    \"\"\"\n",
        "    This function is called every time a user inputs a message in the UI.\n",
        "    It sends back an intermediate response from the tool, followed by the final answer.\n",
        "\n",
        "    Args:\n",
        "        message: The user's message.\n",
        "\n",
        "    Returns:\n",
        "        None.\n",
        "    \"\"\"\n",
        "\n",
        "    final_answer = await cl.Message(content=\"\").send()\n",
        "\n",
        "    # Call the tool\n",
        "    final_answer.content = await tool()\n",
        "\n",
        "    await final_answer.update()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "tbNTQHoH_U4Y"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
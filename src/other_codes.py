from textnode import *
from htmlnode import *
import re


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception(f"Unknown TextType {text_node.text_type}")
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        split_text = node_text.split(delimiter)
        for i, text in enumerate(split_text):
            if i == 0 or i == len(split_text) - 1:
                new_nodes.append(TextNode(text, node.text_type))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes

def extract_markdown_images(text):
    image_urls = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    # Return a list of tuples containing the alt text and the URL
    return [(alt, url) for alt, url in image_urls]

def extract_markdown_links(text):
    markdown_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    # Return a list of tuples containing anchor text and URLs
    return [(anchor_text, url) for anchor_text, url in markdown_links]

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            # If the node is not of type TEXT, keep it as is
            new_nodes.append(old_node)
            continue

        # Extract links from the text
        markdown_links = extract_markdown_links(old_node.text)
        if not markdown_links:
            # If no links are found, keep the node as is
            new_nodes.append(old_node)
            continue

        # Split the text and create new nodes
        text = old_node.text
        last_index = 0
        for match in re.finditer(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text):
            start, end = match.span()
            anchor_text, url = match.groups()

            # Add the text before the link as a TextNode
            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))

            # Add the link as a TextNode with TextType.LINK
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            last_index = end

        # Add any remaining text after the last link
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))

    return new_nodes



def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            # If the node is not of type TEXT, keep it as is
            new_nodes.append(old_node)
            continue

        # Extract images from the text
        markdown_images = extract_markdown_images(old_node.text)
        if not markdown_images:
            # If no images are found, keep the node as is
            new_nodes.append(old_node)
            continue

        # Split the text and create new nodes
        text = old_node.text
        last_index = 0
        for match in re.finditer(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text):
            start, end = match.span()
            alt_text, url = match.groups()

            # Add the text before the image as a TextNode
            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))

            # Add the image as a TextNode with TextType.IMAGE
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            last_index = end

        # Add any remaining text after the last image
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    processed = split_nodes_delimiter([node], "**", TextType.BOLD)
    processed = split_nodes_delimiter(processed, "_", TextType.ITALIC)
    processed = split_nodes_delimiter(processed, "`", TextType.CODE)
    processed = split_nodes_link(processed)
    processed = split_nodes_image(processed)
    return processed




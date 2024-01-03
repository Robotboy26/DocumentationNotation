def generateStyle(backgroundColor, normalColor, fontSize, width, height):
    cssLines = []
    print(f"{backgroundColor}, {normalColor}, {fontSize}, {width}, {height}")
    cssLines.append(f"""body {{
            font-family: Arial, sans-serif;
            font-size: {fontSize}px;
            width: {width}%;
            background-color: #FFD0A0;
            margin: 0 auto;
            padding: 0 auto;
            text-align: left;
            }}\n""")
    cssLines.append(f""".header {{
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
            }}\n""")
    cssLines.append(f""".highlightedBlock {{
            background-color: {backgroundColor};
            border-radius: 8px;
            padding: 12px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            }}\n""")
    cssLines.append(f""".commentBlock {{
            background-color: #32631f;
            border-radius: 8px;
            padding: 12px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            }}\n""")
    cssLines.append(f""".orderedList
            background-color: #346792;
            border-radius: 8px;
            padding: 4px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            list-style-type: circle;
                    }}\n""")
    cssLines.append(f""".testBlock {{
            background-color: #2d1769;
            border-radius: 8px;
            padding: 12px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            }}\n""")
    cssLines.append(f""".standardText {{
            font-family: Arial, sans-serif;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            background-color: #FFD0A0;
            margin: 0 auto;
            padding: 0 auto;
            text-align: left;
            }}\n""")
    cssLines.append(f""".filename {{ 
            background-color: #f705af;
            display: block;
            width: fit-content;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 18px;
            font-weight: bold;
            margin: 10px auto;
            text-align: center;
            }}\n""")
    cssLines.append(f""".highlighted-text {{
            margin-top: 20px;
            }}\n""")
    cssLines.append(f""".copy-button {{
            display: block;
            margin-top: 10px;
            padding: 8px 16px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            }}\n""")
    cssLines.append(f""".copy-button:hover {{
            background-color: #555;
            }}\n""")
    cssLines.append(f""".tempclass {{
            background-color: {backgroundColor};
            border-radius: 8px;
            padding: 12px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            }}\n""")           

    return "".join(cssLines)

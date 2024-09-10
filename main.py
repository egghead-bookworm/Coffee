from guizero import App, Text, PushButton, TextBox
import wikipedia

def get_wiki_summary(query, sentences=5, words_per_line=8):
    """
    Search Wikipedia for a given query and return a summary of the most relevant article with a new line after every N words.
    
    Args:
        query (str): The search term to look up on Wikipedia.
        sentences (int, optional): The maximum number of sentences to include in the summary. Defaults to 5.
        words_per_line (int, optional): The number of words per line before adding a new line. Defaults to 8.
    
    Returns:
        str: A summary of the most relevant Wikipedia article for the given query with a new line after every N words.
    """
    try:
        # Retrieve the page for the given query
        page = wikipedia.page(query)
        
        # Split the summary into sentences
        summary_sentences = page.summary.split('. ')
        
        # Limit to the specified number of sentences
        selected_sentences = summary_sentences[:sentences]
        
        # Join sentences into one string
        full_summary = ' '.join(selected_sentences)
        
        # Break the summary into lines with a specific number of words
        words = full_summary.split()
        lines = []
        for i in range(0, len(words), words_per_line):
            line = ' '.join(words[i:i + words_per_line])
            lines.append(line)
        
        # Join lines with new line characters
        formatted_summary = '\n'.join(lines)
        
        return formatted_summary
    except wikipedia.exceptions.DisambiguationError as e:
        # If the query is ambiguous, return a summary for the first suggested page
        return get_wiki_summary(e.options[0], sentences, words_per_line)
    except wikipedia.exceptions.PageError:
        # If no matching page is found, return an empty string
        return "No results."
    except Exception as e:
        # Handle any other exceptions
        return "Error."

def change_message():
    
    message.value = get_wiki_summary(text_box.value)

app = App(title="Coffee")

text_box = TextBox(app, align="top", width="fill")
button = PushButton(app, text="Search", command=change_message, align="top")
message = Text(app, text="Search something")

app.display()

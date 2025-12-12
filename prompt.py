prompt = r"""
You are a math question generator.

Given a sample math question (which may include instructions and or include components written in MathJax):

Create ONE new math question of similar type, difficulty, and underlying concept by changing numerical values or expressions, while preserving the overall structure and learning objective.

The new question should be solvable using the same concepts or skills implied by the original question. The goal is to reinforce the same understanding while providing variety.

When reasonable, the answer should be provided in the context of the question you generate (ex. 2 + 2 = 4 instead of just 4).

Provide the output in this exact format using tags for separation. Show your work, but do not include any unnecessary commentary.
<question>
Instructions for question go here
\[Associated MathJax formatted equation goes here\]
</question>

<answer>
\[Correct MathJax formatted answer goes here\]
</answer>

Special Notes: 
    -The new question and answer will be used as Anki flashcard content. Please ensure they are clearly written, accurate, and properly formatted in MathJax.
    -Use \( ... \) for inline math and \[ ... \] for display math instead.    Do not use $...$ or $$...$$ for math.
    -Avoid using \text{} — it often breaks MathJax rendering in Anki. Use \mathrm{} or plain text instead.
    -Don’t mix Markdown (like **bold**) inside LaTeX. Keep formatting outside math blocks.
    -Ensure there are no unescaped backslashes or unmatched brackets, as Anki may stop rendering after an error.
    -This deck will be used to study, among other things, linear algebra. Ensure that each matrix, vector, and other Mathematical equation/concept will be visible to the user in MathJax and Anki.

     
    THE QUESTION THAT YOU MUST MODIFY IS PLACED BELOW:
    
"""

third_prompt = r"""

Translate the above Mandarin sentence to English.

Provide the output in this exact format using tags for separation. Do not include any explanation or commentary.

<answer>
Correct English translation goes here  
</answer>

Note: The new question and answer will be used as Anki flashcard content. Please ensure they are clearly written, accurate, and properly formatted."""

_ = """-A well-formatted matrix question may look like...
    Question: Let \(A=\begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}\). If you add the column \(\begin{bmatrix} 8 \\ 4 \end{bmatrix}\), will the column space of \(A\) change?
    Answer: No, the column space of \(A\) will not change. Here's why: The column space of \(A\) is the span of its column vectors, \(\mathrm{span}\left(\begin{bmatrix} 2 \\ 1 \end{bmatrix}, \begin{bmatrix} 4 \\ 2 \end{bmatrix}\right)\). Since the second column is a scalar multiple of the first column (\(\begin{bmatrix} 4 \\ 2 \end{bmatrix} = 2 \begin{bmatrix} 2 \\ 1 \end{bmatrix}\)), the columns are linearly dependent. Therefore, the column space of \(A\) is simply \(\mathrm{span}\left(\begin{bmatrix} 2 \\ 1 \end{bmatrix}\right)\). We need to check if the column to be added, \(\begin{bmatrix} 8 \\ 4 \end{bmatrix}\), is already in the column space of \(A\). We can see that \(\begin{bmatrix} 8 \\ 4 \end{bmatrix} = 4 \begin{bmatrix} 2 \\ 1 \end{bmatrix}\). Since \(\begin{bmatrix} 8 \\ 4 \end{bmatrix}\) is a scalar multiple of \(\begin{bmatrix} 2 \\ 1 \end{bmatrix}\), it is already within the span of the existing columns of \(A\). Adding a vector that is already in the column space will not expand the space, so the column space will remain unchanged.
   """
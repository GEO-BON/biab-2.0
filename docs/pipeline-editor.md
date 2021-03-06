# Pipeline editor

The pipeline editor allows you to create pipelines by plugging steps together.

The left pane shows the available steps, the right pane shows the canvas.

**To add a step:** drag and drop from the left pane to the canvas.

**To connect steps:** drag and drop from one output handle to an input handle. Input handles are on the left, and output handles are on the right.

**To add a constant value:** double-click on any input to add a constant value linked to this input.

**To delete a step or a pipe:** select it and press the Delete key on your keyboard.

**To make an array out of single value outputs:** if many outputs of the same type are connected to the same input, it will be received as an array by the script. 

<img src="https://user-images.githubusercontent.com/6223744/181106359-c4194411-5789-4e55-84d5-24b9e029398f.png" width="300">

A single value can also be combined with an array of the same type, to produce a single array.

<img src="https://user-images.githubusercontent.com/6223744/181106278-f6db6af5-764a-4775-b196-48feac940eec.png" width="300">



## Pipeline inputs and outputs
Any **input** with no constant value assigned will be considered a pipeline input and user will have to fill the value.

Drag and drop an **output** node and link it to a step output to specify that this output is an output of the pipeline. All other unmarked step outputs will still be available as intermediate results in the UI.
![image](https://user-images.githubusercontent.com/6223744/181108988-97d988ca-8f4b-45b1-b4a3-32e90821b68b.png)


## Saving and loading
The editor _does not_ allow you to edit files live on the server. Files need to be commit to the github repo using git.

To load an existing pipeline:
1. Make sure you are up to date using `git pull --rebase`.
2. Click "Load from file"
3. Browse to the file on your computer and open it.

To save your modifications:
1. Click save: the content is copied to your clipboard.
2. Make sure you are up to date using `git pull --rebase`.
3. Remove all the content of the target file.
4. Paste content and save.

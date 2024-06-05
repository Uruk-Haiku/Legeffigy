# Legeffigy
A project to make you out of LEGO. Pass in a picture of yourself (full body) and then it will tell you what pieces you need to make a minifigure out of yourself.

LEGO Company, please do not sue me! <3

### Plan
1. Intake user image - may upgrade to video later
2. Detect human body - segment into:
- Hair
- Head
- Torso
- Legs
3. Scan through a database of Lego parts pulled from the BrickLinks API for the best match.
4. Package & return results. 

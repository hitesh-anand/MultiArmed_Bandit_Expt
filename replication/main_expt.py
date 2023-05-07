#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on April 12, 2023, at 20:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_4
import random
urndlist=[]
uprize_lst=[]
urep_choices = 0
rep_choices = 0
uhistory = []
history = []
shift = random.randint(30, 60)
uavgrew = [[0,0],[0,0],[0,0],[0,0],[0,0]]
conditions = {
    "1" : "IOWA",
    "2" : "Equal Means",
    "3" : "Low Var",
    "4" : "High Var"
}
tot_uprize=0
tot_prize=0
avgrew = [[0,0],[0,0],[0,0],[0,0],[0,0]]
total=0
brk=0
cntbrk=0
for x in range(2):
    urndlist.append(1)
for x in range(3):
    urndlist.append(2)
for x in range(3):
    urndlist.append(3)
for x in range(3):
    urndlist.append(4)
random.shuffle(urndlist)
urndlist.append(1)
uprize_lst=[(-10,3.16),(-10,10),(10,3.16),(10,10)]
# Run 'Before Experiment' code from code_3
import random
rndlist=[]
prize_lst=[]
pos=0
neg=0
cross=0
for x in range(2):
    rndlist.append(1)
for x in range(3):
    rndlist.append(2)
for x in range(3):
    rndlist.append(3)
for x in range(3):
    rndlist.append(4)
random.shuffle(rndlist)
rndlist.append(1)
prize_lst=[(-10,3.16),(-10,10),(10,3.16),(10,10)]


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'bandit task'  # from the Builder filename that created this script
expInfo = {
    'Roll Number': '',
    'Name': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/try.csv'

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\anand\\Desktop\\Academics\\BSE662\\replication\\bandit\\untitled.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcomemessage_1" ---
uIntrotext = visual.TextStim(win=win, name='uIntrotext',
    text='Welcome!\n\nIn this part, you will have unlimited time to select an option (Q/W/O/P).\nEach option corresponds to a reward which will be shown to you afterwards.\n\nYour goal is to maximise your reward!\n\nPress Space to begin',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
uenter_resp = keyboard.Keyboard()
# Set experiment start values for variable component urndtype
urndtype = 1
urndtypeContainer = []

# --- Initialize components for Routine "utrial" ---
ukey_resp = keyboard.Keyboard()
# Set experiment start values for variable component uprize
uprize = 0
uprizeContainer = []
# Set experiment start values for variable component ucntrnd
ucntrnd = 0
ucntrndContainer = []
Q = visual.ImageStim(
    win=win,
    name='Q', 
    image='Q.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, 0.25), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
W = visual.ImageStim(
    win=win,
    name='W', 
    image='W.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.25, 0.255), size=(0.5,0.51),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
O = visual.ImageStim(
    win=win,
    name='O', 
    image='O.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.25), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
P = visual.ImageStim(
    win=win,
    name='P', 
    image='P.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.25, -0.26), size=(0.5,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# --- Initialize components for Routine "uresult" ---
smly = visual.ImageStim(
    win=win,
    name='smly', 
    image='Smiley.svg.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.15), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, -0.15), height=0.08, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "break1" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='You can rest for 30 sec before continue\nOR\nPress Space to Continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "Welcomemessage_2" ---
text = visual.TextStim(win=win, name='text',
    text='Welcome!\n\nIn this part, you will have limited time (0.4 s) to select an option (Q/W/O/P).\nEach option corresponds to a reward which will be shown to you afterwards. \nIncase you fail to select an option before the timer runs out, you will get NO reward.\n\nYour goal is to maximise your reward!\n\nPress Space to begin',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
enterresp = keyboard.Keyboard()
# Set experiment start values for variable component rndtype
rndtype = 1
rndtypeContainer = []

# --- Initialize components for Routine "trial" ---
Optionq = visual.TextStim(win=win, name='Optionq',
    text='Q',
    font='Open Sans',
    pos=(-0.25, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
optionw = visual.TextStim(win=win, name='optionw',
    text='W',
    font='Open Sans',
    pos=(0.25, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
optiono = visual.TextStim(win=win, name='optiono',
    text='O\n',
    font='Open Sans',
    pos=(-0.25, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Optionp = visual.TextStim(win=win, name='Optionp',
    text='P\n',
    font='Open Sans',
    pos=(0.25, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp = keyboard.Keyboard()
# Set experiment start values for variable component prize
prize = 0
prizeContainer = []
# Set experiment start values for variable component cntrnd
cntrnd = 0
cntrndContainer = []
Ql = visual.ImageStim(
    win=win,
    name='Ql', 
    image='Q.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
Wl = visual.ImageStim(
    win=win,
    name='Wl', 
    image='W.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.25, 0.255), size=(0.5, 0.51),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
Ol = visual.ImageStim(
    win=win,
    name='Ol', 
    image='O.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
Pl = visual.ImageStim(
    win=win,
    name='Pl', 
    image='P.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.25, -0.26), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)

# --- Initialize components for Routine "result" ---
sadl = visual.ImageStim(
    win=win,
    name='sadl', 
    image='sad.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.15), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
smlyl = visual.ImageStim(
    win=win,
    name='smlyl', 
    image='Smiley.svg.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.15), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, -0.15), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "break2" ---
text_9 = visual.TextStim(win=win, name='text_9',
    text='You can rest for 30 sec before continue\nOR\nPress Space to Continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "Thankyou" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcomemessage_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
uenter_resp.keys = []
uenter_resp.rt = []
_uenter_resp_allKeys = []
# keep track of which components have finished
Welcomemessage_1Components = [uIntrotext, uenter_resp]
for thisComponent in Welcomemessage_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcomemessage_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *uIntrotext* updates
    if uIntrotext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uIntrotext.frameNStart = frameN  # exact frame index
        uIntrotext.tStart = t  # local t and not account for scr refresh
        uIntrotext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uIntrotext, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'uIntrotext.started')
        uIntrotext.setAutoDraw(True)
    
    # *uenter_resp* updates
    waitOnFlip = False
    if uenter_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uenter_resp.frameNStart = frameN  # exact frame index
        uenter_resp.tStart = t  # local t and not account for scr refresh
        uenter_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uenter_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'uenter_resp.started')
        uenter_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(uenter_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(uenter_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if uenter_resp.status == STARTED and not waitOnFlip:
        theseKeys = uenter_resp.getKeys(keyList=['space'], waitRelease=False)
        _uenter_resp_allKeys.extend(theseKeys)
        if len(_uenter_resp_allKeys):
            uenter_resp.keys = _uenter_resp_allKeys[-1].name  # just the last key pressed
            uenter_resp.rt = _uenter_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcomemessage_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcomemessage_1" ---
for thisComponent in Welcomemessage_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if uenter_resp.keys in ['', [], None]:  # No response was made
    uenter_resp.keys = None
thisExp.addData('uenter_resp.keys',uenter_resp.keys)
if uenter_resp.keys != None:  # we had a response
    thisExp.addData('uenter_resp.rt', uenter_resp.rt)
thisExp.nextEntry()
# the Routine "Welcomemessage_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
utrials = data.TrialHandler(nReps=240.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='utrials')
thisExp.addLoop(utrials)  # add the loop to the experiment
thisUtrial = utrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisUtrial.rgb)
if thisUtrial != None:
    for paramName in thisUtrial:
        exec('{} = thisUtrial[paramName]'.format(paramName))

for thisUtrial in utrials:
    currentLoop = utrials
    # abbreviate parameter names if possible (e.g. rgb = thisUtrial.rgb)
    if thisUtrial != None:
        for paramName in thisUtrial:
            exec('{} = thisUtrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "utrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    ukey_resp.keys = []
    ukey_resp.rt = []
    _ukey_resp_allKeys = []
    # keep track of which components have finished
    utrialComponents = [ukey_resp, Q, W, O, P]
    for thisComponent in utrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "utrial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ukey_resp* updates
        waitOnFlip = False
        if ukey_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ukey_resp.frameNStart = frameN  # exact frame index
            ukey_resp.tStart = t  # local t and not account for scr refresh
            ukey_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ukey_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ukey_resp.started')
            ukey_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ukey_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ukey_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ukey_resp.status == STARTED and not waitOnFlip:
            theseKeys = ukey_resp.getKeys(keyList=['w','o','p','q'], waitRelease=False)
            _ukey_resp_allKeys.extend(theseKeys)
            if len(_ukey_resp_allKeys):
                ukey_resp.keys = _ukey_resp_allKeys[-1].name  # just the last key pressed
                ukey_resp.rt = _ukey_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Q* updates
        if Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q.frameNStart = frameN  # exact frame index
            Q.tStart = t  # local t and not account for scr refresh
            Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q.started')
            Q.setAutoDraw(True)
        
        # *W* updates
        if W.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            W.frameNStart = frameN  # exact frame index
            W.tStart = t  # local t and not account for scr refresh
            W.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(W, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'W.started')
            W.setAutoDraw(True)
        
        # *O* updates
        if O.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            O.frameNStart = frameN  # exact frame index
            O.tStart = t  # local t and not account for scr refresh
            O.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(O, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'O.started')
            O.setAutoDraw(True)
        
        # *P* updates
        if P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P.frameNStart = frameN  # exact frame index
            P.tStart = t  # local t and not account for scr refresh
            P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'P.started')
            P.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in utrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "utrial" ---
    for thisComponent in utrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ukey_resp.keys in ['', [], None]:  # No response was made
        ukey_resp.keys = None
    utrials.addData('ukey_resp.keys',ukey_resp.keys)
    if ukey_resp.keys != None:  # we had a response
        utrials.addData('ukey_resp.rt', ukey_resp.rt)
    # Run 'End Routine' code from code_5
    if ukey_resp.keys=='q':
        uprize=shift+random.gauss(uprize_lst[0][0],uprize_lst[0][1])
#        uprize+=30 + (random.random() * (30))
    elif ukey_resp.keys=='w':
        uprize=shift+random.gauss(uprize_lst[1][0],uprize_lst[1][1])
#        uprize+=30 + (random.random() * (30))
    elif ukey_resp.keys=='o':
        uprize=shift+random.gauss(uprize_lst[2][0],uprize_lst[2][1])
#        uprize+=30 + (random.random() * (30))
    elif ukey_resp.keys=='p':
        uprize=shift+random.gauss(uprize_lst[3][0],uprize_lst[3][1])
#        uprize+=30 + (random.random() * (30))
    else:
        uprize=0
        
    tot_uprize += uprize
    if len(uhistory)>0 and uhistory[-1]==ukey_resp.keys:
        urep_choices+=1
    uhistory.append(ukey_resp.keys)
    uprize=max(uprize,0)
    total=total+uprize
    
    
    # the Routine "utrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "uresult" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_3.setText('Won ' + str(round(uprize,0)) )
    # keep track of which components have finished
    uresultComponents = [smly, text_3]
    for thisComponent in uresultComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "uresult" ---
    while continueRoutine and routineTimer.getTime() < 0.4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *smly* updates
        if smly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smly.frameNStart = frameN  # exact frame index
            smly.tStart = t  # local t and not account for scr refresh
            smly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smly, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smly.started')
            smly.setAutoDraw(True)
        if smly.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smly.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                smly.tStop = t  # not accounting for scr refresh
                smly.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'smly.stopped')
                smly.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in uresultComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "uresult" ---
    for thisComponent in uresultComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_6
    
    
    if(ucntrnd%2==0):
        file = open('untimed_trialWise_data.csv', 'a')
        file.write(str(expInfo['Roll Number'])+", "+conditions[str(urndtype)]+", "+str(ucntrnd)+", "+str(tot_uprize)+", "+str(urep_choices)+"\n")
        file.close()
        
    if(ucntrnd==20):
        uavgrew[urndtype][0] += tot_uprize
        uavgrew[urndtype][1] += urep_choices
        tot_uprize = 0
        uhistory=[]
        urep_choices=0
        ucntrnd=0
        urndtype=urndlist.pop()
        if(urndtype==1):#IGT
            uprize_lst=[(-10,3.16), (-10,10), (10,3.16), (10,10)]
        if(urndtype==2):#equalmeans
            uprize_lst=[ (0,3.16), (0,6.32), (0,8.37), (0,3.16)]
        if(urndtype==3):#lowvar
            uprize_lst=[ (-10,3.16), (-0.3333,3.16), (0.3333,3.16), (10,3.16)]
        if(urndtype==4):#highvar
            uprize_lst=[ (-10,10), (-0.3333,10), (0.3333,10), (10,10)]
        random.shuffle(uprize_lst)
    else:
        ucntrnd+=1
    cntbrk+=1
    if(cntbrk==80):
        brk=1
        cntbrk=0
    else:
        brk=0
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.400000)
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=brk, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "break1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        break1Components = [text_8, key_resp_5]
        for thisComponent in break1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "break1" ---
        while continueRoutine and routineTimer.getTime() < 30.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.started')
                text_8.setAutoDraw(True)
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_8.stopped')
                    text_8.setAutoDraw(False)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_5.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_5.tStop = t  # not accounting for scr refresh
                    key_resp_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                    key_resp_5.status = FINISHED
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break1" ---
        for thisComponent in break1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials_2.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials_2.addData('key_resp_5.rt', key_resp_5.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-30.000000)
        thisExp.nextEntry()
        
    # completed brk repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 400.0 repeats of 'utrials'

file = open('untimed_overall_data.csv', 'a')
for ind, item in enumerate(uavgrew):
    if ind==0:
        continue
    item[0] = item[0]/60
    item[1] = item[1]/60
    file.write(expInfo['Roll Number']+", "+conditions[str(ind)]+", "+str(item[0])+", "+str(item[1])+"\n")
file.close()

# --- Prepare to start Routine "Welcomemessage_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
enterresp.keys = []
enterresp.rt = []
_enterresp_allKeys = []
# keep track of which components have finished
Welcomemessage_2Components = [text, enterresp]
for thisComponent in Welcomemessage_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcomemessage_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *enterresp* updates
    waitOnFlip = False
    if enterresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enterresp.frameNStart = frameN  # exact frame index
        enterresp.tStart = t  # local t and not account for scr refresh
        enterresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enterresp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'enterresp.started')
        enterresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enterresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enterresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enterresp.status == STARTED and not waitOnFlip:
        theseKeys = enterresp.getKeys(keyList=['space'], waitRelease=False)
        _enterresp_allKeys.extend(theseKeys)
        if len(_enterresp_allKeys):
            enterresp.keys = _enterresp_allKeys[-1].name  # just the last key pressed
            enterresp.rt = _enterresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcomemessage_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcomemessage_2" ---
for thisComponent in Welcomemessage_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if enterresp.keys in ['', [], None]:  # No response was made
    enterresp.keys = None
thisExp.addData('enterresp.keys',enterresp.keys)
if enterresp.keys != None:  # we had a response
    thisExp.addData('enterresp.rt', enterresp.rt)
thisExp.nextEntry()
# the Routine "Welcomemessage_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=240.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [Optionq, optionw, optiono, Optionp, key_resp, Ql, Wl, Ol, Pl]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Optionq* updates
        if Optionq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Optionq.frameNStart = frameN  # exact frame index
            Optionq.tStart = t  # local t and not account for scr refresh
            Optionq.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Optionq, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Optionq.started')
            Optionq.setAutoDraw(True)
        if Optionq.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Optionq.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Optionq.tStop = t  # not accounting for scr refresh
                Optionq.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Optionq.stopped')
                Optionq.setAutoDraw(False)
        
        # *optionw* updates
        if optionw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            optionw.frameNStart = frameN  # exact frame index
            optionw.tStart = t  # local t and not account for scr refresh
            optionw.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(optionw, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'optionw.started')
            optionw.setAutoDraw(True)
        if optionw.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > optionw.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                optionw.tStop = t  # not accounting for scr refresh
                optionw.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'optionw.stopped')
                optionw.setAutoDraw(False)
        
        # *optiono* updates
        if optiono.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            optiono.frameNStart = frameN  # exact frame index
            optiono.tStart = t  # local t and not account for scr refresh
            optiono.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(optiono, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'optiono.started')
            optiono.setAutoDraw(True)
        if optiono.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > optiono.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                optiono.tStop = t  # not accounting for scr refresh
                optiono.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'optiono.stopped')
                optiono.setAutoDraw(False)
        
        # *Optionp* updates
        if Optionp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Optionp.frameNStart = frameN  # exact frame index
            Optionp.tStart = t  # local t and not account for scr refresh
            Optionp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Optionp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Optionp.started')
            Optionp.setAutoDraw(True)
        if Optionp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Optionp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Optionp.tStop = t  # not accounting for scr refresh
                Optionp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Optionp.stopped')
                Optionp.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['q','w','o','p'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Ql* updates
        if Ql.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ql.frameNStart = frameN  # exact frame index
            Ql.tStart = t  # local t and not account for scr refresh
            Ql.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ql, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Ql.started')
            Ql.setAutoDraw(True)
        if Ql.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Ql.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Ql.tStop = t  # not accounting for scr refresh
                Ql.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ql.stopped')
                Ql.setAutoDraw(False)
        
        # *Wl* updates
        if Wl.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Wl.frameNStart = frameN  # exact frame index
            Wl.tStart = t  # local t and not account for scr refresh
            Wl.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Wl, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Wl.started')
            Wl.setAutoDraw(True)
        if Wl.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Wl.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Wl.tStop = t  # not accounting for scr refresh
                Wl.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Wl.stopped')
                Wl.setAutoDraw(False)
        
        # *Ol* updates
        if Ol.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ol.frameNStart = frameN  # exact frame index
            Ol.tStart = t  # local t and not account for scr refresh
            Ol.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ol, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Ol.started')
            Ol.setAutoDraw(True)
        if Ol.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Ol.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Ol.tStop = t  # not accounting for scr refresh
                Ol.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Ol.stopped')
                Ol.setAutoDraw(False)
        
        # *Pl* updates
        if Pl.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pl.frameNStart = frameN  # exact frame index
            Pl.tStart = t  # local t and not account for scr refresh
            Pl.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pl, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Pl.started')
            Pl.setAutoDraw(True)
        if Pl.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Pl.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Pl.tStop = t  # not accounting for scr refresh
                Pl.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Pl.stopped')
                Pl.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # Run 'End Routine' code from code
    if key_resp.keys=='q':
        prize=shift + random.gauss(prize_lst[0][0],prize_lst[0][1])
#        prize+=30 + (random.random() * (30))
        pos=0.4
        neg=0
        cross=0
    elif key_resp.keys=='w':
        prize=shift + random.gauss(prize_lst[1][0],prize_lst[1][1])
#        prize+=30 + (random.random() * (30))
        pos=0.4
        neg=0
        cross=0
    elif key_resp.keys=='o':
        prize=shift + random.gauss(prize_lst[2][0],prize_lst[2][1])
#        prize+=30 + (random.random() * (30))
        pos=0.4
        neg=0
        cross=0
    elif key_resp.keys=='p':
        prize=shift + random.gauss(prize_lst[3][0],prize_lst[3][1])
#        prize+=30 + (random.random() * (30))
        pos=0.4
        neg=0
        cross=0
    else:
        prize=0
        neg=0.4
        pos=0
        cross=1
        
    tot_prize += prize
    if len(history)>0 and history[-1]==key_resp.keys:
        rep_choices+=1
    history.append(key_resp.keys)
    prize=max(prize,0)
    total=total+prize
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "result" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_2.setText('Won ' + str(round(prize,0)))
    # keep track of which components have finished
    resultComponents = [sadl, smlyl, text_2]
    for thisComponent in resultComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "result" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sadl* updates
        if sadl.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sadl.frameNStart = frameN  # exact frame index
            sadl.tStart = t  # local t and not account for scr refresh
            sadl.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sadl, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sadl.started')
            sadl.setAutoDraw(True)
        if sadl.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sadl.tStartRefresh + neg-frameTolerance:
                # keep track of stop time/frame for later
                sadl.tStop = t  # not accounting for scr refresh
                sadl.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sadl.stopped')
                sadl.setAutoDraw(False)
        
        # *smlyl* updates
        if smlyl.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smlyl.frameNStart = frameN  # exact frame index
            smlyl.tStart = t  # local t and not account for scr refresh
            smlyl.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smlyl, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smlyl.started')
            smlyl.setAutoDraw(True)
        if smlyl.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smlyl.tStartRefresh + pos-frameTolerance:
                # keep track of stop time/frame for later
                smlyl.tStop = t  # not accounting for scr refresh
                smlyl.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'smlyl.stopped')
                smlyl.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resultComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "result" ---
    for thisComponent in resultComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    if(cntrnd%2==0):
        file = open('timed_trialWise_data.csv', 'a')
        file.write(str(expInfo['Roll Number'])+", "+conditions[str(rndtype)]+", "+str(cntrnd)+", "+str(tot_prize)+", "+str(rep_choices)+"\n")
        file.close()
        
    if(cntrnd==20):
        avgrew[rndtype][0] += tot_prize
        avgrew[rndtype][1] += rep_choices
        tot_prize = 0
        history=[]
        rep_choices=0
        cntrnd=0
        rndtype=rndlist.pop()
        brk=1
        if(rndtype==1):#IGT
            prize_lst=[(-10,3.16), (-10,10), (10,3.16), (10,10)]
        if(rndtype==2):#equalmeans
            prize_lst=[ (0,3.16), (0,6.32), (0,8.37), (0,10)]
        if(rndtype==3):#lowvar
            prize_lst=[ (-10,3.16), (-0.3333,3.16), (0.3333,3.16), (10,3.16)]
        if(rndtype==4):#highvar
            prize_lst=[ (-10,10), (-0.3333,10), (0.3333,10), (10,10)]
        random.shuffle(prize_lst)
    else:
        cntrnd+=1
        brk=0
    cntbrk+=1
    if(cntbrk==80):
        brk=1
        cntbrk=0
    else:
        brk=0
    # the Routine "result" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=brk, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "break2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        break2Components = [text_9, key_resp_4]
        for thisComponent in break2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "break2" ---
        while continueRoutine and routineTimer.getTime() < 30.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_9* updates
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.started')
                text_9.setAutoDraw(True)
            if text_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_9.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    text_9.tStop = t  # not accounting for scr refresh
                    text_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_9.stopped')
                    text_9.setAutoDraw(False)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_4.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_4.tStop = t  # not accounting for scr refresh
                    key_resp_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                    key_resp_4.status = FINISHED
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break2" ---
        for thisComponent in break2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials_3.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials_3.addData('key_resp_4.rt', key_resp_4.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-30.000000)
        thisExp.nextEntry()
        
    # completed brk repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed 400.0 repeats of 'trials'

file = open('timed_overall_data.csv', 'a')
for ind, item in enumerate(avgrew):
    if ind==0:
        continue
    item[0] = item[0]/60
    item[1] = item[1]/60
    file.write(expInfo['Roll Number']+", "+conditions[str(ind)]+", "+str(item[0])+", "+str(item[1])+"\n")
file.close()

# --- Prepare to start Routine "Thankyou" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_4.setText('Total Reward '+ str(round(total,0))+'\n\nThank You for participating!'
)
# keep track of which components have finished
ThankyouComponents = [text_4]
for thisComponent in ThankyouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Thankyou" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Thankyou" ---
for thisComponent in ThankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

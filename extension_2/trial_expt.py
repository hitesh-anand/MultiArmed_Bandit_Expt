#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on April 12, 2023, at 20:47
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

# Run 'Before Experiment' code from code_7
import random
newprize=0
isreq=1
tot=0
ftot=0
isinpreq=0
newrndlist=[]
newprize_lst=[]

rep_choices = 0
history = []
shift = random.randint(30, 60)
conditions = {
    "1" : "IOWA",
    "2" : "Equal Means",
    "3" : "Low Var",
    "4" : "High Var"
}
tot_prize=0
avgrew = [[0,0],[0,0],[0,0],[0,0],[0,0]]

for x in range(4):
    newrndlist.append(1)
for x in range(5):
    newrndlist.append(2)
for x in range(5):
    newrndlist.append(3)
for x in range(5):
    newrndlist.append(4)
newrndlist.append(1)
random.shuffle(newrndlist)
newprize_lst=[(-10,3.16),(-10,10),(10,3.16),(10,10)]


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
    originPath='C:\\Users\\anand\\Desktop\\Academics\\BSE662\\extension_2\\banditext2\\untitled.py',
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

# --- Initialize components for Routine "WelcommeMessage3" ---
newintrotext = visual.TextStim(win=win, name='newintrotext',
    text='Welcome!\n\nIn this part of the task you will have unlimited time to selected an option (Q/W/O/P) based on which you will earn a reward.\nBefore starting, a six digit number will be provided which will have to be recalled after 20 trials. \nYour rewards will then be scaled based on your accuracy in remembering the number.\n\nYour goal is to maximize your rewards.\n\nPress\xa0SPACE\xa0to\xa0begin',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
newintroresp = keyboard.Keyboard()
# Set experiment start values for variable component newrndtype
newrndtype = 1
newrndtypeContainer = []

# --- Initialize components for Routine "remember" ---
key_resp_2 = keyboard.Keyboard()
reme_t = visual.TextStim(win=win, name='reme_t',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
# Set experiment start values for variable component txt
txt = 0
txtContainer = []

# --- Initialize components for Routine "newTrial" ---
newkeyresp = keyboard.Keyboard()
# Set experiment start values for variable component newprize
newprize = 0
newprizeContainer = []
# Set experiment start values for variable component newcntrnd
newcntrnd = 0
newcntrndContainer = []
nQ = visual.ImageStim(
    win=win,
    name='nQ', 
    image='Q.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
nW = visual.ImageStim(
    win=win,
    name='nW', 
    image='W.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.25, 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
nO = visual.ImageStim(
    win=win,
    name='nO', 
    image='O.jpg', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
nP = visual.ImageStim(
    win=win,
    name='nP', 
    image='P.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# --- Initialize components for Routine "buff" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "resulttemp" ---
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "inpremem" ---
text_6 = visual.TextStim(win=win, name='text_6',
    text='Enter the number you remember \n&\nPress Space to Continue',
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0,-0.15),     letterHeight=0.05,
     size=(0.75, 0.15), borderWidth=2.0,
     color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=[0.6941, 0.4980, 0.6941], borderColor=[1.0000, 1.0000, 1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "showrew" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "newresult" ---

# --- Initialize components for Routine "Thankyou" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='Your Total reward is '+str(round(ftot,0))+'\n \n Thank You for participation'
,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "WelcommeMessage3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
newintroresp.keys = []
newintroresp.rt = []
_newintroresp_allKeys = []
# keep track of which components have finished
WelcommeMessage3Components = [newintrotext, newintroresp]
for thisComponent in WelcommeMessage3Components:
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

# --- Run Routine "WelcommeMessage3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *newintrotext* updates
    if newintrotext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        newintrotext.frameNStart = frameN  # exact frame index
        newintrotext.tStart = t  # local t and not account for scr refresh
        newintrotext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(newintrotext, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'newintrotext.started')
        newintrotext.setAutoDraw(True)
    
    # *newintroresp* updates
    waitOnFlip = False
    if newintroresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        newintroresp.frameNStart = frameN  # exact frame index
        newintroresp.tStart = t  # local t and not account for scr refresh
        newintroresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(newintroresp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'newintroresp.started')
        newintroresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(newintroresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(newintroresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if newintroresp.status == STARTED and not waitOnFlip:
        theseKeys = newintroresp.getKeys(keyList=['space'], waitRelease=False)
        _newintroresp_allKeys.extend(theseKeys)
        if len(_newintroresp_allKeys):
            newintroresp.keys = _newintroresp_allKeys[-1].name  # just the last key pressed
            newintroresp.rt = _newintroresp_allKeys[-1].rt
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
    for thisComponent in WelcommeMessage3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "WelcommeMessage3" ---
for thisComponent in WelcommeMessage3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if newintroresp.keys in ['', [], None]:  # No response was made
    newintroresp.keys = None
thisExp.addData('newintroresp.keys',newintroresp.keys)
if newintroresp.keys != None:  # we had a response
    thisExp.addData('newintroresp.rt', newintroresp.rt)
thisExp.nextEntry()
# the Routine "WelcommeMessage3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
newtrials = data.TrialHandler(nReps=40.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='newtrials')
thisExp.addLoop(newtrials)  # add the loop to the experiment
thisNewtrial = newtrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNewtrial.rgb)
if thisNewtrial != None:
    for paramName in thisNewtrial:
        exec('{} = thisNewtrial[paramName]'.format(paramName))

for thisNewtrial in newtrials:
    currentLoop = newtrials
    # abbreviate parameter names if possible (e.g. rgb = thisNewtrial.rgb)
    if thisNewtrial != None:
        for paramName in thisNewtrial:
            exec('{} = thisNewtrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=isreq, method='random', 
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
        
        # --- Prepare to start Routine "remember" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_10
        txt=""
        for i in range(6):
            r1 = random.randint(0, 9)
            txt=txt+str(r1)
        
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        reme_t.setText('Remember this: ' + str(txt) + '\n Press Space To continue')
        # keep track of which components have finished
        rememberComponents = [key_resp_2, reme_t]
        for thisComponent in rememberComponents:
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
        
        # --- Run Routine "remember" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *reme_t* updates
            if reme_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reme_t.frameNStart = frameN  # exact frame index
                reme_t.tStart = t  # local t and not account for scr refresh
                reme_t.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reme_t, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reme_t.started')
                reme_t.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rememberComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "remember" ---
        for thisComponent in rememberComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "remember" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed isreq repeats of 'trials'
    
    
    # --- Prepare to start Routine "newTrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    newkeyresp.keys = []
    newkeyresp.rt = []
    _newkeyresp_allKeys = []
    # keep track of which components have finished
    newTrialComponents = [newkeyresp, nQ, nW, nO, nP]
    for thisComponent in newTrialComponents:
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
    
    # --- Run Routine "newTrial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *newkeyresp* updates
        waitOnFlip = False
        if newkeyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            newkeyresp.frameNStart = frameN  # exact frame index
            newkeyresp.tStart = t  # local t and not account for scr refresh
            newkeyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(newkeyresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'newkeyresp.started')
            newkeyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(newkeyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(newkeyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if newkeyresp.status == STARTED and not waitOnFlip:
            theseKeys = newkeyresp.getKeys(keyList=['w','o','p','q'], waitRelease=False)
            _newkeyresp_allKeys.extend(theseKeys)
            if len(_newkeyresp_allKeys):
                newkeyresp.keys = _newkeyresp_allKeys[-1].name  # just the last key pressed
                newkeyresp.rt = _newkeyresp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *nQ* updates
        if nQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nQ.frameNStart = frameN  # exact frame index
            nQ.tStart = t  # local t and not account for scr refresh
            nQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nQ, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nQ.started')
            nQ.setAutoDraw(True)
        
        # *nW* updates
        if nW.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nW.frameNStart = frameN  # exact frame index
            nW.tStart = t  # local t and not account for scr refresh
            nW.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nW, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nW.started')
            nW.setAutoDraw(True)
        
        # *nO* updates
        if nO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nO.frameNStart = frameN  # exact frame index
            nO.tStart = t  # local t and not account for scr refresh
            nO.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nO, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nO.started')
            nO.setAutoDraw(True)
        
        # *nP* updates
        if nP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nP.frameNStart = frameN  # exact frame index
            nP.tStart = t  # local t and not account for scr refresh
            nP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nP, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nP.started')
            nP.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in newTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "newTrial" ---
    for thisComponent in newTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if newkeyresp.keys in ['', [], None]:  # No response was made
        newkeyresp.keys = None
    newtrials.addData('newkeyresp.keys',newkeyresp.keys)
    if newkeyresp.keys != None:  # we had a response
        newtrials.addData('newkeyresp.rt', newkeyresp.rt)
    # Run 'End Routine' code from code_8
    if newkeyresp.keys=='q':
        newprize=shift + random.gauss(newprize_lst[0][0],newprize_lst[0][1])
#        newprize+=30 + (random.random() * (30))
    elif newkeyresp.keys=='w':
        newprize=shift + random.gauss(newprize_lst[1][0],newprize_lst[1][1])
#        newprize+=30 + (random.random() * (30))
    elif newkeyresp.keys=='o':
        newprize=shift + random.gauss(newprize_lst[2][0],newprize_lst[2][1])
#        newprize+=30 + (random.random() * (30))
    elif newkeyresp.keys=='p':
        newrize=shift + random.gauss(newprize_lst[3][0],newprize_lst[3][1])
#        newprize+=30 + (random.random() * (30))
    else:
        newprize=0
    newprize=max(newprize,0)
    tot_prize += newprize
    
    if len(history)>0 and history[-1]==newkeyresp.keys:
        rep_choices+=1
    history.append(newkeyresp.keys)
    # the Routine "newTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "buff" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    buffComponents = [text_7]
    for thisComponent in buffComponents:
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
    
    # --- Run Routine "buff" ---
    while continueRoutine and routineTimer.getTime() < 0.01:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 0.01-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.stopped')
                text_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in buffComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "buff" ---
    for thisComponent in buffComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.010000)
    
    # --- Prepare to start Routine "resulttemp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text.setText('Won ' + str(round(newprize,0)))
    # keep track of which components have finished
    resulttempComponents = [text]
    for thisComponent in resulttempComponents:
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
    
    # --- Run Routine "resulttemp" ---
    while continueRoutine and routineTimer.getTime() < 0.4:
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
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resulttempComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "resulttemp" ---
    for thisComponent in resulttempComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    tot=tot+newprize
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.400000)
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=isinpreq, method='random', 
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
        
        # --- Prepare to start Routine "inpremem" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_12
        textbox.text=""
        textbox.reset()
        textbox.setText('')
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        inprememComponents = [text_6, textbox, key_resp_3]
        for thisComponent in inprememComponents:
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
        
        # --- Run Routine "inpremem" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                text_6.setAutoDraw(True)
            
            # *textbox* updates
            if textbox.status == NOT_STARTED and tThisFlip >= 00-frameTolerance:
                # keep track of start time/frame for later
                textbox.frameNStart = frameN  # exact frame index
                textbox.tStart = t  # local t and not account for scr refresh
                textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.started')
                textbox.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
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
            for thisComponent in inprememComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "inpremem" ---
        for thisComponent in inprememComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('textbox.text',textbox.text)
        # Run 'End Routine' code from code_11
        inp=textbox.text
        r=0
        for i in range(6):
            if(i>=len(inp)):
                break
            if(inp[i]!=txt[i]):
                continue
            else:
                r=r+1
        tot=tot*(r/10)
        ftot+=tot
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials_2.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_2.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "inpremem" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "showrew" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        text_2.setText('Your total reward based on your performance till now is: ' + str(round(tot))  )
        # keep track of which components have finished
        showrewComponents = [text_2]
        for thisComponent in showrewComponents:
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
        
        # --- Run Routine "showrew" ---
        while continueRoutine and routineTimer.getTime() < 0.4:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            for thisComponent in showrewComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "showrew" ---
        for thisComponent in showrewComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        tot=0
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.400000)
        thisExp.nextEntry()
        
    # completed isinpreq repeats of 'trials_2'
    
    
    # --- Prepare to start Routine "newresult" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    newresultComponents = []
    for thisComponent in newresultComponents:
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
    
    # --- Run Routine "newresult" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in newresultComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "newresult" ---
    for thisComponent in newresultComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_9
    
    if(newcntrnd%2==0):
        file = open('trialWise_data.csv', 'a')
        file.write(str(expInfo['Roll Number'])+", "+conditions[str(newrndtype)]+", "+str(newcntrnd)+", "+str(tot_prize)+", "+str(rep_choices)+"\n")
        file.close()
        
    if(newcntrnd==5):
        avgrew[newrndtype][0] += tot_prize
        avgrew[newrndtype][1] += rep_choices
        tot_prize = 0
        history=[]
        rep_choices=0
        newcntrnd=0
        newrnd=newrndlist.pop()
        if(newcntrnd==1):#IGT
            newprize_lst=[(-10,3.16), (-10,10), (10,3.16), (10,10)]
        if(newcntrnd==2):#equalmeans
            newprize_lst=[ (0,3.16), (0,6.32), (0,8.37), (0,10)]
        if(newcntrnd==3):#lowvar
            newprize_lst=[ (-10,3.16), (-0.3333,3.16), (0.3333,3.16), (10,3.16)]
        if(newcntrnd==4):#highvar
            newprize_lst=[ (-10,10), (-0.3333,10), (0.3333,10), (10,10)]
        random.shuffle(newprize_lst)
        isinpreq=0
        isreq=1
    else:
        if(newcntrnd==19):
            isinpreq=1
            isreq=0
        else:
            isinpreq=0
            isreq=0
        newcntrnd+=1
        
    # the Routine "newresult" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 400.0 repeats of 'newtrials'

file = open('overall_data.csv', 'a')
for ind, item in enumerate(avgrew):
    if ind==0:
        continue
    item[0] = item[0]/100
    item[1] = item[1]/100
    file.write(expInfo['Roll Number']+", "+conditions[str(ind)]+", "+str(item[0])+", "+str(item[1])+"\n")
file.close()

# --- Prepare to start Routine "Thankyou" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
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

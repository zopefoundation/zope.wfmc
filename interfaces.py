##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Workflow-integration interfaces

$Id$
"""

import zope.interface

class IProcessDefinition(zope.interface.Interface):
    """Process definition
    """

    id = zope.interface.Attribute("Process-definition identifier")

    def defineActivities(**activities):
        """Add activity definitions to the collection of defined activities

        Activity definitions are supplied as keyword arguments.  The
        keywords provide activity identifiers.  The values are
        IActivityDefinition objects.
        
        """

    def defineTransitions(*transitions):
        """Add transition definitions

        The transitions are ITransition objects.
        """

    def defineParticipants(**participants):
        """Declare participants

        The participants are provided as keyword arguments.
        Participant identifiers are supplied as the keywords and the
        definitions are supplied as values.  The definitions are
        IParticipantDefinition objects.
        """

    def defineApplications(**applications):
        """Declare applications

        The applications are provided as keyword arguments.
        Application identifiers are supplied as the keywords and the
        definitions are supplied as values.  The definitions are
        IApplicationDefinition objects.
        """

    def defineParameters(*parameters):
        """Declate process parameters

        Input parameters are set as workflow-relevent data.  Output
        parameters are passed from workflow-relevant data to the
        processFinished method of process-instances process contexts.
        
        """

class IActivityDefinition(zope.interface.Interface):
    """Activity definition
    """

    id = zope.interface.Attribute("Activity identifier")

    def addApplication(id, *parameters):
        """Declare that the activity uses the identified activity

        The application identifier must match an application declared
        for the process.  

        Parameter definitions can be given as positional arguments.
        The parameter definition directions must match those given in
        the application definition.
        """

    def definePerformer(performer):
        """Set the activity performer

        The argument must be the identifier of a participant defined
        for the enclosing process.
        """

    def setAndSplit(setting):
        """Provide an and-split setting

        If the setting is true, then the activity will use an "and" split.
        """

    def setAndJoin(setting):
        """Provide an and-join setting

        If the setting is true, then the activity will use an "and" join.
        """

class ITransitionDefinition(zope.interface.Interface):
    """Activity definition
    """

class IProcess(zope.interface.Interface):
    """Process instance
    """

    definition = zope.interface.Attribute("Process definition")

    workflowRelevantData = zope.interface.Attribute(
        """Workflow-relevant data

        Object with attributes containing data used in conditions and
        to pass data as parameters between applications
        """
        )

    applicationRelevantData = zope.interface.Attribute(
        """Application-relevant data

        Object with attributes containing data used to pass data as
        shared data for applications
        
        """
        )

class IProcessContext(zope.interface.Interface):
    """Object that can recieve process results.
    """

    def processFinished(process, *results):
        """Recieve notification of process completion, with results
        """

class IActivity(zope.interface.Interface):
    """Activity instance
    """

    id = zope.interface.Attribute(
        """Activity identifier

        This identifier is set by the process instance

        """)

    definition = zope.interface.Attribute("Activity definition")

    def workItemFinished(work_item, *results):
        """Notify the activity that the work item has been completed.
        """

class IApplicationDefinition(zope.interface.Interface):
    """Application definition
    """

    parameters = zope.interface.Attribute(
        "A sequence of parameter definitions")

class IParameterDefinition(zope.interface.Interface):
    """Parameter definition
    """

    name = zope.interface.Attribute("Parameter name")

    input = zope.interface.Attribute("Is this an input parameter?")

    output = zope.interface.Attribute("Is this an output parameter?")

class IParticipantDefinition(zope.interface.Interface):
    """Participant definition
    """

class IParticipant(zope.interface.Interface):
    """Workflow participant
    """

class IWorkItem(zope.interface.Interface):
    """Work items
    """

    id = zope.interface.Attribute(
        """Item identifier

        This identifier is set by the activity instance

        """)
 
    def start(*arguments):
        """Start the work
        """

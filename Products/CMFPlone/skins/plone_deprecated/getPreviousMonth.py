## Script (Python) "getPreviousMonth"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=month, year
##title=Calendar Presentation Helper
##
context.plone_log("The getPreviousMonth script is deprecated and will be "
                  "removed in Plone 4.0. Use the getPreviousMonth method "
                  "of the @@calendar_view view instead.")

return context.restrictedTraverse('@@calendar_view').getPreviousMonth(month, year)
import xbmc
import sys
import globalvar
import uuid
import urllib,urllib2

def logEvent(category,action,screen):
  cid = str(uuid.uuid1())
  cid=cid[cid.rfind('-')+1:]   
  tid='UA-62192019-1'
  av=xbmc.getInfoLabel( "System.BuildVersion" )
  av=av[:av.find(' ')]
  an='kodi_' + av
  av=globalvar.ADDON.getAddonInfo('name') + globalvar.ADDON.getAddonInfo('version')
  if screen is None:
    cd='ChannelHome'
  else:
    cd=urllib.quote(screen)
    #cd='Les_aventures_de_les_anges'
    
  if category is None:  
    category='Start'  
    
  if action is None:  
    action='Start'
  
  if globalvar.LOGLEVEL==1:
    print 'OS=' + sys.platform
    print 'Build=' + xbmc.getInfoLabel( "System.BuildVersion" )
    print 'Internet' + xbmc.getInfoLabel( "System.InternetState" )
    print 'Session Id=' + cid
  
  if globalvar.LOGLEVEL<=2:
    print 'Addon=' + globalvar.ADDON.getAddonInfo('name') + ' ' + globalvar.ADDON.getAddonInfo('version')
    print 'Addon Path=' + globalvar.ADDON.getAddonInfo('path')
  
  url = 'http://www.google-analytics.com/collect'
  
  #Google Analytics - Screen
  values = {'v' : '1',
          'tid' : tid,
          'cid' : cid,
          't' : 'screenview',
          'an' : an,
          'av' : av,
          'cd' : cd}
  
  data = urllib.urlencode(values)
  req = urllib2.Request(url, data)
  response = urllib2.urlopen(req)  
  
  #Google Analytics - Event
  values = {'v' : '1',
          'tid' : tid,
          'cid' : cid,
          't' : 'event',
          'ec' : category,
          'ea' : action,
          'cd' : cd}
  
  data = urllib.urlencode(values)
  req = urllib2.Request(url, data)
  response = urllib2.urlopen(req)

from java.io import FileInputStream


def exportJMSModule(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      modTarget = module.getTargets()
      serverTarget = ''
	  
      for target in modTarget:
        serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

      print('# exporting JMS Module: ' + modName )
      print('# exporting target: ' + str(serverTarget) )
      print('\n')

      if str(modName) == 'None':
        modName = ''
      elif str(serverTarget) == 'None':
        serverTarget = ''
		
      exp = 'module,' + str(modName) + ',' + str(serverTarget) +'\n'
      file.write(exp)
	  
def exportSubdeployment(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      subdeploy = module.getSubDeployments()
   
      if str(modName) == 'None':
        modName = ''
   
      for sub in subdeploy:
        subName = sub.getName()
        subTarget = sub.getTargets()
        serverTarget = ''

        for target in subTarget:
          serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

        if str(subName) == 'None':
          subName = '' 
        elif str(serverTarget) == 'None':
          serverTarget = ''		

        print('# exporting JMS Module: ' + modName )
        print('# exporting Subdeployemt: ' + str(subName) )
        print('# exporting Target: ' + str(serverTarget) )
        print('\n')
		
        exp = 'subdeployment,' + str(modName) + ',' + str(subName) + ',' + str(serverTarget) +'\n'
        file.write(exp)


def exportForeignServer(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getForeignServers()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        foreignName = resource.getName()
        jndiInitConnFac = resource.getInitialContextFactory()
        jndiConUrl = resource.getConnectionURL()
        
        if str(foreignName) == 'None':
          foreignName == ''
        elif str(jndiInitConnFac) == 'None':
          jndiInitConnFac == ''
        elif str(jndiConUrl) == 'None':
          jndiConUrl == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Foreign Server: ' + str(foreignName) )
        print('# exporting JNDI Init Connection Factory: ' + str(jndiInitConnFac) )
        print('# exporting JNDI Connection URL: ' + str(jndiConUrl) )
        print('\n')
		
        exp = 'foreign,' + str(modName) + ',' + str(foreignName) + ',' + str(jndiInitConnFac) + ',' + str(jndiConUrl) + '\n'
        file.write(exp)
      


def exportQueue(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getQueues()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        name = resource.getName()
        jndi = resource.getJNDIName()
        subdeployment = resource.getSubDeploymentName()
        
        if str(name) == 'None':
          name == ''
        elif str(jndi) == 'None':
          jndi == ''
        elif str(subdeployment) == 'None' or str(subdeployment) == str(name):
          subdeployment == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Queue: ' + str(name) )
        print('# exporting JNDI Queue: ' + str(jndi) )
        print('# exporting Subdeployemt: ' + str(subdeployment) )
        print('\n')
		
        exp = 'queue,' + str(modName) + ',' + str(name) + ',' + str(jndi) + ',' + str(subdeployment) + '\n'
        file.write(exp)
      

def exportDistQueueUniform(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getUniformDistributedQueues()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        name = resource.getName()
        jndi = resource.getJNDIName()
        subdeployment = resource.getSubDeploymentName()
        
        if str(name) == 'None':
          name == ''
        elif str(jndi) == 'None':
          jndi == ''
        elif str(subdeployment) == 'None' or str(subdeployment) == str(name):
          subdeployment == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Dist. Queue Uniform: ' + str(name) )
        print('# exporting JNDI Dist. Queue: ' + str(jndi) )
        print('# exporting Subdeployemt: ' + str(subdeployment) )
        print('\n')
		
        exp = 'distqueueuniform,' + str(modName) + ',' + str(name) + ',' + str(jndi) + ',' + str(subdeployment) + '\n'
        file.write(exp)
		


def exportDistQueueWeighted(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getDistributedQueues()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        name = resource.getName()
        jndi = resource.getJNDIName()
        allMember = resource.getDistributedQueueMembers()
        members = ''		
		
        for member in allMember:
          members = members + member.getName() + '|'
        
        if str(name) == 'None':
          name == ''
        elif str(jndi) == 'None':
          jndi == ''
        elif str(members) == 'None':
          members == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Dist. Queue Uniform: ' + str(name) )
        print('# exporting JNDI Dist. Queue: ' + str(jndi) )
        print('# exporting Queue Members: ' + str(members) )
        print('\n')
		
        exp = 'distqueueweighted,' + str(modName) + ',' + str(name) + ',' + str(jndi) + ',' + str(members) + '\n'
        file.write(exp)
		

def exportTopic(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getTopics()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        name = resource.getName()
        jndi = resource.getJNDIName()
        subdeployment = resource.getSubDeploymentName()
        
        if str(name) == 'None':
          name == ''
        elif str(jndi) == 'None':
          jndi == ''
        elif str(subdeployment) == 'None' or str(subdeployment) == str(name):
          subdeployment == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Topic: ' + str(name) )
        print('# exporting JNDI Topic: ' + str(jndi) )
        print('# exporting Subdeployemt: ' + str(subdeployment) )
        print('\n')
		
        exp = 'topic,' + str(modName) + ',' + str(name) + ',' + str(jndi) + ',' + str(subdeployment) + '\n'
        file.write(exp)
      
      
def exportDistTopicUniform(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getUniformDistributedTopics()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        name = resource.getName()
        jndi = resource.getJNDIName()
        subdeployment = resource.getSubDeploymentName()
        
        if str(name) == 'None':
          name == ''
        elif str(jndi) == 'None':
          jndi == ''
        elif str(subdeployment) == 'None' or str(subdeployment) == str(name):
          subdeployment == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Dist. Topic Uniform: ' + str(name) )
        print('# exporting JNDI Dist. Topic: ' + str(jndi) )
        print('# exporting Subdeployemt: ' + str(subdeployment) )
        print('\n')
		
        exp = 'disttopicuniform,' + str(modName) + ',' + str(name) + ',' + str(jndi) + ',' + str(subdeployment) + '\n'
        file.write(exp)
		

def exportDistTopicWeighted(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getDistributedTopics()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        name = resource.getName()
        jndi = resource.getJNDIName()
        allMember = resource.getDistributedTopicMembers()
        members = ''		
		
        for member in allMember:
          members = members + member.getName() + '|'
        
        if str(name) == 'None':
          name == ''
        elif str(jndi) == 'None':
          jndi == ''
        elif str(members) == 'None':
          members == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Dist. Queue Uniform: ' + str(name) )
        print('# exporting JNDI Dist. Queue: ' + str(jndi) )
        print('# exporting Queue Members: ' + str(members) )
        print('\n')
		
        exp = 'disttopicweighted,' + str(modName) + ',' + str(name) + ',' + str(jndi) + ',' + str(members) + '\n'
        file.write(exp)
		

      
def exportConnectionFactory(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getConnectionFactories()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        name = resource.getName()
        jndi = resource.getJNDIName()
        subdeployment = resource.getSubDeploymentName()
		
        cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName + '/ConnectionFactories/' + name + '/SecurityParams/' + name)
        AttachJMSXUserId = get('AttachJMSXUserId')

        cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName + '/ConnectionFactories/' + name + '/ClientParams/' + name)
        ClientIdPolicy = get('ClientIdPolicy')
        SubscriptionSharingPolicy = get('SubscriptionSharingPolicy')
        MessagesMaximum = get('MessagesMaximum')
		
        cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName + '/ConnectionFactories/' + name + '/TransactionParams/' + name)
        XAConnectionFactoryEnabled = get('XAConnectionFactoryEnabled')
        
        if str(name) == 'None':
          name == ''
        elif str(jndi) == 'None':
          jndi == ''
        elif str(subdeployment) == 'None' or str(subdeployment) == str(name):
          subdeployment == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Connection Factory: ' + str(name) )
        print('# exporting JNDI Conn. Factory: ' + str(jndi) )
        print('# exporting AttachJMSXUserId: ' + str(AttachJMSXUserId) )
        print('# exporting ClientIdPolicy: ' + str(ClientIdPolicy) )
        print('# exporting SubscriptionSharingPolicy: ' + str(SubscriptionSharingPolicy) )
        print('# exporting MessagesMaximum: ' + str(MessagesMaximum) )
        print('# exporting XAConnectionFactoryEnabled: ' + str(XAConnectionFactoryEnabled) )
        print('# exporting Subdeployemt: ' + str(subdeployment) )
        print('\n')
		
        exp = 'factory,' + str(modName) + ',' + str(name) + ',' + str(jndi) + ',' + str(AttachJMSXUserId) + ',' + str(ClientIdPolicy) + ',' + str(SubscriptionSharingPolicy) + ',' + str(MessagesMaximum) + ',' + str(XAConnectionFactoryEnabled) + ',' + str(subdeployment) + '\n'
        file.write(exp)		


def exportForeignDestination(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getForeignServers()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        foreignName = resource.getName()
        destination = resource.getForeignDestinations()
		
        if str(foreignName) == 'None':
          foreignName == ''		
		
        for dest in destination:
          destName = dest.getName() 
          
          cd('/JMSSystemResources/' + modName + '/JMSResource/' + modName + '/ForeignServers/' + foreignName + '/ForeignDestinations/' + destName)
		
          LocalJNDIName = get('LocalJNDIName')
          RemoteJNDIName = get('RemoteJNDIName')
       		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Foreign Server: ' + str(foreignName) )
        print('# exporting Foreign Destination Name: ' + str(destName) )
        print('# exporting Local JNDI Name: ' + str(LocalJNDIName) )
        print('# exporting Remote JNDI Name: ' + str(RemoteJNDIName) )
        print('\n')
		
        exp = 'dest,' + str(modName) + ',' + str(foreignName) + ',' + str(destName) + ',' + str(LocalJNDIName) + ',' + str(RemoteJNDIName) + '\n'
        file.write(exp)
      

def exportForeignConnFact(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getForeignServers()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        foreignName = resource.getName()
        destination = resource.getForeignConnectionFactories()
		
        if str(foreignName) == 'None':
          foreignName == ''		
		
        for dest in destination:
          destName = dest.getName() 
          
          cd('/JMSSystemResources/' + modName + '/JMSResource/' + modName + '/ForeignServers/' + foreignName + '/ForeignConnectionFactories/' + destName)
		
          LocalJNDIName = get('LocalJNDIName')
          RemoteJNDIName = get('RemoteJNDIName')
       		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Foreign Server: ' + str(foreignName) )
        print('# exporting Foreign Connection Factory Name: ' + str(destName) )
        print('# exporting Local JNDI Name: ' + str(LocalJNDIName) )
        print('# exporting Remote JNDI Name: ' + str(RemoteJNDIName) )
        print('\n')
		
        exp = 'conn,' + str(modName) + ',' + str(foreignName) + ',' + str(destName) + ',' + str(LocalJNDIName) + ',' + str(RemoteJNDIName) + '\n'
        file.write(exp)
      


def exportQuota(file):
    cd('/')
    #redirect('/dev/null','false')
    jmsModules = cmo.getJMSSystemResources()

    for module in jmsModules:
      modName = module.getName()
      cd('/JMSSystemResources/'+ modName +'/JMSResource/' + modName)
      jmsResource = cmo.getQuotas()
   
      if str(modName) == 'None':
        modName = ''

      for resource in jmsResource:
        name = resource.getName()
        BytesMaximum = resource.getBytesMaximum()
        MessagesMaximum = resource.getMessagesMaximum()
        Policy = resource.getPolicy()
        Shared = resource.isShared()

        if str(name) == 'None':
          name == ''
		  
        print('# exporting JMS Module: ' + modName )
        print('# exporting Quota: ' + str(name) )
        print('# exporting Bytes Maximum: ' + str(BytesMaximum) )
        print('# exporting Messages Maximum: ' + str(MessagesMaximum) )
        print('# exporting Policy: ' + str(Policy) )
        print('# exporting Shared: ' + str(Shared) )
        print('\n')
		
        exp = 'quota,' + str(modName) + ',' + str(name) + ',' + str(BytesMaximum) + ',' + str(MessagesMaximum) + ',' + str(Policy) + ',' + str(Shared) + '\n'
        file.write(exp)
      

		
def main():
    propInputStream = FileInputStream(sys.argv[1])
    configProps = Properties()
    configProps.load(propInputStream)

    url=configProps.get("adminUrl")
    username = configProps.get("importUser")
    password = configProps.get("importPassword")
    csvLoc = configProps.get("csvLoc")

    connect(username,password,url)
	
    file=open(csvLoc, 'a+')

    print('======= Export JMS Module =======\n')	
    exportJMSModule(file)        
    print('------- End of Export JMS Module -------\n')
	
    print('======= Export JMS Module Subdeployment =======\n')
    exportSubdeployment(file)
    print('------- End of Export JMS Module Subdeployment  -------\n')
	
    print('======= Export Foreign Server =======\n')
    exportForeignServer(file)
    print('------- End of Export Foreign Server  -------\n')

    print('======= Export Queue =======\n')
    exportQueue(file)
    print('------- End of Export Queue  -------\n')
	
    print('======= Export Dist. Queue Uniform =======\n')
    exportDistQueueUniform(file)
    print('------- End of Export Dist. Queue Uniform  -------\n')	
	
    print('======= Export Dist. Queue Weighted =======\n')
    exportDistQueueWeighted(file)
    print('------- End of Export Dist. Queue Weighted  -------\n')

    print('======= Export Topic =======\n')
    exportTopic(file)
    print('------- End of Export Topic  -------\n')
	
    print('======= Export Dist. Topic Uniform =======\n')
    exportDistTopicUniform(file)
    print('------- End of Export Dist. Topic Uniform  -------\n')	
	
    print('======= Export Dist. Topic Weighted =======\n')
    exportDistTopicWeighted(file)
    print('------- End of Export Dist. Topic Weighted  -------\n')	
	
    print('======= Export Connection Factory =======\n')
    exportConnectionFactory(file)
    print('------- End of Export Connection Factory  -------\n')	

    print('======= Export Foreign Destination =======\n')
    exportForeignDestination(file)
    print('------- End of Export Foreign Destination  -------\n')

    print('======= Export Foreign Connection Factory =======\n')
    exportForeignConnFact(file)
    print('------- End of Export Foreign Connection Factory  -------\n')

    print('======= Export Quotas =======\n')
    exportQuota(file)
    print('------- End of Export Quotas  -------\n')

    disconnect()

main()

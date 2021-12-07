import jimi

class _sample(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        jimi.model.registerModel("sampleAction","_sampleAction","_action","plugins.sample.models.action")
        return True

    def uninstall(self):
        jimi.model.deregisterModel("sampleAction","_sampleAction","_action","plugins.sample.models.action")
        return True

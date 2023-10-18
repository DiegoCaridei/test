var targetModule= 'JbDetection2'
    var addr=ptr(0x04a8c);
    var moduleBase=Module.getBaseAddress(targetModule);
    var targetAddress=moduleBase.add(addr);
    Interceptor.attach(targetAddress,{
        onEnter:function(args){
            console.log("JbDetection2.ViewController.inTheDirectory() ")
        },
        onLeave(retval){
            console.log("onLeave")
 
            return retval.replace(0x0)
        }
    });
    
//backgroundColor
var check = Module.getExportByName(null, "$s12JbDetection214ViewControllerC15backgroundColorSbyF")
    Interceptor.attach(check,{
        onEnter(){
            console.log("JbDetection2.ViewController.backgroundColor()")
        },
        onLeave(retVal) {
            console.log("backgroundColor")
          
            return retVal.replace(0x0)
        }
    })

    var check = Module.getExportByName(null, "$s12JbDetection211InterfaceUIV06updateD0SbyF")
    Interceptor.attach(check,{
 
        onLeave(retVal) {
          
            return retVal.replace(0x0)
        }
    })

/**
* JetBrains Space Automation
* This Kotlin-script file lets you automate build activities
* For more info, see https://www.jetbrains.com/help/space/automation.html
*/

job("Hello World!") {
    startOn {
        gitPush {
            // run only if there's a release tag
            // e.g., release/v1.0.0
            tagFilter {
                +"release/*"
            }
        }
    }
    git("slack_bocker_builder")
    container(displayName = "Say Hello", image = "ubuntu:20.04")
    {
    	shellScript {
        	content = """
            	printenv
                ls -a
            """
        }
    }
}

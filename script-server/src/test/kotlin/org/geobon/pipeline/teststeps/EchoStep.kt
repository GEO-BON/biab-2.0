package org.geobon.pipeline.teststeps

import org.geobon.pipeline.ConstantPipe
import org.geobon.pipeline.Output
import org.geobon.pipeline.Pipe
import org.geobon.pipeline.Step

/**
 * Dummy test step:
 * - Transfers param sound to output KEY.
 * - Output BAD_KEY will stay null.
 */
class EchoStep(inputs: MutableMap<String, Pipe> = mutableMapOf()) :
    Step(
        inputs,
        mapOf(
            ECHO to Output("text/plain"),
            NO_ECHO to Output("text/plain")
        )
    ) {

    constructor(sound: String) :
            this(mutableMapOf(SOUND to ConstantPipe("text/plain", sound)))

    companion object {
        const val ECHO = "echo"
        const val NO_ECHO = "no-echo"

        const val SOUND = "sound"
    }

    var executeCount = 0

    override suspend fun execute(resolvedInputs: Map<String, Any>): Map<String, Any> {
        executeCount++
        return mapOf(ECHO to resolvedInputs[SOUND]!!)
    }
}
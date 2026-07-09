export default function AssistantMessages({
    aiResponse,
    loading,
}) {

    if (loading) {
        return (
            <div className="flex-1 p-4">
                🤖 AI is thinking...
            </div>
        );
    }

    if (!aiResponse) {
        return (
            <div className="flex-1 overflow-y-auto py-4">

                <div className="rounded-lg border border-blue-200 bg-blue-50 p-3 text-sm">

                    👋 Hi! I'm your AI CRM Assistant.

                    <br /><br />

                    You can simply chat with me.

                    <br /><br />

                    Examples:

                    <ul className="list-disc ml-5 mt-2 space-y-1">
                        <li>I met Dr. Smith yesterday at 8 PM...</li>
                        <li>Change the meeting time to 7 PM.</li>
                        <li>Summarize the interaction.</li>
                        <li>Generate medical insights.</li>
                        <li>Recommend follow-up actions.</li>
                        <li>Log this interaction.</li>
                    </ul>

                </div>

            </div>
        );
    }

    return (

        <div className="space-y-5 overflow-y-auto py-4">

            {aiResponse.message && (

                <div className="rounded-lg bg-blue-50 p-3 border border-blue-200">

                    <p className="text-sm whitespace-pre-wrap">

                        🤖 {aiResponse.message}

                    </p>

                </div>

            )}

            {aiResponse.summary && (

                <div>

                    <h3 className="font-semibold">
                        Summary
                    </h3>

                    <p className="text-sm whitespace-pre-wrap">
                        {aiResponse.summary}
                    </p>

                </div>

            )}

            {aiResponse.medical_insights && (

                <div>

                    <h3 className="font-semibold">
                        Medical Insights
                    </h3>

                    <p className="text-sm whitespace-pre-wrap">
                        {aiResponse.medical_insights}
                    </p>

                </div>

            )}

            {aiResponse.recommendations && (

                <div>

                    <h3 className="font-semibold">
                        Recommendations
                    </h3>

                    <p className="text-sm whitespace-pre-wrap">
                        {aiResponse.recommendations}
                    </p>

                </div>

            )}

        </div>

    );
}
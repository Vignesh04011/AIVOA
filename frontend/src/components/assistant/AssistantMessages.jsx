export default function AssistantMessages({
    aiResponse,
    loading,
}) {

    if (loading) {
        return (
            <div className="flex-1 p-4">
                🤖 Generating AI insights...
            </div>
        );
    }

    if (!aiResponse) {
        return (
            <div className="flex-1 overflow-y-auto py-4">

                <div className="rounded-lg border border-blue-200 bg-blue-50 p-3 text-sm text-slate-700">

                    👋 Hi! I can help summarize interactions,
                    generate follow-up actions,
                    and suggest next steps.

                </div>

            </div>
        );
    }

    return (

        <div className="space-y-6 overflow-y-auto py-4">

            <div>
                <h3 className="font-semibold">
                    Summary
                </h3>

                <p className="text-sm whitespace-pre-wrap">
                    {aiResponse.summary}
                </p>
            </div>

            <div>
                <h3 className="font-semibold">
                    Medical Insights
                </h3>

                <p className="text-sm whitespace-pre-wrap">
                    {aiResponse.medical_insights}
                </p>
            </div>

            <div>
                <h3 className="font-semibold">
                    Recommendations
                </h3>

                <p className="text-sm whitespace-pre-wrap">
                    {aiResponse.recommendations}
                </p>
            </div>

        </div>

    );
}
import { useEffect, useRef } from "react";

export default function AssistantMessages({

    messages,

    loading,

}) {

    const containerRef = useRef(null);

    useEffect(() => {

        if (containerRef.current) {

            containerRef.current.scrollTop =
                containerRef.current.scrollHeight;

        }

    }, [messages, loading]);

    return (

        <div
            ref={containerRef}
            className="flex-1 overflow-y-auto p-4 space-y-4"
        >

            {messages.length === 0 && (

                <div className="rounded-lg border border-blue-200 bg-blue-50 p-4 text-sm">

                    <h3 className="font-semibold mb-2">
                        🤖 Healthcare CRM Assistant
                    </h3>

                    <p className="mb-3">
                        You can talk to me naturally.
                    </p>

                    <div className="space-y-2">

                        <div>• I met Dr. Smith yesterday around 8 PM.</div>

                        <div>• Actually make it 7 PM.</div>

                        <div>• Remove brochure.</div>

                        <div>• Summarize this interaction.</div>

                        <div>• Give medical insights.</div>

                        <div>• Recommend next steps.</div>

                        <div>• Show all meetings with Dr. Smith.</div>

                        <div>• Log this interaction.</div>

                    </div>

                </div>

            )}

            {messages.map((msg, index) => (

                <div
                    key={index}
                    className={`flex ${
                        msg.role === "user"
                            ? "justify-end"
                            : "justify-start"
                    }`}
                >

                    <div
                        className={`max-w-[92%] rounded-xl p-3 text-sm whitespace-pre-wrap ${
                            msg.role === "user"
                                ? "bg-blue-600 text-white"
                                : "bg-slate-50 border border-slate-200 shadow-sm"
                        }`}
                    >

                        {msg.content}

                    </div>

                </div>

            ))}

            {loading && (

                <div className="flex">

                    <div className="rounded-xl border bg-slate-50 border-slate-200 shadow-sm p-3">

                        🤖 Understanding your request...

                    </div>

                </div>

            )}

        </div>

    );

}
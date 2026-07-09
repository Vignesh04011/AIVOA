import { useState } from "react";

import Header from "../components/layout/Header";
import MainLayout from "../components/layout/MainLayout";

import InteractionForm from "../components/form/InteractionForm";
import AssistantPanel from "../components/assistant/AssistantPanel";

import { createInteraction } from "../services/interactionService";
import { chat } from "../services/aiService";

export default function InteractionPage() {

    const [formData, setFormData] = useState({

        hcp_name: "",
        interaction_type: "",
        interaction_date: "",
        interaction_time: "",
        attendees: "",
        topics_discussed: "",
        materials_shared: "",
        sentiment: "",
        outcomes: "",
        follow_up_actions: "",

    });

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    // -------------------------
    // AI Chat
    // -------------------------
    const handleSendMessage = async (text) => {

        if (!text.trim()) return;

        // Add user message
        setMessages(prev => [

            ...prev,

            {
                role: "user",
                content: text,
            },

        ]);

        try {

            setLoading(true);

            const data = await chat(text, formData);

            // Autofill form after Extract/Edit
            if (
                data.form_data &&
                Object.keys(data.form_data).length > 0
            ) {

                setFormData(data.form_data);

            }

            let assistantReply = "";

            if (data.message) {

                assistantReply += data.message + "\n\n";

            }

            if (data.summary) {

                assistantReply +=
                    "📄 SUMMARY\n\n" +
                    data.summary +
                    "\n\n";

            }

            if (data.medical_insights) {

                assistantReply +=
                    "🩺 MEDICAL INSIGHTS\n\n" +
                    data.medical_insights +
                    "\n\n";

            }

            if (data.recommendations) {

                assistantReply +=
                    "✅ RECOMMENDATIONS\n\n" +
                    data.recommendations +
                    "\n\n";

            }

            if (
                data.search_results &&
                data.search_results.length > 0
            ) {

                assistantReply +=
                    "🔍 SEARCH RESULTS\n\n";

                data.search_results.forEach((item, index) => {

                    assistantReply +=
`${index + 1}. ${item.hcp_name}

Type : ${item.interaction_type}
Date : ${item.interaction_date}
Topic : ${item.topics_discussed}
Sentiment : ${item.sentiment}

`;

                });

            } else if (data.plan?.includes("search")) {

                assistantReply +=
                    "🔍 No matching interactions were found.";

            }

            setMessages(prev => [

                ...prev,

                {

                    role: "assistant",

                    content: assistantReply.trim(),

                },

            ]);

        }

        catch (err) {

            console.error(err);

            setMessages(prev => [

                ...prev,

                {

                    role: "assistant",

                    content:
                        "❌ Sorry, I couldn't process your request. Please try again.",

                },

            ]);

        }

        finally {

            setLoading(false);

        }

    };

    // -------------------------
    // Save Interaction
    // -------------------------
    const handleSubmit = async () => {

        try {

            setLoading(true);

            const response = await createInteraction(formData);

            setMessages(prev => [

                ...prev,

                {

                    role: "assistant",

                    content:
                        response.ai_response?.message ??
                        "✅ Interaction logged successfully.",

                },

            ]);

        }

        catch (err) {

            console.error(err);

            setMessages(prev => [

                ...prev,

                {

                    role: "assistant",

                    content:
                        "❌ Failed to save the interaction.",

                },

            ]);

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <main className="min-h-screen bg-linear-to-br from-slate-100 via-blue-50 to-slate-100">

            <div className="mx-auto max-w-7xl px-8 py-8">

                <Header />

                <MainLayout

                    left={

                        <InteractionForm

                            formData={formData}

                            setFormData={setFormData}

                            onSubmit={handleSubmit}

                            loading={loading}

                        />

                    }

                    right={

                        <AssistantPanel

                            messages={messages}

                            loading={loading}

                            onSend={handleSendMessage}

                        />

                    }

                />

            </div>

        </main>

    );

}
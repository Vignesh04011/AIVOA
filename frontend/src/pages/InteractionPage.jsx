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

  const [loading, setLoading] = useState(false);

const handleAutoFill = async (text) => {

  try {

    setLoading(true);

    const data = await chat(text);

    switch (data.tool) {

      case "extract":
      case "edit":

        setFormData(data.form_data);

        break;

      case "summary":

        setAiResponse(prev => ({
          ...prev,
          summary: data.summary,
          message: data.message,
        }));

        break;

      case "medical":

        setAiResponse(prev => ({
          ...prev,
          medical_insights: data.medical_insights,
          message: data.message,
        }));

        break;

      case "recommendation":

        setAiResponse(prev => ({
          ...prev,
          recommendations: data.recommendations,
          message: data.message,
        }));

        break;

      case "save":

        alert(data.message);

        break;

      default:

        setAiResponse(data);

    }

  } catch (err) {

    console.error(err);

  } finally {

    setLoading(false);

  }

};

const handleSubmit = async () => {
  console.log("FORM DATA:", formData);

  try {
    setLoading(true);

    const response = await createInteraction(formData);

    console.log(response);

    setAiResponse(response.ai_response);

    alert("Interaction Logged Successfully!");

  } catch (err) {

    console.log("ERROR RESPONSE:", err.response);

    console.log("ERROR DATA:", err.response?.data);

    console.error(err);

  } finally {

    setLoading(false);

  }
};

  const [aiResponse, setAiResponse] = useState(null);

  return (
    <main className="min-h-screen bg-[#F5F7FB]">
      <div className="mx-auto max-w-7xl px-8 py-8">

        <Header />

        <MainLayout
          left={
            <InteractionForm
    formData={formData}
    setFormData={setFormData}
    setAiResponse={setAiResponse}
    onSubmit={handleSubmit}
    loading={loading}
/>
          }
          right={
            <AssistantPanel
    aiResponse={aiResponse}
    loading={loading}
    onAutoFill={handleAutoFill}
/>
          }
        />

      </div>
    </main>
  );
}
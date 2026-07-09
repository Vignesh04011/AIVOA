import { useState } from "react";

import Header from "../components/layout/Header";
import MainLayout from "../components/layout/MainLayout";

import InteractionForm from "../components/form/InteractionForm";
import AssistantPanel from "../components/assistant/AssistantPanel";

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
            />
          }
          right={
            <AssistantPanel
              aiResponse={aiResponse}
            />
          }
        />

      </div>
    </main>
  );
}
import Header from "../components/layout/Header";
import MainLayout from "../components/layout/MainLayout";
import InteractionForm from "../components/form/InteractionForm";
import AssistantPanel from "../components/assistant/AssistantPanel";

export default function InteractionPage() {
  return (
    <div className="min-h-screen bg-[#F5F7FB]">
      <div className="mx-auto max-w-7xl p-8">
        <Header />

        <MainLayout
          left={<InteractionForm />}
          right={<AssistantPanel />}
        />
      </div>
    </div>
  );
}
import Input from "../common/Input";
import Select from "../common/Select";
import interactionTypes from "../../constants/interactionTypes";

export default function BasicInfo({
  formData,
  setFormData,
}) {
  return (
    <div className="space-y-5">

      {/* Row 1 */}
      <div className="grid grid-cols-2 gap-5">

        <Input
    label="HCP Name"
    placeholder="Search..."
    value={formData.hcp_name}
    onChange={(e)=>
        setFormData({
            ...formData,
            hcp_name:e.target.value,
        })
    }
/>

        <Select
  label="Interaction Type"
  options={interactionTypes}
  value={formData.interaction_type}
  onChange={(e) =>
    setFormData({
      ...formData,
      interaction_type: e.target.value,
    })
  }
/>

      </div>

      {/* Row 2 */}
      <div className="grid grid-cols-2 gap-5">

        <Input
  label="Date"
  type="date"
  value={formData.interaction_date}
  onChange={(e) =>
    setFormData({
      ...formData,
      interaction_date: e.target.value,
    })
  }
/>

        <Input
  label="Time"
  type="time"
  value={formData.interaction_time}
  onChange={(e) =>
    setFormData({
      ...formData,
      interaction_time: e.target.value,
    })
  }
/>

      </div>

    </div>
  );
}
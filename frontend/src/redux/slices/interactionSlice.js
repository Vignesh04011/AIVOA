import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
  name: "interaction",

  initialState: {
    loading: false,
    aiResponse: null,
    error: null,
  },

  reducers: {

    startLoading(state) {
      state.loading = true;
    },

    setResponse(state, action) {
      state.loading = false;
      state.aiResponse = action.payload;
    },

    setError(state, action) {
      state.loading = false;
      state.error = action.payload;
    },

  },
});

export const {
  startLoading,
  setResponse,
  setError,
} = interactionSlice.actions;

export default interactionSlice.reducer;
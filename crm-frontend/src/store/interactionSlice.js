import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// ✅ Fetch all interactions
export const fetchInteractions = createAsyncThunk(
  "interactions/fetch",
  async () => {
    const res = await axios.get("http://127.0.0.1:8000/interactions");
    return res.data;
  }
);

// ✅ Add interaction (chat input)
export const addInteraction = createAsyncThunk(
  "interactions/add",
  async (data, { dispatch }) => {
    let res;

    if (data.user_input) {
      res = await axios.post("http://127.0.0.1:8000/chat", data);
    } else {
      res = await axios.post("http://127.0.0.1:8000/chat", {
        user_input: data.notes,
      });
    }

    dispatch(fetchInteractions());
    return res.data;
  }
);

// ✅ Edit interaction
export const editInteraction = createAsyncThunk(
  "interactions/edit",
  async ({ id, changes }, { dispatch }) => {
    const res = await axios.put(
      `http://127.0.0.1:8000/edit/${id}`,
      { changes }
    );

    dispatch(fetchInteractions());
    return res.data;
  }
);

// 🔥 FIXED: scheduleFollowup (expects object now)
export const scheduleFollowup = createAsyncThunk(
  "interactions/followup",
  async (data) => {
    const res = await axios.post(
      "http://127.0.0.1:8000/schedule_followup",
      data
    );
    return res.data;
  }
);

// ✅ Generate insights
export const generateInsights = createAsyncThunk(
  "interactions/insights",
  async () => {
    const res = await axios.post(
      "http://127.0.0.1:8000/generate_insights"
    );
    return res.data;
  }
);

// 🔥 FIXED: complianceCheck (expects object now)
export const complianceCheck = createAsyncThunk(
  "interactions/compliance",
  async (data) => {
    const res = await axios.post(
      "http://127.0.0.1:8000/compliance_check",
      data
    );
    return res.data;
  }
);

// ✅ Slice
const interactionSlice = createSlice({
  name: "interactions",
  initialState: {
    list: [],
    insights: null,
    followup: null,
    compliance: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchInteractions.fulfilled, (state, action) => {
      state.list = action.payload;
    });

    builder.addCase(generateInsights.fulfilled, (state, action) => {
      state.insights = action.payload;
    });

    builder.addCase(scheduleFollowup.fulfilled, (state, action) => {
      state.followup = action.payload;
    });

    builder.addCase(complianceCheck.fulfilled, (state, action) => {
      state.compliance = action.payload;
    });
  },
});

export default interactionSlice.reducer;

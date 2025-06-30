import { useState, useCallback } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { BarChart3, PieChart, LineChartIcon, Share2 } from "lucide-react";
import { CategoricalChartState } from "recharts/types/chart/types";

export type MouseMoveState = {
  isTooltipActive: boolean;
  activeTooltipIndex: number;
};

// Sample data
const data = [
  { month: "Jan", impressions: 4000, clicks: 2400 },
  { month: "Feb", impressions: 3000, clicks: 1398 },
  { month: "Mar", impressions: 2000, clicks: 9800 },
  { month: "Apr", impressions: 2780, clicks: 3908 },
  { month: "May", impressions: 1890, clicks: 4800 },
  { month: "Jun", impressions: 2390, clicks: 3800 },
  { month: "Jul", impressions: 3490, clicks: 4300 },
  { month: "Aug", impressions: 3490, clicks: 4300 },
  { month: "Sep", impressions: 3490, clicks: 4300 },
  { month: "Oct", impressions: 3490, clicks: 4300 },
  { month: "Nov", impressions: 3490, clicks: 4300 },
  { month: "Dec", impressions: 3490, clicks: 4300 },
];

const VerticalToolbar = () => (
  <div
    style={{
      display: "flex",
      flexDirection: "column",
      gap: "0.5rem",
      padding: "0.5rem",
      backgroundColor: "#f1f5f9",
      borderRight: "1px solid #e2e8f0",
    }}
  >
    <button title="Bar Chart">
      <BarChart3 size={16} />
    </button>
    <button title="Pie Chart">
      <PieChart size={16} />
    </button>
    <button title="Line Chart">
      <LineChartIcon size={16} />
    </button>
    <button title="Share">
      <Share2 size={16} />
    </button>
  </div>
);

const CustomizedDot = ({ cx, cy }: {
  cx?: string | number;
  cy?: string | number;
}) => {
  return (
    <circle
      cx={cx}
      cy={cy}
      r={4}
      fill="var(--color-impressions, #3b82f6)"
      stroke="white"
      strokeWidth={2}
      style={{ transition: "all 300ms ease-in-out" }}
    />
  );
};

export default function ChartWithToolbar() {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [_, setActiveIndex] = useState<number | undefined>(undefined);

  const handleMouseMove = useCallback((state: CategoricalChartState) => {
    if (state.isTooltipActive) {
      setActiveIndex(state.activeTooltipIndex);
    } else {
      setActiveIndex(undefined);
    }
  }, []);

  return (
    <div
      style={{
        width: "100%",
        maxWidth: "64rem",
        border: "1px solid #e2e8f0",
        borderRadius: "0.5rem",
        overflow: "hidden",
      }}
    >
      <div style={{ display: "flex" }}>
        <VerticalToolbar />
        <div style={{ flexGrow: 1, padding: "1.5rem" }}>
          <div style={{ height: "400px" }}>
            <ResponsiveContainer width="100%" height="100%">
              <LineChart
                data={data}
                margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
                onMouseMove={handleMouseMove}
                onMouseLeave={() => setActiveIndex(undefined)}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="month" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="impressions"
                  stroke="var(--color-impressions, #3b82f6)"
                  dot={<CustomizedDot />}
                  activeDot={{
                    r: 8,
                    fill: "var(--color-impressions, #3b82f6)",
                    stroke: "white",
                    strokeWidth: 2,
                  }}
                />
                <Line
                  type="monotone"
                  dataKey="clicks"
                  stroke="var(--color-clicks, #10b981)"
                  dot={false}
                  activeDot={{
                    r: 8,
                    fill: "var(--color-clicks, #10b981)",
                    stroke: "white",
                    strokeWidth: 2,
                  }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}

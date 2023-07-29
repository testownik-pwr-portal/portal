/* Components */
import { Providers } from "@/lib/providers";

/* Instruments */
import styles from "./styles/layout.module.css";
import "./styles/globals.css";
import { Stack } from "@mui/material";
import TestListItem from "./components/TestList/TestListItem";

const mockListTitles = [
  "Test 1",
  "Test 2",
  "Test 3",
  "Test 4",
  "Test 5",
  "Test 6",
];

export default function RootLayout(props: React.PropsWithChildren) {
  return (
    <Providers>
      <html lang="en">
        <body>
          <Stack direction="column" spacing={0}>
            {mockListTitles.map((title) => (
              <TestListItem title={title} />
            ))}
          </Stack>
        </body>
      </html>
    </Providers>
  );
}

import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";

export default function ParentalControls() {
  const [controls, setControls] = useState({
    contentFilter: true,
    screenTimeLimit: false,
    timeLimitHours: 2,
    bedtimeLock: false,
    bedtimeHour: "21:00",
    pin: ""
  });

  const toggleControl = (key) => {
    setControls((prev) => ({ ...prev, [key]: !prev[key] }));
  };

  const handleChange = (key, value) => {
    setControls((prev) => ({ ...prev, [key]: value }));
  };

  return (
    <Card className="p-4 shadow-xl max-w-2xl mx-auto mt-10">
      <CardContent className="space-y-6">
        <h2 className="text-2xl font-bold">Parental Controls</h2>

        <Tabs defaultValue="settings">
          <TabsList className="grid grid-cols-2">
            <TabsTrigger value="settings">Settings</TabsTrigger>
            <TabsTrigger value="security">Security</TabsTrigger>
          </TabsList>

          <TabsContent value="settings" className="space-y-4">
            <div className="flex items-center justify-between">
              <Label>Content Filter</Label>
              <Switch checked={controls.contentFilter} onCheckedChange={() => toggleControl("contentFilter")} />
            </div>

            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <Label>Screen Time Limit</Label>
                <Switch checked={controls.screenTimeLimit} onCheckedChange={() => toggleControl("screenTimeLimit")} />
              </div>
              {controls.screenTimeLimit && (
                <Input
                  type="number"
                  min="1"
                  max="12"
                  value={controls.timeLimitHours}
                  onChange={(e) => handleChange("timeLimitHours", e.target.value)}
                  placeholder="Hours per day"
                />
              )}
            </div>

            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <Label>Bedtime Lock</Label>
                <Switch checked={controls.bedtimeLock} onCheckedChange={() => toggleControl("bedtimeLock")} />
              </div>
              {controls.bedtimeLock && (
                <Input
                  type="time"
                  value={controls.bedtimeHour}
                  onChange={(e) => handleChange("bedtimeHour", e.target.value)}
                />
              )}
            </div>
          </TabsContent>

          <TabsContent value="security" className="space-y-4">
            <div className="space-y-2">
              <Label>Set Parental PIN</Label>
              <Input
                type="password"
                value={controls.pin}
                onChange={(e) => handleChange("pin", e.target.value)}
                placeholder="Enter a 4-digit PIN"
                maxLength={4}
              />
            </div>
            <Button className="w-full">Save Settings</Button>
          </TabsContent>
        </Tabs>
      </CardContent>
    </Card>
  );
}

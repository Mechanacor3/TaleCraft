// This file exports TypeScript types and interfaces used throughout the application.

export interface StoryIdea {
  id: string;
  content: string;
  createdAt: Date;
}

export interface StoryOutline {
  id: string;
  title: string;
  beats: StoryBeat[];
}

export interface StoryBeat {
  id: string;
  description: string;
  approved: boolean;
}

export interface ImageGenerationPrompt {
  beatId: string;
  prompt: string;
}

export interface Script {
  id: string;
  dialogue: string;
  timing: number; // in seconds
}

export interface AudioClip {
  id: string;
  voiceStyle: string;
  audioUrl: string;
}

export interface VideoAssembly {
  images: string[];
  audioClips: AudioClip[];
  animations: AnimationStyle[];
}

export interface AnimationStyle {
  type: string; // e.g., 'pan', 'zoom', 'fade'
  duration: number; // in seconds
}

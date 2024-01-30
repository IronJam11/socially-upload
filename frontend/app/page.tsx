import { getServerSession } from "next-auth";
import { authOptions } from "./utils/auth";
import LogoutButton from "./components/LogoutButton";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import Header from "./components/header";


export default async function Home() 
{

  return <> 
  <Header />
  <div>You successfully logged in</div> 
  <div className = "flex"><b> Go to </b> </div>

  <br/>
  <a href="/blogpage">Blogs</a> <br/>
  <a href="/posts">Posts</a> <br/>
  <a href="/jokes">Jokes</a> <br/>
  <a href="/memes">Memes</a> <br/>
  <a href="/aboutus">About Us</a> <br/>
  
  </>
  
}

 
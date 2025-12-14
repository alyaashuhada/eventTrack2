@extends('layouts.app')

@section('content')
<div class="auth-container" role="main" aria-label="Login">
  <div class="auth-card">
    <header class="auth-header">
      <h1>Sign in to your account</h1>
      <p class="muted">Welcome back — please enter your credentials to continue.</p>
    </header>

    @if (session('status'))
      <div class="alert alert-success" role="status">
        {{ session('status') }}
      </div>
    @endif

    <form method="POST" action="{{ route('login') }}" novalidate class="auth-form" aria-describedby="login-instructions">
      @csrf

      <p id="login-instructions" class="sr-only">Use your email and password to sign in. Required fields are marked.</p>

      <!-- Email -->
      <div class="form-group">
        <label for="email">Email address</label>
        <input
          id="email"
          type="email"
          name="email"
          value="{{ old('email') }}"
          required
          autocomplete="email"
          autofocus
          aria-required="true"
          aria-invalid="{{ $errors->has('email') ? 'true' : 'false' }}"
          aria-describedby="{{ $errors->has('email') ? 'email-error' : '' }}"
          class="form-control{{ $errors->has('email') ? ' is-invalid' : '' }}"
          placeholder="you@example.com"
        >
        @if ($errors->has('email'))
          <div id="email-error" class="error" role="alert">{{ $errors->first('email') }}</div>
        @endif
      </div>

      <!-- Password -->
      <div class="form-group">
        <label for="password">Password</label>
        <div class="password-wrapper">
          <input
            id="password"
            type="password"
            name="password"
            required
            autocomplete="current-password"
            aria-required="true"
            aria-invalid="{{ $errors->has('password') ? 'true' : 'false' }}"
            aria-describedby="{{ $errors->has('password') ? 'password-error' : '' }}"
            class="form-control{{ $errors->has('password') ? ' is-invalid' : '' }}"
            placeholder="Your secure password"
          >
          <button type="button" class="toggle-password" aria-label="Show password" title="Show password">Show</button>
        </div>
        @if ($errors->has('password'))
          <div id="password-error" class="error" role="alert">{{ $errors->first('password') }}</div>
        @endif
      </div>

      <!-- Remember + Forgot -->
      <div class="form-row space-between">
        <label class="checkbox">
          <input type="checkbox" name="remember" {{ old('remember') ? 'checked' : '' }}>
          <span>Remember me</span>
        </label>

        @if (Route::has('password.request'))
          <a class="link" href="{{ route('password.request') }}">Forgot your password?</a>
        @endif
      </div>

      <div class="form-group">
        <button type="submit" class="btn-primary" aria-live="polite">
          Sign in
        </button>
      </div>

      @if(config('services') && (config('services.google') || config('services.github') || config('services.facebook')))
        <div class="divider"><span>or continue with</span></div>
        <div class="socials">
          @if(config('services.google'))
            <a href="{{ route('social.redirect', 'google') }}" class="btn-social">Google</a>
          @endif
          @if(config('services.github'))
            <a href="{{ route('social.redirect', 'github') }}" class="btn-social">GitHub</a>
          @endif
          @if(config('services.facebook'))
            <a href="{{ route('social.redirect', 'facebook') }}" class="btn-social">Facebook</a>
          @endif
        </div>
      @endif

      <p class="signup-note">
        Don't have an account? <a href="{{ route('register') }}">Create one</a>.
      </p>
    </form>
  </div>
</div>

<style>
  .auth-container{
    min-height: 70vh;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:2rem;
  }
  .auth-card{
    width:100%;
    max-width:430px;
    background:#fff;
    border:1px solid #e6e6e6;
    border-radius:10px;
    padding:1.5rem;
    box-shadow:0 6px 20px rgba(18,22,28,0.06);
  }
  .auth-header h1{margin:0 0 .25rem;font-size:1.4rem}
  .muted{color:#6b7280;margin:0 0 1rem;font-size:.95rem}
  .form-group{margin-bottom:1rem}
  label{display:block;margin-bottom:.35rem;font-weight:600}
  .form-control{
    width:100%;
    padding:.55rem .75rem;
    border:1px solid #cbd5e1;
    border-radius:6px;
    font-size:1rem;
  }
  .form-control:focus{outline:none;border-color:#6b8cff;box-shadow:0 0 0 3px rgba(107,140,255,0.12)}
  .is-invalid{border-color:#ef4444}
  .error{color:#b91c1c;margin-top:.375rem;font-size:.9rem}
  .space-between{display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem}
  .checkbox{display:flex;align-items:center;gap:.5rem;font-weight:500}
  .link{font-size:.95rem;color:#2563eb;text-decoration:none}
  .link:hover{text-decoration:underline}
  .btn-primary{
    width:100%;
    background:#0f172a;color:#fff;padding:.65rem .8rem;border-radius:8px;border:0;font-weight:700;font-size:1rem;
  }
  .btn-primary:hover{filter:brightness(.98)}
  .divider{display:flex;align-items:center;margin:1rem 0;color:#6b7280;font-size:.9rem}
  .divider::before,.divider::after{content:"";flex:1;height:1px;background:#e6e6e6;margin:0 .75rem}
  .socials{display:flex;gap:.5rem;flex-wrap:wrap}
  .btn-social{flex:1;padding:.5rem .6rem;border-radius:8px;text-align:center;background:#f3f4f6;border:1px solid #e6e6e6;color:#111;text-decoration:none}
  .signup-note{margin-top:1rem;color:#6b7280;font-size:.95rem}
  .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  .password-wrapper{position:relative}
  .toggle-password{
    position:absolute;right:.35rem;top:50%;transform:translateY(-50%);
    background:transparent;border:0;color:#374151;padding:.2rem .4rem;border-radius:6px;cursor:pointer;font-weight:600
  }
  @media (max-width:480px){
    .auth-card{padding:1rem;border-radius:8px}
  }
</style>

<script>
  (function(){
    const toggle = document.querySelector('.toggle-password');
    const pwd = document.getElementById('password');
    if (!toggle || !pwd) return;

    toggle.addEventListener('click', function(){
      const type = pwd.getAttribute('type') === 'password' ? 'text' : 'password';
      pwd.setAttribute('type', type);
      this.textContent = type === 'password' ? 'Show' : 'Hide';
      this.setAttribute('aria-pressed', type === 'text');
      this.setAttribute('aria-label', type === 'text' ? 'Hide password' : 'Show password');
    });

    // Prevent form resubmission accidental double submits
    const form = document.querySelector('.auth-form');
    if (form) {
      form.addEventListener('submit', function(e){
        const btn = form.querySelector('button[type="submit"]');
        if (btn){
          btn.disabled = true;
          btn.setAttribute('aria-busy', 'true');
        }
      });
    }
  })();
</script>
@endsection
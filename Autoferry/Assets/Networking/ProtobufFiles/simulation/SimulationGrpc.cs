// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: simulation/simulation.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Simulation {
  /// <summary>
  ///Input forces from OSP, step Unity the duration of "stepSize", return position and velocity
  /// </summary>
  public static partial class Simulation
  {
    static readonly string __ServiceName = "simulation.Simulation";

    static readonly grpc::Marshaller<global::Simulation.StepRequest> __Marshaller_simulation_StepRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Simulation.StepRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Simulation.StepResponse> __Marshaller_simulation_StepResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Simulation.StepResponse.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Simulation.ResetRequest> __Marshaller_simulation_ResetRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Simulation.ResetRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Simulation.ResetResponse> __Marshaller_simulation_ResetResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Simulation.ResetResponse.Parser.ParseFrom);

    static readonly grpc::Method<global::Simulation.StepRequest, global::Simulation.StepResponse> __Method_DoStep = new grpc::Method<global::Simulation.StepRequest, global::Simulation.StepResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "DoStep",
        __Marshaller_simulation_StepRequest,
        __Marshaller_simulation_StepResponse);

    static readonly grpc::Method<global::Simulation.ResetRequest, global::Simulation.ResetResponse> __Method_Reset = new grpc::Method<global::Simulation.ResetRequest, global::Simulation.ResetResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "Reset",
        __Marshaller_simulation_ResetRequest,
        __Marshaller_simulation_ResetResponse);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Simulation.SimulationReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of Simulation</summary>
    [grpc::BindServiceMethod(typeof(Simulation), "BindService")]
    public abstract partial class SimulationBase
    {
      public virtual global::System.Threading.Tasks.Task<global::Simulation.StepResponse> DoStep(global::Simulation.StepRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      /// <summary>
      ///Reset the position and velocity of a vessel to the specified values
      /// </summary>
      /// <param name="request">The request received from the client.</param>
      /// <param name="context">The context of the server-side call handler being invoked.</param>
      /// <returns>The response to send back to the client (wrapped by a task).</returns>
      public virtual global::System.Threading.Tasks.Task<global::Simulation.ResetResponse> Reset(global::Simulation.ResetRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for Simulation</summary>
    public partial class SimulationClient : grpc::ClientBase<SimulationClient>
    {
      /// <summary>Creates a new client for Simulation</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public SimulationClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for Simulation that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public SimulationClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected SimulationClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected SimulationClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual global::Simulation.StepResponse DoStep(global::Simulation.StepRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return DoStep(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Simulation.StepResponse DoStep(global::Simulation.StepRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_DoStep, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Simulation.StepResponse> DoStepAsync(global::Simulation.StepRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return DoStepAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Simulation.StepResponse> DoStepAsync(global::Simulation.StepRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_DoStep, null, options, request);
      }
      /// <summary>
      ///Reset the position and velocity of a vessel to the specified values
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      public virtual global::Simulation.ResetResponse Reset(global::Simulation.ResetRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return Reset(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///Reset the position and velocity of a vessel to the specified values
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      public virtual global::Simulation.ResetResponse Reset(global::Simulation.ResetRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_Reset, null, options, request);
      }
      /// <summary>
      ///Reset the position and velocity of a vessel to the specified values
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      public virtual grpc::AsyncUnaryCall<global::Simulation.ResetResponse> ResetAsync(global::Simulation.ResetRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return ResetAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///Reset the position and velocity of a vessel to the specified values
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      public virtual grpc::AsyncUnaryCall<global::Simulation.ResetResponse> ResetAsync(global::Simulation.ResetRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_Reset, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override SimulationClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new SimulationClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(SimulationBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_DoStep, serviceImpl.DoStep)
          .AddMethod(__Method_Reset, serviceImpl.Reset).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static void BindService(grpc::ServiceBinderBase serviceBinder, SimulationBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_DoStep, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Simulation.StepRequest, global::Simulation.StepResponse>(serviceImpl.DoStep));
      serviceBinder.AddMethod(__Method_Reset, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Simulation.ResetRequest, global::Simulation.ResetResponse>(serviceImpl.Reset));
    }

  }
}
#endregion
